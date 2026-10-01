from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

from gtm_agent.tools.company import get_company
from gtm_agent.tools.contact import get_contact
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage ,ToolMessage



model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", api_key=api_key)

model_with_tools = model.bind_tools([get_company, get_contact])


tool_registry = {
    "get_company": get_company,
    "get_contact": get_contact,
}


SYSTEM_MESSAGE = """You are a helpful assistant that can answer questions about companies and contacts.
You can use the following tools to get more information about companies and contacts:
get_company: Retrieves a company from the data store by its ID.
get_contact: Retrieves a contact from the data store by its ID.
"""

if __name__ == "__main__":
    sys_msg = SystemMessage(content=SYSTEM_MESSAGE)

    question = "For company ID 1, tell me the company name, the contact's full name, and their job title."
    history = [sys_msg, HumanMessage(content=question)]
    response = model_with_tools.invoke([sys_msg, HumanMessage(content=question)])
    history.append(response)


    while response.tool_calls:
        for tool_call in response.tool_calls:
            print(f"Tool Call: {tool_call['name']} with args: {tool_call['args']}")
            tool_result = tool_registry[tool_call["name"]].invoke(tool_call["args"])
            print("Tool result:", tool_result)
            print("Tool result type:", type(tool_result))
            print("Tool call ID:", tool_call["id"])
            tool_msg=ToolMessage(content=str(tool_result.model_dump()), tool_call_id=tool_call["id"])
            print("Tool message:", tool_msg)
            history.append(tool_msg)

        response = model_with_tools.invoke(history)
        history.append(response)

    print("Final Response:", response.content)
    print("Final Response Type:", type(response.content))
    print("Final Response Object:", response)


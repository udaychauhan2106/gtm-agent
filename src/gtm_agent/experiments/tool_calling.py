from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

from gtm_agent.tools.company import get_company
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage


model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", api_key=api_key)

model_with_tools = model.bind_tools([get_company])

SYSTEM_MESSAGE = """You are a helpful assistant that can answer questions about companies.
You can use the following tools to get more information about a company:
get_company: Retrieves a company from the data store by its ID.
"""

prompt = SystemMessage(content=SYSTEM_MESSAGE)

question = "What is the name of the company with ID 1?"
response = model_with_tools.invoke([prompt, HumanMessage(content=question)])

print(response.tool_calls)
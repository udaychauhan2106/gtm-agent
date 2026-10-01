from gtm_agent.graphs.state import State
from gtm_agent.experiments.tool_calling import model_with_tools , tool_registry
from langchain.messages import ToolMessage

def agent(state: State):
    response=model_with_tools.invoke(state["messages"])   
    return {
        "messages":[response]
    }

def tools(state:State):
    tool_message=[]
    for tool_call in state["messages"][-1].tool_calls:
        print(f"Tool Call: {tool_call['name']} with args: {tool_call['args']}")
        tool_result = tool_registry[tool_call["name"]].invoke(tool_call["args"])
        print("Tool result:", tool_result)
        tool_message.append(ToolMessage(content=str(tool_result.model_dump()), tool_call_id=tool_call["id"]))
    return {
        "messages":tool_message
    }



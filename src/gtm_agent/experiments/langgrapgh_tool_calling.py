from langgraph.graph import START,END,StateGraph
from gtm_agent.graphs.state import State
from gtm_agent.graphs.tool_nodes import agent
from langchain.messages import SystemMessage, HumanMessage
from gtm_agent.graphs.tool_nodes import tools


def route(state: State):
    if state["messages"][-1].tool_calls:
        return "tools"
    else:
        return "END"

builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", tools)
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", route ,{"tools":"tools","END":END})
builder.add_edge("tools", "agent")

SYSTEM_MESSAGE = """You are a helpful assistant that can answer questions about companies and contacts.
You can use the available tools when necessary.
"""

initial_state = {
    "messages": [
        SystemMessage(content=SYSTEM_MESSAGE),
        HumanMessage(
            content="What is the name of the contact with ID 1?"
        ),
    ]
}


graph = builder.compile()
print(graph.get_graph().draw_ascii())
result = graph.invoke(initial_state)

print(result)
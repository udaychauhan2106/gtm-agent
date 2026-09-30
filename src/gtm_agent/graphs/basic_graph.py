from typing import TypedDict , Literal
from langgraph.graph import START,END,StateGraph
from .state import State
from gtm_agent.domain.models.company import Company
from gtm_agent.domain.models.contact import Contact

def load_lead(state: State):

    lead = state["lead"]
    company = Company(lead.company_id)
    contact = Contact(lead.contact_id)
    return{
        "company": company,
        "contact": contact
    }


def qualify_lead(state: State):
    if state["company"].website:
        return{
            qualified: True,
        }
    else:
        return{
            
        }
def research_lead(state: State):
    return{
        "researched":True
    }
def route(state: State):
    if state["is_adult"]:
        return "research_lead"
    else:
        return END

builder = StateGraph(State)
builder.add_node("load_lead", load_lead)
builder.add_edge(START, "load_lead")
builder.add_node("qualify_lead", qualify_lead)
builder.add_node("research_lead", research_lead)
builder.add_edge("load_lead", "qualify_lead")
builder.add_conditional_edges("qualify_lead", route)
builder.add_edge("research_lead", END)

graph = builder.compile()

result = graph.invoke({
    "name": "John Doe",
    "age": 20,
})

print(result)
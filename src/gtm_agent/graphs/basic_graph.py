from typing import TypedDict , Literal
from langgraph.graph import START,END,StateGraph
from .state import State
from gtm_agent.domain.models.company import Company
from gtm_agent.domain.models.contact import Contact
from gtm_agent.domain.models.source import Source
from gtm_agent.domain.models.signal import Signal, SignalType
from gtm_agent.domain.models.research import ResearchReport
import datetime

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
            "qualified": True,
            "qualification_reason": "website_exists"
        }
    else:
        return{
            "qualified": False,
            "qualification_reason": "no_website"
        }
def research_lead(state: State):
    company = state["company"]

    now = datetime.datetime.now(datetime.timezone.utc)

    source = Source(
        url=company.website,
        title=f"{company.name} Website",
        source_type="company_website",
        retrieved_at=now,
    )

    signal = Signal(
        type=SignalType.OTHER,
        sources=[source],
        claim=f"{company.name} has an active company website",
        evidence=f"Company website: {company.website}",
        detected_at=now,
        confidence=1.0,
    )

    report = ResearchReport(
        company_id=company.id,
        summary=f"Initial research for {company.name}.",
        sources=[source],
        signals=[signal],
        researched_at=now,
        research_version="0.1",
    )

    return {
        "research_report": report
    }

def route(state: State):
    if state["qualified"]:
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
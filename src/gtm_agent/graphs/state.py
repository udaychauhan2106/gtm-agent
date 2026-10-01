from typing import TypedDict , NotRequired , Annotated
from langchain.messages import AnyMessage
from langgraph.graph.message import add_messages
from gtm_agent.domain.models.company import Company
from gtm_agent.domain.models.contact import Contact
from gtm_agent.domain.models.lead import Lead
from gtm_agent.domain.models.research import ResearchReport


class State(TypedDict):
    company: NotRequired[Company]
    contact: NotRequired[Contact]
    lead: Lead
    research_report: NotRequired[ResearchReport]
    qualified: NotRequired[bool]
    qualification_reason: NotRequired[str]
    messages: Annotated[list[AnyMessage], add_messages]
from typing import TypedDict , NotRequired
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
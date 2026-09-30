
from pydantic import BaseModel , Field
from typing import Optional
from .signal import Signal
from .source import Source
import datetime

class ResearchReport(BaseModel):
    company_id: int
    summary: str
    sources: list[Source]
    signals: list[Signal]
    researched_at: datetime.datetime
    research_version: Optional[str] = Field(None, description="Version of the research")


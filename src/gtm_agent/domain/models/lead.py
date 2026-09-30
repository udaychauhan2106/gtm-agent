from pydantic import BaseModel , Field
from typing import Optional ,Any
from enum import Enum
import datetime

class LeadStatus(str, Enum):
    NEW="new"
    RESEARCHING = "researching"
    QUALIFIED = "qualified"
    DISQUALIFIED= "disqualified"
    DRAFTED="drafted"
    APPROVED="approved"
    CONTACTED="contacted"
    REPLIED="replied"

class Lead(BaseModel):
    id: int
    company_id: int
    contact_id: int
    source: Optional[str] =Field(None, description="Source of the lead")
    status: LeadStatus = Field(LeadStatus.NEW, description="Status of the lead")
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = Field(None, description="Last updated timestamp")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the lead")
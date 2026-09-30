from pydantic import BaseModel , Field
from typing import Optional
from .source import Source
from enum import Enum
import datetime

class SignalType(str, Enum):
    FUNDING = "funding"
    HIRING = "hiring"
    PRODUCT_LAUNCH = "product_launch"
    EXPANSION = "expansion"
    LEADERSHIP_CHANGE = "leadership_change"
    GROWTH = "growth"
    PAIN_POINT = "pain_point"
    TECHNOLOGY_ADOPTION = "technology_adoption"
    OTHER = "other"

class Signal(BaseModel):
    type: SignalType    
    sources: list[Source] = Field(default_factory=list,min_items=1, description="Sources of the signal")
    claim: str = Field(..., description="Claim of the signal")
    evidence: str = Field(..., description="Evidence of the signal")
    detected_at: datetime.datetime
    confidence: Optional[float] = Field(None ,ge=0.0, le=1.0, description="Confidence of the signal")


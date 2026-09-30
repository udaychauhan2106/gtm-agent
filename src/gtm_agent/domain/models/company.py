

from pydantic import BaseModel , Field
from typing import Any, Optional

class Company(BaseModel):
    id: int  
    name: str
    website: str
    industry: Optional[str] = Field(None, description="Industry of the company")
    employee_count: Optional[int] = Field(None, description="Number of employees in the company")
    location: Optional[str] = Field(None, description="Location of the company")
    metadata: dict[str,Any] = Field(default_factory=dict, description="Additional metadata about the company")

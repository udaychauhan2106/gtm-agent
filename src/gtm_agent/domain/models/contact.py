
from pydantic import BaseModel , Field
from typing import Optional , Any

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = Field(None, description="Phone number of the contact")
    company_id: int
    job_title: Optional[str] = Field(None, description="Job title of the contact")
    linkedin_url: Optional[str] = Field(None, description="LinkedIn profile URL of the contact")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the contact")

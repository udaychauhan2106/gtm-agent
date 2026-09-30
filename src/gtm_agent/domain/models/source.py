from pydantic import BaseModel , Field
from typing import Optional
import datetime

class Source(BaseModel):
    url: str
    title: Optional[str] = Field(None, description="Title of the source")
    source_type: Optional[str] = Field(None, description="Type of the source (e.g., article, blog, report)")
    published_at: Optional[datetime.datetime] = Field(None, description="Publication date of the source")
    retrieved_at: datetime.datetime
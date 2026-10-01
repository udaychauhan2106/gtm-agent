

from gtm_agent.domain.models.company import Company
from gtm_agent.domain.models.contact import Contact


companies = {
    1: Company(
        id=1,
        name="Acme Technologies",
        website="https://acme.example.com",
        industry="SaaS",
        employee_count=120,
        location="Bengaluru, India",
    ),
    2: Company(
        id=2,
        name="Nova Health",
        website="https://novahealth.example.com",
        industry="Healthcare",
        employee_count=85,
        location="Delhi, India",
    ),
    3: Company(
        id=3,
        name="FinEdge",
        website="https://finedge.example.com",
        industry="FinTech",
        employee_count=250,
        location="Mumbai, India",
    ),
    4: Company(
        id=4,
        name="GreenGrid Energy",
        website="https://greengrid.example.com",
        industry="Renewable Energy",
        employee_count=60,
        location="Hyderabad, India",
    ),
    5: Company(
        id=5,
        name="CloudStack Labs",
        website="https://cloudstack.example.com",
        industry="Cloud Computing",
        employee_count=180,
        location="Pune, India",
    ),
}
contacts = {}
leads = {}
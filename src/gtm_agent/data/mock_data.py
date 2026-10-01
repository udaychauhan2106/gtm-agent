

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
contacts = {
    1: Contact(
        id=1,
        first_name="Rahul",
        last_name="Sharma",
        email="rahul.sharma@acme.example.com",
        phone="+91-9876543210",
        company_id=1,
        job_title="Head of Sales",
        linkedin_url="https://linkedin.com/in/rahul-sharma",
    ),
    2: Contact(
        id=2,
        first_name="Priya",
        last_name="Mehta",
        email="priya.mehta@novahealth.example.com",
        phone="+91-9876543211",
        company_id=2,
        job_title="VP of Operations",
        linkedin_url="https://linkedin.com/in/priya-mehta",
    ),
    3: Contact(
        id=3,
        first_name="Arjun",
        last_name="Patel",
        email="arjun.patel@finedge.example.com",
        phone="+91-9876543212",
        company_id=3,
        job_title="CTO",
        linkedin_url="https://linkedin.com/in/arjun-patel",
    ),
    4: Contact(
        id=4,
        first_name="Neha",
        last_name="Verma",
        email="neha.verma@greengrid.example.com",
        phone="+91-9876543213",
        company_id=4,
        job_title="Chief Growth Officer",
        linkedin_url="https://linkedin.com/in/neha-verma",
    ),
    5: Contact(
        id=5,
        first_name="Vikram",
        last_name="Singh",
        email="vikram.singh@cloudstack.example.com",
        phone="+91-9876543214",
        company_id=5,
        job_title="Director of Engineering",
        linkedin_url="https://linkedin.com/in/vikram-singh",
    ),
}
leads = {}
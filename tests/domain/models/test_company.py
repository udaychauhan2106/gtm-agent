from gtm_agent.domain.models.company import Company

def test_company():

    company = Company(id=1, name="Google", website="https://www.google.com", industry="Technology", location="Mountain View, CA")
    assert company.id == 1
    assert company.name == "Google"
    assert company.website == "https://www.google.com"
    assert company.metadata == {}
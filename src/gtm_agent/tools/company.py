from gtm_agent.data.mock_data import companies
from gtm_agent.domain.models.company import Company
from langchain.tools import tool


@tool("get_company")
def get_company(company_id: int) -> Company:
    """Retrieve a company from the data store by its ID.
        Args:
            company_id (int): The ID of the company to retrieve.
        Returns:
            Company: The company object corresponding to the provided ID.
    """

    if company_id in companies:
        return companies[company_id]
    
    raise ValueError(f"Company with ID {company_id} not found.")
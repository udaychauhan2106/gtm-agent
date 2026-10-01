from gtm_agent.data.mock_data import contacts
from gtm_agent.domain.models.contact import Contact
from langchain.tools import tool


@tool("get_contact")
def get_contact(contact_id: int) -> Contact:
    """Retrieve a contact from the data store by its ID.
        Args:
            contact_id (int): The ID of the contact to retrieve.
        Returns:
            Contact: The contact object corresponding to the provided ID.
    """

    if contact_id in contacts:
        return contacts[contact_id]
    
    raise ValueError(f"Contact with ID {contact_id} not found.")
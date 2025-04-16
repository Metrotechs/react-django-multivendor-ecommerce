from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput

class HubSpotIntegration:
    def __init__(self, api_key):
        self.client = HubSpot(api_key=api_key)

    def create_contact(self, email, first_name, last_name):
        contact_input = SimplePublicObjectInput(properties={
            "email": email,
            "firstname": first_name,
            "lastname": last_name
        })
        response = self.client.crm.contacts.basic_api.create(simple_public_object_input=contact_input)
        return response

    def get_contact(self, contact_id):
        response = self.client.crm.contacts.basic_api.get_by_id(contact_id)
        return response

    def update_contact(self, contact_id, properties):
        contact_input = SimplePublicObjectInput(properties=properties)
        response = self.client.crm.contacts.basic_api.update(contact_id, simple_public_object_input=contact_input)
        return response

    def delete_contact(self, contact_id):
        self.client.crm.contacts.basic_api.archive(contact_id)
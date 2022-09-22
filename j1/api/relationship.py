from j1.api.api_client import ApiClient
from typing import Dict, List

from j1.api.queries import (
    CREATE_RELATIONSHIP,
    DELETE_RELATIONSHIP
)
    
class Relationship(ApiClient): 
    def create(self,
               relationship_key: str,
               relationship_type: str,
               relationship_class: str,
               from_entity_id: str,
               to_entity_id: str):
        variables = {
            'relationshipKey': relationship_key,
            'relationshipType': relationship_type,
            'relationshipClass': relationship_class,
            'fromEntityId': from_entity_id,
            'toEntityId': to_entity_id
        }

        response = self.execute_query(
            self.config.get_query_endpont(),
            query=CREATE_RELATIONSHIP,
            variables=variables
        )
        if response:
            return response['data']['createRelationship']

    def delete(self, relationship_id: str):
        """ Deletes a relationship between two entities.

        args:
            relationship_id (str): The ID of the relationship
        """
        variables = {
            'relationshipId': relationship_id
        }

        response = self.execute_query(
            self.config.get_query_endpont(),
            DELETE_RELATIONSHIP,
            variables=variables
        )

        if response:
            return response['data']['deleteRelationship']

from j1.api.api_client import ApiClient
from typing import Dict, List

from j1.queries import (
    CREATE_RELATIONSHIP,
    DELETE_RELATIONSHIP
)
    
class Relationship(ApiClient): 
    
    def create_relationship(self, **kwargs) -> Dict:
        """
        Create a relationship (edge) between two entities (veritces).

        args:
            relationship_key (str): Unique key for the relationship
            relationship_type (str): Value for _type of relationship
            relationship_class (str): Value for _class of relationship
            from_entity_id (str): Entity ID of the source vertex
            to_entity_id (str): Entity ID of the destination vertex
        """
        variables = {
            'relationshipKey': kwargs.pop('relationship_key'),
            'relationshipType': kwargs.pop('relationship_type'),
            'relationshipClass': kwargs.pop('relationship_class'),
            'fromEntityId': kwargs.pop('from_entity_id'),
            'toEntityId': kwargs.pop('to_entity_id')
        }

        properties = kwargs.pop('properties', None)
        if properties:
            variables['properties'] = properties

        response = self._execute_query(
            query=CREATE_RELATIONSHIP,
            variables=variables
        )
        return response['data']['createRelationship']

    def delete_relationship(self, relationship_id: str = None):
        """ Deletes a relationship between two entities.

        args:
            relationship_id (str): The ID of the relationship
        """
        variables = {
            'relationshipId': relationship_id
        }

        response = self._execute_query(
            DELETE_RELATIONSHIP,
            variables=variables
        )
        return response['data']['deleteRelationship']
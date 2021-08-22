from .api_client import ApiClient
from typing import Dict, List

from .queries import (
    CREATE_ENTITY,
    DELETE_ENTITY,
    UPDATE_ENTITY,
)
    
class Entity(ApiClient):
    def __init__(self, config, call_back=None):
        super(Entity, self).__init__(config)
  
    def create(self,
               entity_key: str = None,
               entity_type: str = None,
               entity_class: str = None,
               timestamp: int=None,
               properties: Dict = None):
        variables = {
            'entityKey': entity_key,
            'entityType': entity_type,
            'entityClass': entity_class
        }

        timestamp: int = timestamp
        properties: Dict = properties

        if timestamp:
            variables.update(timestamp=timestamp)
        if properties:
            variables.update(properties=properties)

        response = self.execute_query(
            self.config.get_query_endpont(),
            query=CREATE_ENTITY,
            variables=variables
        )
        return response['data']['createEntity']

    
    def update(self, entity_id: str = None, properties: Dict = None) -> Dict:
        """
        Update an existing entity.

        args:
            entity_id (str): The _id of the entity to udate
            properties (dict): Dictionary of key/value entity properties
        """
        variables = {
            'entityId': entity_id,
            'properties': properties
        }
        response = self.execute_query(
                        self.config.get_query_endpont(),
                        UPDATE_ENTITY,
                        variables=variables
                        )
        return response['data']['updateEntity']

    def delete(self, entity_id: str = None, hard_delete: bool = True):
        """ Deletes an entity from the graph.  Note this is a hard delete.

        args:
            entity_id (str): Entity ID for entity to delete
        """
        variables = {
            'entityId': entity_id
        }
        response = self.execute_query(
                    self.config.get_query_endpont(),
                    DELETE_ENTITY,
                    variables=variables
                    )
        return response['data']['deleteEntity']

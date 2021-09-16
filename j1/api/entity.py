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
        variables = {
            'entityId': entity_id,
            'hardDelete': hard_delete
        }
        response = self.execute_query(
                    self.config.get_query_endpont(),
                    DELETE_ENTITY,
                    variables=variables
                    )
        print("WOMBAT: ")
        print(response)
        return response['data']['deleteEntity']

    def upsert_raw_data(self):
        return
from .api_client import ApiClient
from typing import Dict

from .queries import (
    CREATE_ENTITY,
    DELETE_ENTITY,
    UPDATE_ENTITY,
)
    
class Entity(ApiClient):
    def __init__(self, config):
        super(Entity, self).__init__(config)
  
    def create(self,
               entity_key: str,
               entity_type: str,
               entity_class: str,):
        variables = {
            'entityKey': entity_key,
            'entityType': entity_type,
            'entityClass': entity_class
        }

        response = self.execute_query(
            self.config.get_query_endpont(),
            query=CREATE_ENTITY,
            variables=variables
        )
        if response:
            return response['data']['createEntity']
        else:
            return None

    
    def update(self, entity_id: str, properties: Dict):
        variables = {
            'entityId': entity_id,
            'properties': properties
        }
        response = self.execute_query(
                        self.config.get_query_endpont(),
                        UPDATE_ENTITY,
                        variables=variables
                        )

        if response:
            return response['data']['updateEntity']
        else:
            return None

    def delete(self, entity_id: str, hard_delete: bool = True):
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

        if response:
            return response['data']['deleteEntity']
        else:
            return None

    def upsert_raw_data(self):
        return

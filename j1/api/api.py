from .api_client import ApiClient
from typing import Dict, List


from j1.api.queries import(
    QUERY_V1
)
from j1.constants import (
    J1QL_SKIP_COUNT,
    J1QL_LIMIT_COUNT
)
    
class Api(ApiClient):
    def __init__(self, config, call_back=None):
        super(Api, self).__init__(config)
  
    def query_v1(self,
                query: str,
                skip: int,
                limit: int,
                include_deleted: bool
                ):
        """ Performs a V1 graph query
            args:
                query (str): Query text
                skip (int):  Skip entity count
                limit (int): Limit entity count
                include_deleted (bool): Include recently deleted entities in query/search
        """

        results: List = []
        page: int = 0

        while True:
            variables = {
                'query': f"{query} SKIP {page * skip} LIMIT {limit}",
                'includeDeleted': include_deleted
            }
            response = self._execute_query(
                self.config.get_query_endpont(),
                query=QUERY_V1,
                variables=variables
            )

            data = response['data']['queryV1']['data']

            # If tree query then no pagination
            if 'vertices' in data and 'edges' in data:
                return data

            if len(data) < J1QL_SKIP_COUNT:
                results.extend(data)
                break

            results.extend(data)
            page += 1

        return {'data': results}

    def bulk_upload(self):
        return

    def bulk_delete(self):
        return

import json
import pytest
import responses

from j1.client import J1Client

@responses.activate
def test_tree_query_v1():

    def request_callback(request):
        headers = {
            'Content-Type': 'application/json'
        }

        response = {
            'data': {
                'createEntity': {
                    'entity': {
                        '_id': '1'
                    },
                    'vertex': {
                        'id': '1',
                        'entity': {
                            '_id': '1'
                        }
                    }
                }
            }
        }
        return (200, headers, json.dumps(response))
    
    responses.add_callback(
        responses.POST, 'https://api.us.jupiterone.io/graphql',
        callback=request_callback,
        content_type='application/json',
    )

    j1_client = J1Client(
        account='j1dev',
        access_token='123token'
    )
    response = j1_client.entity().create(
        entity_key='host1',
        entity_type='test_host',
        entity_class='Host',
    )

    assert type(response) == dict
    assert type(response['vertex']) == dict
    assert response['entity']['_id'] == '1'

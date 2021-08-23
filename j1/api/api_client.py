
import requests
import json
from typing import Dict, List
from retrying import retry

from j1.exceptions.exceptions import (
    J1ApiRetryError,
    J1ApiError
)

def retry_on_429(exc):
    """ Used to trigger retry on rate limit """
    return isinstance(exc, J1ApiRetryError)

class ApiClient(object):

    RETRY_OPTS = {
        'wait_exponential_multiplier': 1000,
        'wait_exponential_max': 10000,
        'stop_max_delay': 300000,
        'retry_on_exception': retry_on_429
    }

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        global_headers (dict): The global headers of the API which are sent with
            every request.

    """

    def global_headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.config.access_token),
            'LifeOmic-Account': self.config.account
        }

    def __init__(self, config, call_back=None):
        self._config = config

    @property
    def config(self):
        return self._config

    def validate_parameters(self, **kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError("Required parameter {} cannot be None.".format(name))

    @retry(**RETRY_OPTS)
    def execute_query(self, url: str, query: str, variables: Dict = None) -> Dict:
        """ Executes query against graphql endpoint """
        data = {
            'query': query
        }
        if variables:
            data.update(variables=variables)

        print(data)

        response = requests.post(url, headers=self.global_headers(), json=data)
        print(response._content)
        # It is still unclear if all responses will have a status
        # code of 200 or if 429 will eventually be used to 
        # indicate rate limitting.  J1 devs are aware.
        if response.status_code == 200:
            if response._content:
                content = json.loads(response._content)
                if 'errors' in content:
                    errors = content['errors']
                    if len(errors) == 1:
                        if '429' in errors[0]['message']:
                            raise J1ApiRetryError('JupiterOne API rate limit exceeded')
                    raise J1ApiError(content.get('errors'))
                return response.json()

        elif response.status_code in [429, 500]:
            raise J1ApiRetryError('JupiterOne API rate limit exceeded')

        else:
            content = json.loads(response._content)
            raise J1ApiError('{}:{}'.format(response.status_code, content.get('error')))


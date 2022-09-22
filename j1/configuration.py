# -*- coding: utf-8 -*-
from j1.exceptions.exceptions import J1ClientError

class Configuration(object):
    """A class used for configuring the SDK by a user.
    """

    @property
    def account(self):
        """ Your JupiterOne account ID """
        if not self._account:
            raise J1ClientError('Account is required')
        return self._account

    @property
    def environment(self):
        return self._environment

    @property
    def access_token(self):
        """ Your JupiteOne access token """
        if not self._access_token:
            raise J1ClientError('Token is required')
        return self._access_token

    def __init__(
        self,
        account=None,
        environment='prod',
        access_token=None
    ):
        # The J1 Account associated with this request
        self._account = account

        # Current API environment
        self._environment = environment

        # The OAuth 2.0 Access Token to use for API requests.
        self._access_token = access_token


    # All the environments the SDK can run in
    environments = {
        'prod': {
            'default': 'https://api.us.jupiterone.io'
        },
        'dev': {
            'default': 'https://api.dev.jupiterone.io'
        }
    }

    def _get_base_uri(self):
        """Generates the appropriate base URI for the environment and the
        server.
        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.
        Returns:
            String: The base URI.
        """

        return self.environments[self.environment]

    def get_query_endpont(self):
        return str(self.environments[self.environment]['default']) + '/graphql'

    def get_rules_endpoint(self):
        return str(self._get_base_uri) + '/rules/graphql'

from j1.configuration import Configuration
from j1.api.entity import Entity
from j1.api.relationship import Relationship
from j1.decorators import lazy_property

class J1Client(object):
    @lazy_property
    def entity(self):
        return Entity(self.config)

    @lazy_property
    def relationship(self):
        return Relationship(self.config)

    def __init__(self,
                 environment='prod',
                 account=None,
                 access_token=None,
                 config=None):
        if config is None:
            self.config = Configuration(account=account,
                                        environment=environment,
                                        access_token=access_token)
        else:
            self.config = config

    

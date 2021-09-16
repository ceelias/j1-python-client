from .api_client import ApiClient
from typing import Dict, List

from .queries import (
    CREATE_ALERT_RULE,
    UPDATE_ALERT_RULE
)
    
class Alert(ApiClient):
    def __init__(self, config):
        super(Alert, self).__init__(config)
  
    def create(self):
        return

    
    def update(self):
        return
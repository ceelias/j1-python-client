from .api_client import ApiClient
from typing import Dict, List

from .queries import (
    CREATE_QUESTION,
    UPDATE_QUESTION,
    DELETE_QUESTION
)
    
class Question(ApiClient):
    def __init__(self, config):
        super(Question, self).__init__(config)
  
    def create(self):
        return

    
    def update(self):
        return

    def delete(self):
        return
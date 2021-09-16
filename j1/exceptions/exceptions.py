
class J1ClientError(Exception):
    """ Raised when error creating client """    

class J1ApiRetryError(Exception):
    """ Used to trigger retry on rate limit """

class J1ApiError(Exception):
    """ Raised when API returns error response """
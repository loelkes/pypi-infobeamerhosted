class Error(Exception):
    """Base class for other exceptions"""
    pass

class MissingAPIKeyError(Error):
    """Raised when there is no API Key available"""
    pass

class APIError(Error):
    pass

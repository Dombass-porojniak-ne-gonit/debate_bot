class DebateBotException(Exception):
    """Base debate bot exception"""

    pass


class UserNotFoundException(DebateBotException):
    """Raised when user is not found"""

    pass


# NOTE: Add unique exception for errors (with comments)

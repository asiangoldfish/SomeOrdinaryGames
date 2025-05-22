from enum import StrEnum

class ErrorType(StrEnum):
    STATUS="Status"
    WARNING="Warning"
    FATAL="Fatal"
        

class Error:
    def __init__(self, message="", type=ErrorType.STATUS):
        self.message = f"{type}: {message}"
        self.type = type

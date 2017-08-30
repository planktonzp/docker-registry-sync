class regsyncError(Exception):
    pass


class regsyncValueError(ValueError):
    pass


class regsyncTypeError(TypeError):
    pass


class regsyncTimeoutError(TypeError):
    pass


class regsyncNotExitsError(TypeError):
    pass


class regsyncReturnContextManager(Exception):
    pass

__all__ = ("regsyncError", "regsyncValueError", "regsyncTypeError",
           "regsyncTimeoutError", "regsyncNotExitsError",
           "regsyncReturnContextManager")

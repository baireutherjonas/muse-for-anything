"""
This type stub file was generated by pyright.
"""

import werkzeug.exceptions as wexc

"""Custom exceptions"""
class FlaskSmorestError(Exception):
    """Generic flask-smorest exception"""
    ...


class MissingAPIParameterError(FlaskSmorestError):
    """Missing API parameter"""
    ...


class CheckEtagNotCalledError(FlaskSmorestError):
    """ETag enabled on resource but check_etag not called"""
    ...


class NotModified(wexc.HTTPException, FlaskSmorestError):
    """Resource was not modified (Etag is unchanged)

    Exception created to compensate for a lack in Werkzeug (and Flask)
    """
    code = ...
    description = ...


class PreconditionRequired(wexc.PreconditionRequired, FlaskSmorestError):
    """Etag required but missing"""
    description = ...


class PreconditionFailed(wexc.PreconditionFailed, FlaskSmorestError):
    """Etag required and wrong ETag provided"""
    ...


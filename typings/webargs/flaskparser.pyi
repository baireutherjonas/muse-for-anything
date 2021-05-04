"""
This type stub file was generated by pyright.
"""

from typing import NoReturn
from webargs import core

"""Flask request argument parsing module.

Example: ::

    from flask import Flask

    from webargs import fields
    from webargs.flaskparser import use_args

    app = Flask(__name__)

    user_detail_args = {
        'per_page': fields.Int()
    }

    @app.route("/user/<int:uid>")
    @use_args(user_detail_args)
    def user_detail(args, uid):
        return ("The user page for user {uid}, showing {per_page} posts.").format(
            uid=uid, per_page=args["per_page"]
        )
"""

def abort(http_status_code, exc=..., **kwargs) -> NoReturn:
    """Raise a HTTPException for the given http_status_code. Attach any keyword
    arguments to the exception for later processing.

    From Flask-Restful. See NOTICE file for license information.
    """
    ...

def is_json_request(req): ...

class FlaskParser(core.Parser):
    """Flask request argument parser."""

    __location_map__ = ...
    def load_view_args(self, req, schema):
        """Return the request's ``view_args`` or ``missing`` if there are none."""
        ...
    def load_querystring(self, req, schema):
        """Return query params from the request as a MultiDictProxy."""
        ...
    def load_form(self, req, schema):
        """Return form values from the request as a MultiDictProxy."""
        ...
    def load_headers(self, req, schema):
        """Return headers from the request as a MultiDictProxy."""
        ...
    def load_cookies(self, req, schema):
        """Return cookies from the request."""
        ...
    def load_files(self, req, schema):
        """Return files from the request as a MultiDictProxy."""
        ...
    def handle_error(self, error, req, schema, *, error_status_code, error_headers):
        """Handles errors during parsing. Aborts the current HTTP request and
        responds with a 422 error.
        """
        ...
    def get_default_request(self):
        """Override to use Flask's thread-local request object by default"""
        ...

parser = ...
use_args = ...
use_kwargs = ...
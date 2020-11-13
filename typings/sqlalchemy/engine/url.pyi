"""
This type stub file was generated by pyright.
"""

"""Provides the :class:`~sqlalchemy.engine.url.URL` class which encapsulates
information about a database connection specification.

The URL object is created automatically when
:func:`~sqlalchemy.engine.create_engine` is called with a string
argument; alternatively, the URL is a public-facing construct which can
be used directly and is also accepted directly by ``create_engine()``.
"""
class URL(object):
    """
    Represent the components of a URL used to connect to a database.

    This object is suitable to be passed directly to a
    :func:`~sqlalchemy.create_engine` call.  The fields of the URL are parsed
    from a string by the :func:`.make_url` function.  The string
    format of the URL is an RFC-1738-style string.

    All initialization parameters are available as public attributes.

    :param drivername: the name of the database backend.
      This name will correspond to a module in sqlalchemy/databases
      or a third party plug-in.

    :param username: The user name.

    :param password: database password.

    :param host: The name of the host.

    :param port: The port number.

    :param database: The database name.

    :param query: A dictionary of options to be passed to the
      dialect and/or the DBAPI upon connect.

    """
    def __init__(self, drivername, username=..., password=..., host=..., port=..., database=..., query=...) -> None:
        ...
    
    def __to_string__(self, hide_password=...):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    @property
    def password(self):
        ...
    
    @password.setter
    def password(self, password):
        ...
    
    def get_backend_name(self):
        ...
    
    def get_driver_name(self):
        ...
    
    def get_dialect(self):
        """Return the SQLAlchemy database dialect class corresponding
        to this URL's driver name.
        """
        ...
    
    def translate_connect_args(self, names=..., **kw):
        r"""Translate url attributes into a dictionary of connection arguments.

        Returns attributes of this url (`host`, `database`, `username`,
        `password`, `port`) as a plain dictionary.  The attribute names are
        used as the keys by default.  Unset or false attributes are omitted
        from the final dictionary.

        :param \**kw: Optional, alternate key names for url attributes.

        :param names: Deprecated.  Same purpose as the keyword-based alternate
            names, but correlates the name to the original positionally.
        """
        ...
    


def make_url(name_or_url):
    """Given a string or unicode instance, produce a new URL instance.

    The given string is parsed according to the RFC 1738 spec.  If an
    existing URL object is passed, just returns the object.
    """
    ...

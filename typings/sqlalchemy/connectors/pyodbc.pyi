"""
This type stub file was generated by pyright.
"""

from . import Connector

class PyODBCConnector(Connector):
    driver = ...
    supports_sane_rowcount_returning = ...
    supports_sane_multi_rowcount = ...
    supports_unicode_statements = ...
    supports_unicode_binds = ...
    supports_native_decimal = ...
    default_paramstyle = ...
    pyodbc_driver_name = ...
    def __init__(self, supports_unicode_binds=..., **kw) -> None:
        ...
    
    @classmethod
    def dbapi(cls):
        ...
    
    def create_connect_args(self, url):
        ...
    
    def is_disconnect(self, e, connection, cursor):
        ...
    
    def set_isolation_level(self, connection, level):
        ...
    



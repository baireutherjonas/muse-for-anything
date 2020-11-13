"""
This type stub file was generated by pyright.
"""

from .base import MySQLDialect, MySQLExecutionContext
from .types import TIME
from ...connectors.pyodbc import PyODBCConnector

r"""


.. dialect:: mysql+pyodbc
    :name: PyODBC
    :dbapi: pyodbc
    :connectstring: mysql+pyodbc://<username>:<password>@<dsnname>
    :url: http://pypi.python.org/pypi/pyodbc/

    .. note:: The PyODBC for MySQL dialect is not well supported, and
       is subject to unresolved character encoding issues
       which exist within the current ODBC drivers available.
       (see http://code.google.com/p/pyodbc/issues/detail?id=25).
       Other dialects for MySQL are recommended.

Pass through exact pyodbc connection string::

    import urllib
    connection_string = (
        'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
        'SERVER=localhost;'
        'PORT=3307;'
        'DATABASE=mydb;'
        'UID=root;'
        'PWD=(whatever);'
        'charset=utf8mb4;'
    )
    params = urllib.parse.quote_plus(connection_string)
    connection_uri = "mysql+pyodbc:///?odbc_connect=%s" % params

"""
class _pyodbcTIME(TIME):
    def result_processor(self, dialect, coltype):
        ...
    


class MySQLExecutionContext_pyodbc(MySQLExecutionContext):
    def get_lastrowid(self):
        ...
    


class MySQLDialect_pyodbc(PyODBCConnector, MySQLDialect):
    colspecs = ...
    supports_unicode_statements = ...
    execution_ctx_cls = ...
    pyodbc_driver_name = ...
    def __init__(self, **kw) -> None:
        ...
    


dialect = MySQLDialect_pyodbc
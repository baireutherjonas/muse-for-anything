"""
This type stub file was generated by pyright.
"""

from .base import PGDialect, PGExecutionContext
from ...connectors.zxJDBC import ZxJDBCConnector

"""
.. dialect:: postgresql+zxjdbc
    :name: zxJDBC for Jython
    :dbapi: zxjdbc
    :connectstring: postgresql+zxjdbc://scott:tiger@localhost/db
    :driverurl: http://jdbc.postgresql.org/


"""
class PGExecutionContext_zxjdbc(PGExecutionContext):
    def create_cursor(self):
        ...
    


class PGDialect_zxjdbc(ZxJDBCConnector, PGDialect):
    jdbc_db_name = ...
    jdbc_driver_name = ...
    execution_ctx_cls = ...
    supports_native_decimal = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


dialect = PGDialect_zxjdbc
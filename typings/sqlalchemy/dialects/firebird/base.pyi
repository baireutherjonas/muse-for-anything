"""
This type stub file was generated by pyright.
"""

from sqlalchemy import sql, types as sqltypes
from sqlalchemy.engine import default, reflection
from sqlalchemy.sql import compiler
from sqlalchemy.types import BIGINT, BLOB, DATE, FLOAT, INTEGER, SMALLINT, TEXT, TIME, TIMESTAMP

r"""

.. dialect:: firebird
    :name: Firebird

.. note::

    The Firebird dialect within SQLAlchemy **is not currently supported**.
    It is not tested within continuous integration and is likely to have
    many issues and caveats not currently handled. Consider using the
    `external dialect <https://github.com/pauldex/sqlalchemy-firebird>`_
    instead.

Firebird Dialects
-----------------

Firebird offers two distinct dialects_ (not to be confused with a
SQLAlchemy ``Dialect``):

dialect 1
  This is the old syntax and behaviour, inherited from Interbase pre-6.0.

dialect 3
  This is the newer and supported syntax, introduced in Interbase 6.0.

The SQLAlchemy Firebird dialect detects these versions and
adjusts its representation of SQL accordingly.  However,
support for dialect 1 is not well tested and probably has
incompatibilities.

Locking Behavior
----------------

Firebird locks tables aggressively.  For this reason, a DROP TABLE may
hang until other transactions are released.  SQLAlchemy does its best
to release transactions as quickly as possible.  The most common cause
of hanging transactions is a non-fully consumed result set, i.e.::

    result = engine.execute("select * from table")
    row = result.fetchone()
    return

Where above, the ``ResultProxy`` has not been fully consumed.  The
connection will be returned to the pool and the transactional state
rolled back once the Python garbage collector reclaims the objects
which hold onto the connection, which often occurs asynchronously.
The above use case can be alleviated by calling ``first()`` on the
``ResultProxy`` which will fetch the first row and immediately close
all remaining cursor/connection resources.

RETURNING support
-----------------

Firebird 2.0 supports returning a result set from inserts, and 2.1
extends that to deletes and updates. This is generically exposed by
the SQLAlchemy ``returning()`` method, such as::

    # INSERT..RETURNING
    result = table.insert().returning(table.c.col1, table.c.col2).\
                   values(name='foo')
    print(result.fetchall())

    # UPDATE..RETURNING
    raises = empl.update().returning(empl.c.id, empl.c.salary).\
                  where(empl.c.sales>100).\
                  values(dict(salary=empl.c.salary * 1.1))
    print(raises.fetchall())


.. _dialects: http://mc-computing.com/Databases/Firebird/SQL_Dialect.html
"""
RESERVED_WORDS = set(["active", "add", "admin", "after", "all", "alter", "and", "any", "as", "asc", "ascending", "at", "auto", "avg", "before", "begin", "between", "bigint", "bit_length", "blob", "both", "by", "case", "cast", "char", "character", "character_length", "char_length", "check", "close", "collate", "column", "commit", "committed", "computed", "conditional", "connect", "constraint", "containing", "count", "create", "cross", "cstring", "current", "current_connection", "current_date", "current_role", "current_time", "current_timestamp", "current_transaction", "current_user", "cursor", "database", "date", "day", "dec", "decimal", "declare", "default", "delete", "desc", "descending", "disconnect", "distinct", "do", "domain", "double", "drop", "else", "end", "entry_point", "escape", "exception", "execute", "exists", "exit", "external", "extract", "fetch", "file", "filter", "float", "for", "foreign", "from", "full", "function", "gdscode", "generator", "gen_id", "global", "grant", "group", "having", "hour", "if", "in", "inactive", "index", "inner", "input_type", "insensitive", "insert", "int", "integer", "into", "is", "isolation", "join", "key", "leading", "left", "length", "level", "like", "long", "lower", "manual", "max", "maximum_segment", "merge", "min", "minute", "module_name", "month", "names", "national", "natural", "nchar", "no", "not", "null", "numeric", "octet_length", "of", "on", "only", "open", "option", "or", "order", "outer", "output_type", "overflow", "page", "pages", "page_size", "parameter", "password", "plan", "position", "post_event", "precision", "primary", "privileges", "procedure", "protected", "rdb$db_key", "read", "real", "record_version", "recreate", "recursive", "references", "release", "reserv", "reserving", "retain", "returning_values", "returns", "revoke", "right", "rollback", "rows", "row_count", "savepoint", "schema", "second", "segment", "select", "sensitive", "set", "shadow", "shared", "singular", "size", "smallint", "snapshot", "some", "sort", "sqlcode", "stability", "start", "starting", "starts", "statistics", "sub_type", "sum", "suspend", "table", "then", "time", "timestamp", "to", "trailing", "transaction", "trigger", "trim", "uncommitted", "union", "unique", "update", "upper", "user", "using", "value", "values", "varchar", "variable", "varying", "view", "wait", "when", "where", "while", "with", "work", "write", "year"])
class _StringType(sqltypes.String):
    """Base for Firebird string types."""
    def __init__(self, charset=..., **kw) -> None:
        ...
    


class VARCHAR(_StringType, sqltypes.VARCHAR):
    """Firebird VARCHAR type"""
    __visit_name__ = ...
    def __init__(self, length=..., **kwargs) -> None:
        ...
    


class CHAR(_StringType, sqltypes.CHAR):
    """Firebird CHAR type"""
    __visit_name__ = ...
    def __init__(self, length=..., **kwargs) -> None:
        ...
    


class _FBDateTime(sqltypes.DateTime):
    def bind_processor(self, dialect):
        ...
    


colspecs = { sqltypes.DateTime: _FBDateTime }
ischema_names = { "SHORT": SMALLINT,"LONG": INTEGER,"QUAD": FLOAT,"FLOAT": FLOAT,"DATE": DATE,"TIME": TIME,"TEXT": TEXT,"INT64": BIGINT,"DOUBLE": FLOAT,"TIMESTAMP": TIMESTAMP,"VARYING": VARCHAR,"CSTRING": CHAR,"BLOB": BLOB }
class FBTypeCompiler(compiler.GenericTypeCompiler):
    def visit_boolean(self, type_, **kw):
        ...
    
    def visit_datetime(self, type_, **kw):
        ...
    
    def visit_TEXT(self, type_, **kw):
        ...
    
    def visit_BLOB(self, type_, **kw):
        ...
    
    def visit_CHAR(self, type_, **kw):
        ...
    
    def visit_VARCHAR(self, type_, **kw):
        ...
    


class FBCompiler(sql.compiler.SQLCompiler):
    """Firebird specific idiosyncrasies"""
    ansi_bind_rules = ...
    def visit_now_func(self, fn, **kw):
        ...
    
    def visit_startswith_op_binary(self, binary, operator, **kw):
        ...
    
    def visit_notstartswith_op_binary(self, binary, operator, **kw):
        ...
    
    def visit_mod_binary(self, binary, operator, **kw):
        ...
    
    def visit_alias(self, alias, asfrom=..., **kwargs):
        ...
    
    def visit_substring_func(self, func, **kw):
        ...
    
    def visit_length_func(self, function, **kw):
        ...
    
    visit_char_length_func = ...
    def function_argspec(self, func, **kw):
        ...
    
    def default_from(self):
        ...
    
    def visit_sequence(self, seq, **kw):
        ...
    
    def get_select_precolumns(self, select, **kw):
        """Called when building a ``SELECT`` statement, position is just
        before column list Firebird puts the limit and offset right
        after the ``SELECT``...
        """
        ...
    
    def limit_clause(self, select, **kw):
        """Already taken care of in the `get_select_precolumns` method."""
        ...
    
    def returning_clause(self, stmt, returning_cols):
        ...
    


class FBDDLCompiler(sql.compiler.DDLCompiler):
    """Firebird syntactic idiosyncrasies"""
    def visit_create_sequence(self, create):
        """Generate a ``CREATE GENERATOR`` statement for the sequence."""
        ...
    
    def visit_drop_sequence(self, drop):
        """Generate a ``DROP GENERATOR`` statement for the sequence."""
        ...
    
    def visit_computed_column(self, generated):
        ...
    


class FBIdentifierPreparer(sql.compiler.IdentifierPreparer):
    """Install Firebird specific reserved words."""
    reserved_words = ...
    illegal_initial_characters = ...
    def __init__(self, dialect) -> None:
        ...
    


class FBExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_):
        """Get the next value from the sequence using ``gen_id()``."""
        ...
    


class FBDialect(default.DefaultDialect):
    """Firebird dialect"""
    name = ...
    max_identifier_length = ...
    supports_sequences = ...
    sequences_optional = ...
    supports_default_values = ...
    postfetch_lastrowid = ...
    supports_native_boolean = ...
    requires_name_normalize = ...
    supports_empty_insert = ...
    statement_compiler = ...
    ddl_compiler = ...
    preparer = ...
    type_compiler = ...
    execution_ctx_cls = ...
    colspecs = ...
    ischema_names = ...
    construct_arguments = ...
    _version_two = ...
    def initialize(self, connection):
        ...
    
    def has_table(self, connection, table_name, schema=...):
        """Return ``True`` if the given table exists, ignoring
        the `schema`."""
        ...
    
    def has_sequence(self, connection, sequence_name, schema=...):
        """Return ``True`` if the given sequence (generator) exists."""
        ...
    
    @reflection.cache
    def get_table_names(self, connection, schema=..., **kw):
        ...
    
    @reflection.cache
    def get_view_names(self, connection, schema=..., **kw):
        ...
    
    @reflection.cache
    def get_view_definition(self, connection, view_name, schema=..., **kw):
        ...
    
    @reflection.cache
    def get_pk_constraint(self, connection, table_name, schema=..., **kw):
        ...
    
    @reflection.cache
    def get_column_sequence(self, connection, table_name, column_name, schema=..., **kw):
        ...
    
    @reflection.cache
    def get_columns(self, connection, table_name, schema=..., **kw):
        ...
    
    @reflection.cache
    def get_foreign_keys(self, connection, table_name, schema=..., **kw):
        ...
    
    @reflection.cache
    def get_indexes(self, connection, table_name, schema=..., **kw):
        ...
    



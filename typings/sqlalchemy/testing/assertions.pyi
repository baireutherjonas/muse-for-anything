"""
This type stub file was generated by pyright.
"""

import contextlib

def expect_warnings(*messages, **kw):
    """Context manager which expects one or more warnings.

    With no arguments, squelches all SAWarnings emitted via
    sqlalchemy.util.warn and sqlalchemy.util.warn_limited.   Otherwise
    pass string expressions that will match selected warnings via regex;
    all non-matching warnings are sent through.

    The expect version **asserts** that the warnings were in fact seen.

    Note that the test suite sets SAWarning warnings to raise exceptions.

    """
    ...

@contextlib.contextmanager
def expect_warnings_on(db, *messages, **kw):
    """Context manager which expects one or more warnings on specific
    dialects.

    The expect version **asserts** that the warnings were in fact seen.

    """
    ...

def emits_warning(*messages):
    """Decorator form of expect_warnings().

    Note that emits_warning does **not** assert that the warnings
    were in fact seen.

    """
    ...

def expect_deprecated(*messages, **kw):
    ...

def emits_warning_on(db, *messages):
    """Mark a test as emitting a warning on a specific dialect.

    With no arguments, squelches all SAWarning failures.  Or pass one or more
    strings; these will be matched to the root of the warning description by
    warnings.filterwarnings().

    Note that emits_warning_on does **not** assert that the warnings
    were in fact seen.

    """
    ...

def uses_deprecated(*messages):
    """Mark a test as immune from fatal deprecation warnings.

    With no arguments, squelches all SADeprecationWarning failures.
    Or pass one or more strings; these will be matched to the root
    of the warning description by warnings.filterwarnings().

    As a special case, you may pass a function name prefixed with //
    and it will be re-written as needed to match the standard warning
    verbiage emitted by the sqlalchemy.util.deprecated decorator.

    Note that uses_deprecated does **not** assert that the warnings
    were in fact seen.

    """
    ...

def global_cleanup_assertions():
    """Check things that have to be finalized at the end of a test suite.

    Hardcoded at the moment, a modular system can be built here
    to support things like PG prepared transactions, tables all
    dropped, etc.

    """
    ...

_STRAY_CONNECTION_FAILURES = 0
def eq_regex(a, b, msg=...):
    ...

def eq_(a, b, msg=...):
    """Assert a == b, with repr messaging on failure."""
    ...

def ne_(a, b, msg=...):
    """Assert a != b, with repr messaging on failure."""
    ...

def le_(a, b, msg=...):
    """Assert a <= b, with repr messaging on failure."""
    ...

def is_instance_of(a, b, msg=...):
    ...

def is_true(a, msg=...):
    ...

def is_false(a, msg=...):
    ...

def is_(a, b, msg=...):
    """Assert a is b, with repr messaging on failure."""
    ...

def is_not(a, b, msg=...):
    """Assert a is not b, with repr messaging on failure."""
    ...

is_not_ = is_not
def in_(a, b, msg=...):
    """Assert a in b, with repr messaging on failure."""
    ...

def not_in(a, b, msg=...):
    """Assert a in not b, with repr messaging on failure."""
    ...

not_in_ = not_in
def startswith_(a, fragment, msg=...):
    """Assert a.startswith(fragment), with repr messaging on failure."""
    ...

def eq_ignore_whitespace(a, b, msg=...):
    ...

def assert_raises(except_cls, callable_, *args, **kw):
    ...

def assert_raises_context_ok(except_cls, callable_, *args, **kw):
    ...

def assert_raises_return(except_cls, callable_, *args, **kw):
    ...

def assert_raises_message(except_cls, msg, callable_, *args, **kwargs):
    ...

def assert_raises_message_context_ok(except_cls, msg, callable_, *args, **kwargs):
    ...

class AssertsCompiledSQL(object):
    def assert_compile(self, clause, result, params=..., checkparams=..., dialect=..., checkpositional=..., check_prefetch=..., use_default_dialect=..., allow_dialect_select=..., literal_binds=..., schema_translate_map=...):
        ...
    


class ComparesTables(object):
    def assert_tables_equal(self, table, reflected_table, strict_types=...):
        ...
    
    def assert_types_base(self, c1, c2):
        ...
    


class AssertsExecutionResults(object):
    def assert_result(self, result, class_, *objects):
        ...
    
    def assert_list(self, result, class_, list_):
        ...
    
    def assert_row(self, class_, rowobj, desc):
        ...
    
    def assert_unordered_result(self, result, cls, *expected):
        """As assert_result, but the order of objects is not considered.

        The algorithm is very expensive but not a big deal for the small
        numbers of rows that the test suite manipulates.
        """
        class immutabledict(dict):
            ...
        
        
    
    def sql_execution_asserter(self, db=...):
        ...
    
    def assert_sql_execution(self, db, callable_, *rules):
        ...
    
    def assert_sql(self, db, callable_, rules):
        ...
    
    def assert_sql_count(self, db, callable_, count):
        ...
    
    def assert_multiple_sql_count(self, dbs, callable_, counts):
        ...
    
    @contextlib.contextmanager
    def assert_execution(self, db, *rules):
        ...
    
    def assert_statement_count(self, db, count):
        ...
    


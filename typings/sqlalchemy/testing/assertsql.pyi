"""
This type stub file was generated by pyright.
"""

import collections
import contextlib

class AssertRule(object):
    is_consumed = ...
    errormessage = ...
    consume_statement = ...
    def process_statement(self, execute_observed):
        ...
    
    def no_more_statements(self):
        ...
    


class SQLMatchRule(AssertRule):
    ...


class CursorSQL(SQLMatchRule):
    consume_statement = ...
    def __init__(self, statement, params=...) -> None:
        ...
    
    def process_statement(self, execute_observed):
        ...
    


class CompiledSQL(SQLMatchRule):
    def __init__(self, statement, params=..., dialect=...) -> None:
        ...
    
    def process_statement(self, execute_observed):
        ...
    


class RegexSQL(CompiledSQL):
    def __init__(self, regex, params=..., dialect=...) -> None:
        ...
    


class DialectSQL(CompiledSQL):
    ...


class CountStatements(AssertRule):
    def __init__(self, count) -> None:
        ...
    
    def process_statement(self, execute_observed):
        ...
    
    def no_more_statements(self):
        ...
    


class AllOf(AssertRule):
    def __init__(self, *rules) -> None:
        ...
    
    def process_statement(self, execute_observed):
        ...
    


class EachOf(AssertRule):
    def __init__(self, *rules) -> None:
        ...
    
    def process_statement(self, execute_observed):
        ...
    
    def no_more_statements(self):
        ...
    


class Or(AllOf):
    def process_statement(self, execute_observed):
        ...
    


class SQLExecuteObserved(object):
    def __init__(self, context, clauseelement, multiparams, params) -> None:
        ...
    


class SQLCursorExecuteObserved(collections.namedtuple("SQLCursorExecuteObserved", ["statement", "parameters", "context", "executemany"])):
    ...


class SQLAsserter(object):
    def __init__(self) -> None:
        ...
    
    def assert_(self, *rules):
        ...
    


@contextlib.contextmanager
def assert_engine(engine):
    ...


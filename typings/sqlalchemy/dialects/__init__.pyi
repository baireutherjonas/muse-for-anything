"""
This type stub file was generated by pyright.
"""

from .. import util

_translates = { "postgres": "postgresql" }
registry = util.PluginLoader("sqlalchemy.dialects", auto_fn=_auto_fn)
plugins = util.PluginLoader("sqlalchemy.plugins")
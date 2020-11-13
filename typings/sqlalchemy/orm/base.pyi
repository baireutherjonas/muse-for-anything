"""
This type stub file was generated by pyright.
"""

import operator
from typing import Any, Callable
from .. import util

"""Constants and rudimental functions used throughout the ORM.

"""
PASSIVE_NO_RESULT = util.symbol(
    "PASSIVE_NO_RESULT",
    """Symbol returned by a loader callable or other attribute/history
    retrieval operation when a value could not be determined, based
    on loader callable flags.
    """,
)
PASSIVE_CLASS_MISMATCH = util.symbol(
    "PASSIVE_CLASS_MISMATCH",
    """Symbol indicating that an object is locally present for a given
    primary key identity but it is not of the requested class.  The
    return value is therefore None and no SQL should be emitted.""",
)
ATTR_WAS_SET = util.symbol(
    "ATTR_WAS_SET",
    """Symbol returned by a loader callable to indicate the
    retrieved value, or values, were assigned to their attributes
    on the target object.
    """,
)
ATTR_EMPTY = util.symbol(
    "ATTR_EMPTY", """Symbol used internally to indicate an attribute had no callable."""
)
NO_VALUE = util.symbol(
    "NO_VALUE",
    """Symbol which may be placed as the 'previous' value of an attribute,
    indicating no value was loaded for an attribute when it was modified,
    and flags indicated we were not to load it.
    """,
)
NEVER_SET = util.symbol(
    "NEVER_SET",
    """Symbol which may be placed as the 'previous' value of an attribute
    indicating that the attribute had not been assigned to previously.
    """,
)
NO_CHANGE = util.symbol(
    "NO_CHANGE",
    """No callables or SQL should be emitted on attribute access
    and no state should change
    """,
    canonical=0,
)
CALLABLES_OK = util.symbol(
    "CALLABLES_OK",
    """Loader callables can be fired off if a value
    is not present.
    """,
    canonical=1,
)
SQL_OK = util.symbol(
    "SQL_OK",
    """Loader callables can emit SQL at least on scalar value attributes.""",
    canonical=2,
)
RELATED_OBJECT_OK = util.symbol(
    "RELATED_OBJECT_OK",
    """Callables can use SQL to load related objects as well
    as scalar value attributes.
    """,
    canonical=4,
)
INIT_OK = util.symbol(
    "INIT_OK",
    """Attributes should be initialized with a blank
    value (None or an empty collection) upon get, if no other
    value can be obtained.
    """,
    canonical=8,
)
NON_PERSISTENT_OK = util.symbol(
    "NON_PERSISTENT_OK",
    """Callables can be emitted if the parent is not persistent.""",
    canonical=16,
)
LOAD_AGAINST_COMMITTED = util.symbol(
    "LOAD_AGAINST_COMMITTED",
    """Callables should use committed values as primary/foreign keys during a
    load.
    """,
    canonical=32,
)
NO_AUTOFLUSH = util.symbol(
    "NO_AUTOFLUSH", """Loader callables should disable autoflush.""", canonical=64
)
NO_RAISE = util.symbol(
    "NO_RAISE", """Loader callables should not raise any assertions""", canonical=128
)
PASSIVE_OFF = util.symbol(
    "PASSIVE_OFF",
    "Callables can be emitted in all cases.",
    canonical=RELATED_OBJECT_OK | NON_PERSISTENT_OK | INIT_OK | CALLABLES_OK | SQL_OK,
)
PASSIVE_RETURN_NEVER_SET = util.symbol(
    "PASSIVE_RETURN_NEVER_SET",
    """PASSIVE_OFF ^ INIT_OK""",
    canonical=PASSIVE_OFF ^ INIT_OK,
)
PASSIVE_NO_INITIALIZE = util.symbol(
    "PASSIVE_NO_INITIALIZE",
    "PASSIVE_RETURN_NEVER_SET ^ CALLABLES_OK",
    canonical=PASSIVE_RETURN_NEVER_SET ^ CALLABLES_OK,
)
PASSIVE_NO_FETCH = util.symbol(
    "PASSIVE_NO_FETCH", "PASSIVE_OFF ^ SQL_OK", canonical=PASSIVE_OFF ^ SQL_OK
)
PASSIVE_NO_FETCH_RELATED = util.symbol(
    "PASSIVE_NO_FETCH_RELATED",
    "PASSIVE_OFF ^ RELATED_OBJECT_OK",
    canonical=PASSIVE_OFF ^ RELATED_OBJECT_OK,
)
PASSIVE_ONLY_PERSISTENT = util.symbol(
    "PASSIVE_ONLY_PERSISTENT",
    "PASSIVE_OFF ^ NON_PERSISTENT_OK",
    canonical=PASSIVE_OFF ^ NON_PERSISTENT_OK,
)
DEFAULT_MANAGER_ATTR = "_sa_class_manager"
DEFAULT_STATE_ATTR = "_sa_instance_state"
_INSTRUMENTOR = ("mapper", "instrumentor")
EXT_CONTINUE = util.symbol("EXT_CONTINUE")
EXT_STOP = util.symbol("EXT_STOP")
EXT_SKIP = util.symbol("EXT_SKIP")
ONETOMANY = util.symbol(
    "ONETOMANY",
    """Indicates the one-to-many direction for a :func:`_orm.relationship`.

    This symbol is typically used by the internals but may be exposed within
    certain API features.

    """,
)
MANYTOONE = util.symbol(
    "MANYTOONE",
    """Indicates the many-to-one direction for a :func:`_orm.relationship`.

    This symbol is typically used by the internals but may be exposed within
    certain API features.

    """,
)
MANYTOMANY = util.symbol(
    "MANYTOMANY",
    """Indicates the many-to-many direction for a :func:`_orm.relationship`.

    This symbol is typically used by the internals but may be exposed within
    certain API features.

    """,
)
NOT_EXTENSION = util.symbol(
    "NOT_EXTENSION",
    """Symbol indicating an :class:`InspectionAttr` that's
    not part of sqlalchemy.ext.

    Is assigned to the :attr:`.InspectionAttr.extension_type`
    attribute.

    """,
)
_never_set = frozenset([NEVER_SET])
_none_set = frozenset([None, NEVER_SET, PASSIVE_NO_RESULT])
_SET_DEFERRED_EXPIRED = util.symbol("SET_DEFERRED_EXPIRED")
_DEFER_FOR_STATE = util.symbol("DEFER_FOR_STATE")


def _generative(
    *assertions: Callable[..., Any]
) -> Callable[..., Callable[..., Any]]:
    """Mark a method as generative, e.g. method-chained."""
    ...


def manager_of_class(cls):
    ...


instance_state = operator.attrgetter(DEFAULT_STATE_ATTR)
instance_dict = operator.attrgetter("__dict__")


def instance_str(instance):
    """Return a string describing an instance."""
    ...


def state_str(state):
    """Return a string describing an instance via its InstanceState."""
    ...


def state_class_str(state):
    """Return a string describing an instance's class via its
    InstanceState.
    """
    ...


def attribute_str(instance, attribute):
    ...


def state_attribute_str(state, attribute):
    ...


def object_mapper(instance):
    """Given an object, return the primary Mapper associated with the object
    instance.

    Raises :class:`sqlalchemy.orm.exc.UnmappedInstanceError`
    if no mapping is configured.

    This function is available via the inspection system as::

        inspect(instance).mapper

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the instance is
    not part of a mapping.

    """
    ...


def object_state(instance):
    """Given an object, return the :class:`.InstanceState`
    associated with the object.

    Raises :class:`sqlalchemy.orm.exc.UnmappedInstanceError`
    if no mapping is configured.

    Equivalent functionality is available via the :func:`_sa.inspect`
    function as::

        inspect(instance)

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the instance is
    not part of a mapping.

    """
    ...


_state_mapper = util.dottedgetter("manager.mapper")


def class_mapper(class_, configure=...):
    """Given a class, return the primary :class:`_orm.Mapper` associated
    with the key.

    Raises :exc:`.UnmappedClassError` if no mapping is configured
    on the given class, or :exc:`.ArgumentError` if a non-class
    object is passed.

    Equivalent functionality is available via the :func:`_sa.inspect`
    function as::

        inspect(some_mapped_class)

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the class is not mapped.

    """
    ...


class InspectionAttr(object):
    """A base class applied to all ORM objects that can be returned
    by the :func:`_sa.inspect` function.

    The attributes defined here allow the usage of simple boolean
    checks to test basic facts about the object returned.

    While the boolean checks here are basically the same as using
    the Python isinstance() function, the flags here can be used without
    the need to import all of these classes, and also such that
    the SQLAlchemy class system can change while leaving the flags
    here intact for forwards-compatibility.

    """

    __slots__ = ...
    is_selectable = ...
    is_aliased_class = ...
    is_instance = ...
    is_mapper = ...
    is_property = ...
    is_attribute = ...
    _is_internal_proxy = ...
    is_clause_element = ...
    extension_type = ...


class InspectionAttrInfo(InspectionAttr):
    """Adds the ``.info`` attribute to :class:`.InspectionAttr`.

    The rationale for :class:`.InspectionAttr` vs. :class:`.InspectionAttrInfo`
    is that the former is compatible as a mixin for classes that specify
    ``__slots__``; this is essentially an implementation artifact.

    """

    @util.memoized_property
    def info(self):
        """Info dictionary associated with the object, allowing user-defined
        data to be associated with this :class:`.InspectionAttr`.

        The dictionary is generated when first accessed.  Alternatively,
        it can be specified as a constructor argument to the
        :func:`.column_property`, :func:`_orm.relationship`, or
        :func:`.composite`
        functions.

        .. versionchanged:: 1.0.0 :attr:`.MapperProperty.info` is also
           available on extension types via the
           :attr:`.InspectionAttrInfo.info` attribute, so that it can apply
           to a wider variety of ORM and extension constructs.

        .. seealso::

            :attr:`.QueryableAttribute.info`

            :attr:`.SchemaItem.info`

        """
        ...


class _MappedAttribute(object):
    """Mixin for attributes which should be replaced by mapper-assigned
    attributes.

    """

    __slots__ = ...
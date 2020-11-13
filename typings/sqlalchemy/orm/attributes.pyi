"""
This type stub file was generated by pyright.
"""

from . import interfaces
from .base import NEVER_SET, NO_VALUE, PASSIVE_NO_RESULT
from .. import inspection, util

"""Defines instrumentation for class attributes and their interaction
with instances.

This module is usually not directly visible to user applications, but
defines a large part of the ORM's interactivity.


"""
@inspection._self_inspects
class QueryableAttribute(interfaces._MappedAttribute, interfaces.InspectionAttr, interfaces.PropComparator):
    """Base class for :term:`descriptor` objects that intercept
    attribute events on behalf of a :class:`.MapperProperty`
    object.  The actual :class:`.MapperProperty` is accessible
    via the :attr:`.QueryableAttribute.property`
    attribute.


    .. seealso::

        :class:`.InstrumentedAttribute`

        :class:`.MapperProperty`

        :attr:`_orm.Mapper.all_orm_descriptors`

        :attr:`_orm.Mapper.attrs`
    """
    is_attribute = ...
    def __init__(self, class_, key, impl=..., comparator=..., parententity=..., of_type=...) -> None:
        ...
    
    def get_history(self, instance, passive=...):
        ...
    
    def __selectable__(self):
        ...
    
    @util.memoized_property
    def info(self):
        """Return the 'info' dictionary for the underlying SQL element.

        The behavior here is as follows:

        * If the attribute is a column-mapped property, i.e.
          :class:`.ColumnProperty`, which is mapped directly
          to a schema-level :class:`_schema.Column` object, this attribute
          will return the :attr:`.SchemaItem.info` dictionary associated
          with the core-level :class:`_schema.Column` object.

        * If the attribute is a :class:`.ColumnProperty` but is mapped to
          any other kind of SQL expression other than a
          :class:`_schema.Column`,
          the attribute will refer to the :attr:`.MapperProperty.info`
          dictionary associated directly with the :class:`.ColumnProperty`,
          assuming the SQL expression itself does not have its own ``.info``
          attribute (which should be the case, unless a user-defined SQL
          construct has defined one).

        * If the attribute refers to any other kind of
          :class:`.MapperProperty`, including :class:`.RelationshipProperty`,
          the attribute will refer to the :attr:`.MapperProperty.info`
          dictionary associated with that :class:`.MapperProperty`.

        * To access the :attr:`.MapperProperty.info` dictionary of the
          :class:`.MapperProperty` unconditionally, including for a
          :class:`.ColumnProperty` that's associated directly with a
          :class:`_schema.Column`, the attribute can be referred to using
          :attr:`.QueryableAttribute.property` attribute, as
          ``MyClass.someattribute.property.info``.

        .. seealso::

            :attr:`.SchemaItem.info`

            :attr:`.MapperProperty.info`

        """
        ...
    
    @util.memoized_property
    def parent(self):
        """Return an inspection instance representing the parent.

        This will be either an instance of :class:`_orm.Mapper`
        or :class:`.AliasedInsp`, depending upon the nature
        of the parent entity which this attribute is associated
        with.

        """
        ...
    
    @property
    def expression(self):
        ...
    
    def __clause_element__(self):
        ...
    
    def adapt_to_entity(self, adapt_to_entity):
        ...
    
    def of_type(self, cls):
        ...
    
    def label(self, name):
        ...
    
    def operate(self, op, *other, **kwargs):
        ...
    
    def reverse_operate(self, op, other, **kwargs):
        ...
    
    def hasparent(self, state, optimistic=...):
        ...
    
    def __getattr__(self, key):
        ...
    
    def __str__(self) -> str:
        ...
    
    @util.memoized_property
    def property(self):
        """Return the :class:`.MapperProperty` associated with this
        :class:`.QueryableAttribute`.


        Return values here will commonly be instances of
        :class:`.ColumnProperty` or :class:`.RelationshipProperty`.


        """
        ...
    


class InstrumentedAttribute(QueryableAttribute):
    """Class bound instrumented attribute which adds basic
    :term:`descriptor` methods.

    See :class:`.QueryableAttribute` for a description of most features.


    """
    def __set__(self, instance, value):
        ...
    
    def __delete__(self, instance):
        ...
    
    def __get__(self, instance, owner):
        ...
    


def create_proxied_attribute(descriptor):
    """Create an QueryableAttribute / user descriptor hybrid.

    Returns a new QueryableAttribute type that delegates descriptor
    behavior and getattr() to the given descriptor.
    """
    class Proxy(QueryableAttribute):
        """Presents the :class:`.QueryableAttribute` interface as a
        proxy on top of a Python descriptor / :class:`.PropComparator`
        combination.

        """
        ...
    
    

OP_REMOVE = util.symbol("REMOVE")
OP_APPEND = util.symbol("APPEND")
OP_REPLACE = util.symbol("REPLACE")
OP_BULK_REPLACE = util.symbol("BULK_REPLACE")
OP_MODIFIED = util.symbol("MODIFIED")
class Event(object):
    """A token propagated throughout the course of a chain of attribute
    events.

    Serves as an indicator of the source of the event and also provides
    a means of controlling propagation across a chain of attribute
    operations.

    The :class:`.Event` object is sent as the ``initiator`` argument
    when dealing with events such as :meth:`.AttributeEvents.append`,
    :meth:`.AttributeEvents.set`,
    and :meth:`.AttributeEvents.remove`.

    The :class:`.Event` object is currently interpreted by the backref
    event handlers, and is used to control the propagation of operations
    across two mutually-dependent attributes.

    .. versionadded:: 0.9.0

    :attribute impl: The :class:`.AttributeImpl` which is the current event
     initiator.

    :attribute op: The symbol :attr:`.OP_APPEND`, :attr:`.OP_REMOVE`,
     :attr:`.OP_REPLACE`, or :attr:`.OP_BULK_REPLACE`, indicating the
     source operation.

    """
    __slots__ = ...
    def __init__(self, attribute_impl, op) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    @property
    def key(self):
        ...
    
    def hasparent(self, state):
        ...
    


class AttributeImpl(object):
    """internal implementation for instrumented attributes."""
    def __init__(self, class_, key, callable_, dispatch, trackparent=..., extension=..., compare_function=..., active_history=..., parent_token=..., expire_missing=..., send_modified_events=..., accepts_scalar_loader=..., **kwargs) -> None:
        r"""Construct an AttributeImpl.

        :param \class_: associated class

        :param key: string name of the attribute

        :param \callable_:
          optional function which generates a callable based on a parent
          instance, which produces the "default" values for a scalar or
          collection attribute when it's first accessed, if not present
          already.

        :param trackparent:
          if True, attempt to track if an instance has a parent attached
          to it via this attribute.

        :param extension:
          a single or list of AttributeExtension object(s) which will
          receive set/delete/append/remove/etc. events.
          The event package is now used.

          .. deprecated::  1.3

            The :paramref:`.AttributeImpl.extension` parameter is deprecated
            and will be removed in a future release, corresponding to the
            "extension" parameter on the :class:`.MapperProprty` classes
            like :func:`.column_property` and :func:`_orm.relationship`  The
            events system is now used.

        :param compare_function:
          a function that compares two values which are normally
          assignable to this attribute.

        :param active_history:
          indicates that get_history() should always return the "old" value,
          even if it means executing a lazy callable upon attribute change.

        :param parent_token:
          Usually references the MapperProperty, used as a key for
          the hasparent() function to identify an "owning" attribute.
          Allows multiple AttributeImpls to all match a single
          owner attribute.

        :param expire_missing:
          if False, don't add an "expiry" callable to this attribute
          during state.expire_attributes(None), if no value is present
          for this key.

        :param send_modified_events:
          if False, the InstanceState._modified_event method will have no
          effect; this means the attribute will never show up as changed in a
          history entry.

        """
        ...
    
    __slots__ = ...
    def __str__(self) -> str:
        ...
    
    active_history = ...
    def hasparent(self, state, optimistic=...):
        """Return the boolean value of a `hasparent` flag attached to
        the given state.

        The `optimistic` flag determines what the default return value
        should be if no `hasparent` flag can be located.

        As this function is used to determine if an instance is an
        *orphan*, instances that were loaded from storage should be
        assumed to not be orphans, until a True/False value for this
        flag is set.

        An instance attribute that is loaded by a callable function
        will also not have a `hasparent` flag.

        """
        ...
    
    def sethasparent(self, state, parent_state, value):
        """Set a boolean flag on the given item corresponding to
        whether or not it is attached to a parent object via the
        attribute represented by this ``InstrumentedAttribute``.

        """
        ...
    
    def get_history(self, state, dict_, passive=...):
        ...
    
    def get_all_pending(self, state, dict_, passive=...):
        """Return a list of tuples of (state, obj)
        for all objects in this attribute's current state
        + history.

        Only applies to object-based attributes.

        This is an inlining of existing functionality
        which roughly corresponds to:

            get_state_history(
                        state,
                        key,
                        passive=PASSIVE_NO_INITIALIZE).sum()

        """
        ...
    
    def initialize(self, state, dict_):
        """Initialize the given state's attribute with an empty value."""
        ...
    
    def get(self, state, dict_, passive=...):
        """Retrieve a value from the given object.
        If a callable is assembled on this object's attribute, and
        passive is False, the callable will be executed and the
        resulting value will be set as the new value for this attribute.
        """
        ...
    
    def append(self, state, dict_, value, initiator, passive=...):
        ...
    
    def remove(self, state, dict_, value, initiator, passive=...):
        ...
    
    def pop(self, state, dict_, value, initiator, passive=...):
        ...
    
    def set(self, state, dict_, value, initiator, passive=..., check_old=..., pop=...):
        ...
    
    def get_committed_value(self, state, dict_, passive=...):
        """return the unchanged value of this attribute"""
        ...
    
    def set_committed_value(self, state, dict_, value):
        """set an attribute value on the given instance and 'commit' it."""
        ...
    


class ScalarAttributeImpl(AttributeImpl):
    """represents a scalar value-holding InstrumentedAttribute."""
    default_accepts_scalar_loader = ...
    uses_objects = ...
    supports_population = ...
    collection = ...
    dynamic = ...
    __slots__ = ...
    def __init__(self, *arg, **kw) -> None:
        ...
    
    def delete(self, state, dict_):
        ...
    
    def get_history(self, state, dict_, passive=...):
        ...
    
    def set(self, state, dict_, value, initiator, passive=..., check_old=..., pop=...):
        ...
    
    def fire_replace_event(self, state, dict_, value, previous, initiator):
        ...
    
    def fire_remove_event(self, state, dict_, value, initiator):
        ...
    
    @property
    def type(self):
        ...
    


class ScalarObjectAttributeImpl(ScalarAttributeImpl):
    """represents a scalar-holding InstrumentedAttribute,
    where the target object is also instrumented.

    Adds events to delete/set operations.

    """
    default_accepts_scalar_loader = ...
    uses_objects = ...
    supports_population = ...
    collection = ...
    __slots__ = ...
    def delete(self, state, dict_):
        ...
    
    def get_history(self, state, dict_, passive=...):
        ...
    
    def get_all_pending(self, state, dict_, passive=...):
        ...
    
    def set(self, state, dict_, value, initiator, passive=..., check_old=..., pop=...):
        """Set a value on the given InstanceState."""
        ...
    
    def fire_remove_event(self, state, dict_, value, initiator):
        ...
    
    def fire_replace_event(self, state, dict_, value, previous, initiator):
        ...
    


class CollectionAttributeImpl(AttributeImpl):
    """A collection-holding attribute that instruments changes in membership.

    Only handles collections of instrumented objects.

    InstrumentedCollectionAttribute holds an arbitrary, user-specified
    container object (defaulting to a list) and brokers access to the
    CollectionAdapter, a "view" onto that object that presents consistent bag
    semantics to the orm layer independent of the user data implementation.

    """
    default_accepts_scalar_loader = ...
    uses_objects = ...
    supports_population = ...
    collection = ...
    dynamic = ...
    __slots__ = ...
    def __init__(self, class_, key, callable_, dispatch, typecallable=..., trackparent=..., extension=..., copy_function=..., compare_function=..., **kwargs) -> None:
        ...
    
    def get_history(self, state, dict_, passive=...):
        ...
    
    def get_all_pending(self, state, dict_, passive=...):
        ...
    
    def fire_append_event(self, state, dict_, value, initiator):
        ...
    
    def fire_pre_remove_event(self, state, dict_, initiator):
        """A special event used for pop() operations.

        The "remove" event needs to have the item to be removed passed to
        it, which in the case of pop from a set, we don't have a way to access
        the item before the operation.   the event is used for all pop()
        operations (even though set.pop is the one where it is really needed).

        """
        ...
    
    def fire_remove_event(self, state, dict_, value, initiator):
        ...
    
    def delete(self, state, dict_):
        ...
    
    def initialize(self, state, dict_):
        """Initialize this attribute with an empty collection."""
        ...
    
    def append(self, state, dict_, value, initiator, passive=...):
        ...
    
    def remove(self, state, dict_, value, initiator, passive=...):
        ...
    
    def pop(self, state, dict_, value, initiator, passive=...):
        ...
    
    def set(self, state, dict_, value, initiator=..., passive=..., pop=..., _adapt=...):
        ...
    
    def set_committed_value(self, state, dict_, value):
        """Set an attribute value on the given instance and 'commit' it."""
        ...
    
    def get_collection(self, state, dict_, user_data=..., passive=...):
        """Retrieve the CollectionAdapter associated with the given state.

        Creates a new CollectionAdapter if one does not exist.

        """
        ...
    


def backref_listeners(attribute, key, uselist):
    """Apply listeners to synchronize a two-way relationship."""
    ...

_NO_HISTORY = util.symbol("NO_HISTORY")
_NO_STATE_SYMBOLS = frozenset([id(PASSIVE_NO_RESULT), id(NO_VALUE), id(NEVER_SET)])
History = util.namedtuple("History", ["added", "unchanged", "deleted"])
class History(History):
    """A 3-tuple of added, unchanged and deleted values,
    representing the changes which have occurred on an instrumented
    attribute.

    The easiest way to get a :class:`.History` object for a particular
    attribute on an object is to use the :func:`_sa.inspect` function::

        from sqlalchemy import inspect

        hist = inspect(myobject).attrs.myattribute.history

    Each tuple member is an iterable sequence:

    * ``added`` - the collection of items added to the attribute (the first
      tuple element).

    * ``unchanged`` - the collection of items that have not changed on the
      attribute (the second tuple element).

    * ``deleted`` - the collection of items that have been removed from the
      attribute (the third tuple element).

    """
    def __bool__(self):
        ...
    
    __nonzero__ = ...
    def empty(self):
        """Return True if this :class:`.History` has no changes
        and no existing, unchanged state.

        """
        ...
    
    def sum(self):
        """Return a collection of added + unchanged + deleted."""
        ...
    
    def non_deleted(self):
        """Return a collection of added + unchanged."""
        ...
    
    def non_added(self):
        """Return a collection of unchanged + deleted."""
        ...
    
    def has_changes(self):
        """Return True if this :class:`.History` has changes."""
        ...
    
    def as_state(self):
        ...
    
    @classmethod
    def from_scalar_attribute(cls, attribute, state, current):
        ...
    
    @classmethod
    def from_object_attribute(cls, attribute, state, current):
        ...
    
    @classmethod
    def from_collection(cls, attribute, state, current):
        ...
    


HISTORY_BLANK = History(None, None, None)
def get_history(obj, key, passive=...):
    """Return a :class:`.History` record for the given object
    and attribute key.

    This is the **pre-flush** history for a given attribute, which is
    reset each time the :class:`.Session` flushes changes to the
    current database transaction.

    .. note::

        Prefer to use the :attr:`.AttributeState.history` and
        :meth:`.AttributeState.load_history` accessors to retrieve the
        :class:`.History` for instance attributes.


    :param obj: an object whose class is instrumented by the
      attributes package.

    :param key: string attribute name.

    :param passive: indicates loading behavior for the attribute
       if the value is not already present.   This is a
       bitflag attribute, which defaults to the symbol
       :attr:`.PASSIVE_OFF` indicating all necessary SQL
       should be emitted.

    .. seealso::

        :attr:`.AttributeState.history`

        :meth:`.AttributeState.load_history` - retrieve history
        using loader callables if the value is not locally present.

    """
    ...

def get_state_history(state, key, passive=...):
    ...

def has_parent(cls, obj, key, optimistic=...):
    """TODO"""
    ...

def register_attribute(class_, key, **kw):
    ...

def register_attribute_impl(class_, key, uselist=..., callable_=..., useobject=..., impl_class=..., backref=..., **kw):
    ...

def register_descriptor(class_, key, comparator=..., parententity=..., doc=...):
    ...

def unregister_attribute(class_, key):
    ...

def init_collection(obj, key):
    """Initialize a collection attribute and return the collection adapter.

    This function is used to provide direct access to collection internals
    for a previously unloaded attribute.  e.g.::

        collection_adapter = init_collection(someobject, 'elements')
        for elem in values:
            collection_adapter.append_without_event(elem)

    For an easier way to do the above, see
    :func:`~sqlalchemy.orm.attributes.set_committed_value`.

    :param obj: a mapped object

    :param key: string attribute name where the collection is located.

    """
    ...

def init_state_collection(state, dict_, key):
    """Initialize a collection attribute and return the collection adapter."""
    ...

def set_committed_value(instance, key, value):
    """Set the value of an attribute with no history events.

    Cancels any previous history present.  The value should be
    a scalar value for scalar-holding attributes, or
    an iterable for any collection-holding attribute.

    This is the same underlying method used when a lazy loader
    fires off and loads additional data from the database.
    In particular, this method can be used by application code
    which has loaded additional attributes or collections through
    separate queries, which can then be attached to an instance
    as though it were part of its original loaded state.

    """
    ...

def set_attribute(instance, key, value, initiator=...):
    """Set the value of an attribute, firing history events.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.
    Custom attribute management schemes will need to make usage
    of this method to establish attribute state as understood
    by SQLAlchemy.

    :param instance: the object that will be modified

    :param key: string name of the attribute

    :param value: value to assign

    :param initiator: an instance of :class:`.Event` that would have
     been propagated from a previous event listener.  This argument
     is used when the :func:`.set_attribute` function is being used within
     an existing event listening function where an :class:`.Event` object
     is being supplied; the object may be used to track the origin of the
     chain of events.

     .. versionadded:: 1.2.3

    """
    ...

def get_attribute(instance, key):
    """Get the value of an attribute, firing any callables required.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.
    Custom attribute management schemes will need to make usage
    of this method to make usage of attribute state as understood
    by SQLAlchemy.

    """
    ...

def del_attribute(instance, key):
    """Delete the value of an attribute, firing history events.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.
    Custom attribute management schemes will need to make usage
    of this method to establish attribute state as understood
    by SQLAlchemy.

    """
    ...

def flag_modified(instance, key):
    """Mark an attribute on an instance as 'modified'.

    This sets the 'modified' flag on the instance and
    establishes an unconditional change event for the given attribute.
    The attribute must have a value present, else an
    :class:`.InvalidRequestError` is raised.

    To mark an object "dirty" without referring to any specific attribute
    so that it is considered within a flush, use the
    :func:`.attributes.flag_dirty` call.

    .. seealso::

        :func:`.attributes.flag_dirty`

    """
    ...

def flag_dirty(instance):
    """Mark an instance as 'dirty' without any specific attribute mentioned.

    This is a special operation that will allow the object to travel through
    the flush process for interception by events such as
    :meth:`.SessionEvents.before_flush`.   Note that no SQL will be emitted in
    the flush process for an object that has no changes, even if marked dirty
    via this method.  However, a :meth:`.SessionEvents.before_flush` handler
    will be able to see the object in the :attr:`.Session.dirty` collection and
    may establish changes on it, which will then be included in the SQL
    emitted.

    .. versionadded:: 1.2

    .. seealso::

        :func:`.attributes.flag_modified`

    """
    ...

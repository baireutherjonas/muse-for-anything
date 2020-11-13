"""
This type stub file was generated by pyright.
"""

import operator
from .compat import py2k

"""Collection classes and helpers."""
EMPTY_SET = frozenset()
class AbstractKeyedTuple(tuple):
    __slots__ = ...
    def keys(self):
        """Return a list of string key names for this :class:`.KeyedTuple`.

        .. seealso::

            :attr:`.KeyedTuple._fields`

        """
        ...
    


class KeyedTuple(AbstractKeyedTuple):
    """``tuple`` subclass that adds labeled names.

    E.g.::

        >>> k = KeyedTuple([1, 2, 3], labels=["one", "two", "three"])
        >>> k.one
        1
        >>> k.two
        2

    Result rows returned by :class:`_query.Query` that contain multiple
    ORM entities and/or column expressions make use of this
    class to return rows.

    The :class:`.KeyedTuple` exhibits similar behavior to the
    ``collections.namedtuple()`` construct provided in the Python
    standard library, however is architected very differently.
    Unlike ``collections.namedtuple()``, :class:`.KeyedTuple` is
    does not rely on creation of custom subtypes in order to represent
    a new series of keys, instead each :class:`.KeyedTuple` instance
    receives its list of keys in place.   The subtype approach
    of ``collections.namedtuple()`` introduces significant complexity
    and performance overhead, which is not necessary for the
    :class:`_query.Query` object's use case.

    .. seealso::

        :ref:`ormtutorial_querying`

    """
    def __new__(cls, vals, labels=...):
        ...
    
    def __setattr__(self, key, value):
        ...
    


class _LW(AbstractKeyedTuple):
    __slots__ = ...
    def __new__(cls, vals):
        ...
    
    def __reduce__(self):
        ...
    


class ImmutableContainer(object):
    __delitem__ = ...


class immutabledict(ImmutableContainer, dict):
    clear = ...
    def __new__(cls, *args):
        ...
    
    def __init__(self, *args) -> None:
        ...
    
    def __reduce__(self):
        ...
    
    def union(self, d):
        ...
    
    def __repr__(self):
        ...
    


class Properties(object):
    """Provide a __getattr__/__setattr__ interface over a dict."""
    __slots__ = ...
    def __init__(self, data) -> None:
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self):
        ...
    
    def __dir__(self):
        ...
    
    def __add__(self, other):
        ...
    
    def __setitem__(self, key, obj):
        ...
    
    def __getitem__(self, key):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __setattr__(self, key, obj):
        ...
    
    def __getstate__(self):
        ...
    
    def __setstate__(self, state):
        ...
    
    def __getattr__(self, key):
        ...
    
    def __contains__(self, key):
        ...
    
    def as_immutable(self):
        """Return an immutable proxy for this :class:`.Properties`."""
        ...
    
    def update(self, value):
        ...
    
    def get(self, key, default=...):
        ...
    
    def keys(self):
        ...
    
    def values(self):
        ...
    
    def items(self):
        ...
    
    def has_key(self, key):
        ...
    
    def clear(self):
        ...
    


class OrderedProperties(Properties):
    """Provide a __getattr__/__setattr__ interface with an OrderedDict
    as backing store."""
    __slots__ = ...
    def __init__(self) -> None:
        ...
    


class ImmutableProperties(ImmutableContainer, Properties):
    """Provide immutable dict/object attribute to an underlying dictionary."""
    __slots__ = ...


class OrderedDict(dict):
    """A dict that returns keys/values/items in the order they were added."""
    __slots__ = ...
    def __reduce__(self):
        ...
    
    def __init__(self, ____sequence=..., **kwargs) -> None:
        ...
    
    def clear(self):
        ...
    
    def copy(self):
        ...
    
    def __copy__(self):
        ...
    
    def sort(self, *arg, **kw):
        ...
    
    def update(self, ____sequence=..., **kwargs):
        ...
    
    def setdefault(self, key, value):
        ...
    
    def __iter__(self):
        ...
    
    def keys(self):
        ...
    
    def values(self):
        ...
    
    def items(self):
        ...
    
    if py2k:
        def itervalues(self):
            ...
        
        def iterkeys(self):
            ...
        
        def iteritems(self):
            ...
        
    def __setitem__(self, key, obj):
        ...
    
    def __delitem__(self, key):
        ...
    
    def pop(self, key, *default):
        ...
    
    def popitem(self):
        ...
    


class OrderedSet(set):
    def __init__(self, d=...) -> None:
        ...
    
    def add(self, element):
        ...
    
    def remove(self, element):
        ...
    
    def insert(self, pos, element):
        ...
    
    def discard(self, element):
        ...
    
    def clear(self):
        ...
    
    def __getitem__(self, key):
        ...
    
    def __iter__(self):
        ...
    
    def __add__(self, other):
        ...
    
    def __repr__(self):
        ...
    
    __str__ = ...
    def update(self, iterable):
        ...
    
    __ior__ = ...
    def union(self, other):
        ...
    
    __or__ = ...
    def intersection(self, other):
        ...
    
    __and__ = ...
    def symmetric_difference(self, other):
        ...
    
    __xor__ = ...
    def difference(self, other):
        ...
    
    __sub__ = ...
    def intersection_update(self, other):
        ...
    
    __iand__ = ...
    def symmetric_difference_update(self, other):
        ...
    
    __ixor__ = ...
    def difference_update(self, other):
        ...
    
    __isub__ = ...


class IdentitySet(object):
    """A set that considers only object id() for uniqueness.

    This strategy has edge cases for builtin types- it's possible to have
    two 'foo' strings in one of these sets, for example.  Use sparingly.

    """
    def __init__(self, iterable=...) -> None:
        ...
    
    def add(self, value):
        ...
    
    def __contains__(self, value):
        ...
    
    def remove(self, value):
        ...
    
    def discard(self, value):
        ...
    
    def pop(self):
        ...
    
    def clear(self):
        ...
    
    def __cmp__(self, other):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def issubset(self, iterable):
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def issuperset(self, iterable):
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def union(self, iterable):
        ...
    
    def __or__(self, other):
        ...
    
    def update(self, iterable):
        ...
    
    def __ior__(self, other):
        ...
    
    def difference(self, iterable):
        ...
    
    def __sub__(self, other):
        ...
    
    def difference_update(self, iterable):
        ...
    
    def __isub__(self, other):
        ...
    
    def intersection(self, iterable):
        ...
    
    def __and__(self, other):
        ...
    
    def intersection_update(self, iterable):
        ...
    
    def __iand__(self, other):
        ...
    
    def symmetric_difference(self, iterable):
        ...
    
    def __xor__(self, other):
        ...
    
    def symmetric_difference_update(self, iterable):
        ...
    
    def __ixor__(self, other):
        ...
    
    def copy(self):
        ...
    
    __copy__ = ...
    def __len__(self):
        ...
    
    def __iter__(self):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __repr__(self):
        ...
    


class WeakSequence(object):
    def __init__(self, __elements=...) -> None:
        ...
    
    def append(self, item):
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, index):
        ...
    


class OrderedIdentitySet(IdentitySet):
    def __init__(self, iterable=...) -> None:
        ...
    


class PopulateDict(dict):
    """A dict which populates missing values via a creation function.

    Note the creation function takes a key, unlike
    collections.defaultdict.

    """
    def __init__(self, creator) -> None:
        ...
    
    def __missing__(self, key):
        ...
    


class WeakPopulateDict(dict):
    """Like PopulateDict, but assumes a self + a method and does not create
    a reference cycle.

    """
    def __init__(self, creator_method) -> None:
        ...
    
    def __missing__(self, key):
        ...
    


column_set = set
column_dict = dict
ordered_column_set = OrderedSet
_getters = PopulateDict(operator.itemgetter)
_property_getters = PopulateDict(lambda idx: property(operator.itemgetter(idx)))
def unique_list(seq, hashfunc=...):
    ...

class UniqueAppender(object):
    """Appends items to a collection ensuring uniqueness.

    Additional appends() of the same object are ignored.  Membership is
    determined by identity (``is a``) not equality (``==``).
    """
    def __init__(self, data, via=...) -> None:
        ...
    
    def append(self, item):
        ...
    
    def __iter__(self):
        ...
    


def coerce_generator_arg(arg):
    ...

def to_list(x, default=...):
    ...

def has_intersection(set_, iterable):
    r"""return True if any items of set\_ are present in iterable.

    Goes through special effort to ensure __hash__ is not called
    on items in iterable that don't support it.

    """
    ...

def to_set(x):
    ...

def to_column_set(x):
    ...

def update_copy(d, _new=..., **kw):
    """Copy the given dict and update with the given values."""
    ...

def flatten_iterator(x):
    """Given an iterator of which further sub-elements may also be
    iterators, flatten the sub-elements into a single iterator.

    """
    ...

class LRUCache(dict):
    """Dictionary with 'squishy' removal of least
    recently used items.

    Note that either get() or [] should be used here, but
    generally its not safe to do an "in" check first as the dictionary
    can change subsequent to that call.

    """
    __slots__ = ...
    def __init__(self, capacity=..., threshold=..., size_alert=...) -> None:
        ...
    
    def get(self, key, default=...):
        ...
    
    def __getitem__(self, key):
        ...
    
    def values(self):
        ...
    
    def setdefault(self, key, value):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    @property
    def size_threshold(self):
        ...
    


_lw_tuples = LRUCache(100)
def lightweight_named_tuple(name, fields):
    ...

class ScopedRegistry(object):
    """A Registry that can store one or multiple instances of a single
    class on the basis of a "scope" function.

    The object implements ``__call__`` as the "getter", so by
    calling ``myregistry()`` the contained object is returned
    for the current scope.

    :param createfunc:
      a callable that returns a new object to be placed in the registry

    :param scopefunc:
      a callable that will return a key to store/retrieve an object.
    """
    def __init__(self, createfunc, scopefunc) -> None:
        """Construct a new :class:`.ScopedRegistry`.

        :param createfunc:  A creation function that will generate
          a new value for the current scope, if none is present.

        :param scopefunc:  A function that returns a hashable
          token representing the current scope (such as, current
          thread identifier).

        """
        ...
    
    def __call__(self):
        ...
    
    def has(self):
        """Return True if an object is present in the current scope."""
        ...
    
    def set(self, obj):
        """Set the value for the current scope."""
        ...
    
    def clear(self):
        """Clear the current scope, if any."""
        ...
    


class ThreadLocalRegistry(ScopedRegistry):
    """A :class:`.ScopedRegistry` that uses a ``threading.local()``
    variable for storage.

    """
    def __init__(self, createfunc) -> None:
        ...
    
    def __call__(self):
        ...
    
    def has(self):
        ...
    
    def set(self, obj):
        ...
    
    def clear(self):
        ...
    


def has_dupes(sequence, target):
    """Given a sequence and search object, return True if there's more
    than one, False if zero or one of them.


    """
    ...


"""
This type stub file was generated by pyright.
"""

from .. import log, util

"""Base constructs for connection pools.

"""
reset_rollback = util.symbol("reset_rollback")
reset_commit = util.symbol("reset_commit")
reset_none = util.symbol("reset_none")
class _ConnDialect(object):
    """partial implementation of :class:`.Dialect`
    which provides DBAPI connection methods.

    When a :class:`_pool.Pool` is combined with an :class:`_engine.Engine`,
    the :class:`_engine.Engine` replaces this with its own
    :class:`.Dialect`.

    """
    def do_rollback(self, dbapi_connection):
        ...
    
    def do_commit(self, dbapi_connection):
        ...
    
    def do_close(self, dbapi_connection):
        ...
    
    def do_ping(self, dbapi_connection):
        ...
    


class Pool(log.Identified):
    """Abstract base class for connection pools."""
    _dialect = ...
    @util.deprecated_params(use_threadlocal=("1.3", "The :paramref:`_pool.Pool.use_threadlocal` parameter is " "deprecated and will be removed in a future release."), listeners=("0.7", ":class:`.PoolListener` is deprecated in favor of the " ":class:`_events.PoolEvents` listener interface.  The " ":paramref:`_pool.Pool.listeners` parameter will be removed in a " "future release."))
    def __init__(self, creator, recycle=..., echo=..., use_threadlocal=..., logging_name=..., reset_on_return=..., listeners=..., events=..., dialect=..., pre_ping=..., _dispatch=...) -> None:
        """
        Construct a Pool.

        :param creator: a callable function that returns a DB-API
          connection object.  The function will be called with
          parameters.

        :param recycle: If set to a value other than -1, number of
          seconds between connection recycling, which means upon
          checkout, if this timeout is surpassed the connection will be
          closed and replaced with a newly opened connection. Defaults to -1.

        :param logging_name:  String identifier which will be used within
          the "name" field of logging records generated within the
          "sqlalchemy.pool" logger. Defaults to a hexstring of the object's
          id.

        :param echo: if True, the connection pool will log
         informational output such as when connections are invalidated
         as well as when connections are recycled to the default log handler,
         which defaults to ``sys.stdout`` for output..   If set to the string
         ``"debug"``, the logging will include pool checkouts and checkins.

         The :paramref:`_pool.Pool.echo` parameter can also be set from the
         :func:`_sa.create_engine` call by using the
         :paramref:`_sa.create_engine.echo_pool` parameter.

         .. seealso::

             :ref:`dbengine_logging` - further detail on how to configure
             logging.

        :param use_threadlocal: If set to True, repeated calls to
          :meth:`connect` within the same application thread will be
          guaranteed to return the same connection object that is already
          checked out.   This is a legacy use case and the flag has no
          effect when using the pool with a :class:`_engine.Engine` object.

        :param reset_on_return: Determine steps to take on
          connections as they are returned to the pool.
          reset_on_return can have any of these values:

          * ``"rollback"`` - call rollback() on the connection,
            to release locks and transaction resources.
            This is the default value.  The vast majority
            of use cases should leave this value set.
          * ``True`` - same as 'rollback', this is here for
            backwards compatibility.
          * ``"commit"`` - call commit() on the connection,
            to release locks and transaction resources.
            A commit here may be desirable for databases that
            cache query plans if a commit is emitted,
            such as Microsoft SQL Server.  However, this
            value is more dangerous than 'rollback' because
            any data changes present on the transaction
            are committed unconditionally.
          * ``None`` - don't do anything on the connection.
            This setting should generally only be made on a database
            that has no transaction support at all,
            namely MySQL MyISAM; when used on this backend, performance
            can be improved as the "rollback" call is still expensive on
            MySQL.   It is **strongly recommended** that this setting not be
            used for transaction-supporting databases in conjunction with
            a persistent pool such as :class:`.QueuePool`, as it opens
            the possibility for connections still in a transaction to be
            idle in the pool.   The setting may be appropriate in the
            case of :class:`.NullPool` or special circumstances where
            the connection pool in use is not being used to maintain connection
            lifecycle.

          * ``False`` - same as None, this is here for
            backwards compatibility.

        :param events: a list of 2-tuples, each of the form
         ``(callable, target)`` which will be passed to :func:`.event.listen`
         upon construction.   Provided here so that event listeners
         can be assigned via :func:`_sa.create_engine` before dialect-level
         listeners are applied.

        :param listeners: A list of :class:`.PoolListener`-like objects or
          dictionaries of callables that receive events when DB-API
          connections are created, checked out and checked in to the
          pool.

        :param dialect: a :class:`.Dialect` that will handle the job
         of calling rollback(), close(), or commit() on DBAPI connections.
         If omitted, a built-in "stub" dialect is used.   Applications that
         make use of :func:`_sa.create_engine` should not use this parameter
         as it is handled by the engine creation strategy.

         .. versionadded:: 1.1 - ``dialect`` is now a public parameter
            to the :class:`_pool.Pool`.

        :param pre_ping: if True, the pool will emit a "ping" (typically
         "SELECT 1", but is dialect-specific) on the connection
         upon checkout, to test if the connection is alive or not.   If not,
         the connection is transparently re-connected and upon success, all
         other pooled connections established prior to that timestamp are
         invalidated.     Requires that a dialect is passed as well to
         interpret the disconnection error.

         .. versionadded:: 1.2

        """
        ...
    
    @util.deprecated("0.7", "The :meth:`_pool.Pool.add_listener` method is deprecated and " "will be removed in a future release.  Please use the " ":class:`_events.PoolEvents` listener interface.")
    def add_listener(self, listener):
        """Add a :class:`.PoolListener`-like object to this pool.

        ``listener`` may be an object that implements some or all of
        PoolListener, or a dictionary of callables containing implementations
        of some or all of the named methods in PoolListener.

        """
        ...
    
    def unique_connection(self):
        """Produce a DBAPI connection that is not referenced by any
        thread-local context.

        This method is equivalent to :meth:`_pool.Pool.connect` when the
        :paramref:`_pool.Pool.use_threadlocal` flag is not set to True.
        When :paramref:`_pool.Pool.use_threadlocal` is True, the
        :meth:`_pool.Pool.unique_connection`
        method provides a means of bypassing
        the threadlocal context.

        """
        ...
    
    def recreate(self):
        """Return a new :class:`_pool.Pool`, of the same class as this one
        and configured with identical creation arguments.

        This method is used in conjunction with :meth:`dispose`
        to close out an entire :class:`_pool.Pool` and create a new one in
        its place.

        """
        ...
    
    def dispose(self):
        """Dispose of this pool.

        This method leaves the possibility of checked-out connections
        remaining open, as it only affects connections that are
        idle in the pool.

        .. seealso::

            :meth:`Pool.recreate`

        """
        ...
    
    def connect(self):
        """Return a DBAPI connection from the pool.

        The connection is instrumented such that when its
        ``close()`` method is called, the connection will be returned to
        the pool.

        """
        ...
    
    def status(self):
        ...
    


class _ConnectionRecord(object):
    """Internal object which maintains an individual DBAPI connection
    referenced by a :class:`_pool.Pool`.

    The :class:`._ConnectionRecord` object always exists for any particular
    DBAPI connection whether or not that DBAPI connection has been
    "checked out".  This is in contrast to the :class:`._ConnectionFairy`
    which is only a public facade to the DBAPI connection while it is checked
    out.

    A :class:`._ConnectionRecord` may exist for a span longer than that
    of a single DBAPI connection.  For example, if the
    :meth:`._ConnectionRecord.invalidate`
    method is called, the DBAPI connection associated with this
    :class:`._ConnectionRecord`
    will be discarded, but the :class:`._ConnectionRecord` may be used again,
    in which case a new DBAPI connection is produced when the
    :class:`_pool.Pool`
    next uses this record.

    The :class:`._ConnectionRecord` is delivered along with connection
    pool events, including :meth:`_events.PoolEvents.connect` and
    :meth:`_events.PoolEvents.checkout`, however :class:`._ConnectionRecord`
    still
    remains an internal object whose API and internals may change.

    .. seealso::

        :class:`._ConnectionFairy`

    """
    def __init__(self, pool, connect=...) -> None:
        ...
    
    fairy_ref = ...
    starttime = ...
    connection = ...
    _soft_invalidate_time = ...
    @util.memoized_property
    def info(self):
        """The ``.info`` dictionary associated with the DBAPI connection.

        This dictionary is shared among the :attr:`._ConnectionFairy.info`
        and :attr:`_engine.Connection.info` accessors.

        .. note::

            The lifespan of this dictionary is linked to the
            DBAPI connection itself, meaning that it is **discarded** each time
            the DBAPI connection is closed and/or invalidated.   The
            :attr:`._ConnectionRecord.record_info` dictionary remains
            persistent throughout the lifespan of the
            :class:`._ConnectionRecord` container.

        """
        ...
    
    @util.memoized_property
    def record_info(self):
        """An "info' dictionary associated with the connection record
        itself.

        Unlike the :attr:`._ConnectionRecord.info` dictionary, which is linked
        to the lifespan of the DBAPI connection, this dictionary is linked
        to the lifespan of the :class:`._ConnectionRecord` container itself
        and will remain persistent throughout the life of the
        :class:`._ConnectionRecord`.

        .. versionadded:: 1.1

        """
        ...
    
    @classmethod
    def checkout(cls, pool):
        ...
    
    def checkin(self, _no_fairy_ref=...):
        ...
    
    @property
    def in_use(self):
        ...
    
    @property
    def last_connect_time(self):
        ...
    
    def close(self):
        ...
    
    def invalidate(self, e=..., soft=...):
        """Invalidate the DBAPI connection held by this :class:`._ConnectionRecord`.

        This method is called for all connection invalidations, including
        when the :meth:`._ConnectionFairy.invalidate` or
        :meth:`_engine.Connection.invalidate` methods are called,
        as well as when any
        so-called "automatic invalidation" condition occurs.

        :param e: an exception object indicating a reason for the invalidation.

        :param soft: if True, the connection isn't closed; instead, this
         connection will be recycled on next checkout.

         .. versionadded:: 1.0.3

        .. seealso::

            :ref:`pool_connection_invalidation`

        """
        ...
    
    def get_connection(self):
        ...
    


_refs = set()
class _ConnectionFairy(object):
    """Proxies a DBAPI connection and provides return-on-dereference
    support.

    This is an internal object used by the :class:`_pool.Pool` implementation
    to provide context management to a DBAPI connection delivered by
    that :class:`_pool.Pool`.

    The name "fairy" is inspired by the fact that the
    :class:`._ConnectionFairy` object's lifespan is transitory, as it lasts
    only for the length of a specific DBAPI connection being checked out from
    the pool, and additionally that as a transparent proxy, it is mostly
    invisible.

    .. seealso::

        :class:`._ConnectionRecord`

    """
    def __init__(self, dbapi_connection, connection_record, echo) -> None:
        ...
    
    connection = ...
    _connection_record = ...
    _reset_agent = ...
    _close = ...
    @property
    def is_valid(self):
        """Return True if this :class:`._ConnectionFairy` still refers
        to an active DBAPI connection."""
        ...
    
    @util.memoized_property
    def info(self):
        """Info dictionary associated with the underlying DBAPI connection
        referred to by this :class:`.ConnectionFairy`, allowing user-defined
        data to be associated with the connection.

        The data here will follow along with the DBAPI connection including
        after it is returned to the connection pool and used again
        in subsequent instances of :class:`._ConnectionFairy`.  It is shared
        with the :attr:`._ConnectionRecord.info` and
        :attr:`_engine.Connection.info`
        accessors.

        The dictionary associated with a particular DBAPI connection is
        discarded when the connection itself is discarded.

        """
        ...
    
    @property
    def record_info(self):
        """Info dictionary associated with the :class:`._ConnectionRecord
        container referred to by this :class:`.ConnectionFairy`.

        Unlike the :attr:`._ConnectionFairy.info` dictionary, the lifespan
        of this dictionary is persistent across connections that are
        disconnected and/or invalidated within the lifespan of a
        :class:`._ConnectionRecord`.

        .. versionadded:: 1.1

        """
        ...
    
    def invalidate(self, e=..., soft=...):
        """Mark this connection as invalidated.

        This method can be called directly, and is also called as a result
        of the :meth:`_engine.Connection.invalidate` method.   When invoked,
        the DBAPI connection is immediately closed and discarded from
        further use by the pool.  The invalidation mechanism proceeds
        via the :meth:`._ConnectionRecord.invalidate` internal method.

        :param e: an exception object indicating a reason for the invalidation.

        :param soft: if True, the connection isn't closed; instead, this
         connection will be recycled on next checkout.

         .. versionadded:: 1.0.3

        .. seealso::

            :ref:`pool_connection_invalidation`

        """
        ...
    
    def cursor(self, *args, **kwargs):
        """Return a new DBAPI cursor for the underlying connection.

        This method is a proxy for the ``connection.cursor()`` DBAPI
        method.

        """
        ...
    
    def __getattr__(self, key):
        ...
    
    def detach(self):
        """Separate this connection from its Pool.

        This means that the connection will no longer be returned to the
        pool when closed, and will instead be literally closed.  The
        containing ConnectionRecord is separated from the DB-API connection,
        and will create a new connection when next used.

        Note that any overall connection limiting constraints imposed by a
        Pool implementation may be violated after a detach, as the detached
        connection is removed from the pool's knowledge and control.
        """
        ...
    
    def close(self):
        ...
    


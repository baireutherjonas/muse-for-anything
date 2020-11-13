"""
This type stub file was generated by pyright.
"""

from .interfaces import MapperOption
from ..sql.base import Generative, _generative

"""

"""
class Load(Generative, MapperOption):
    """Represents loader options which modify the state of a
    :class:`_query.Query` in order to affect how various mapped attributes are
    loaded.

    The :class:`_orm.Load` object is in most cases used implicitly behind the
    scenes when one makes use of a query option like :func:`_orm.joinedload`,
    :func:`.defer`, or similar.   However, the :class:`_orm.Load` object
    can also be used directly, and in some cases can be useful.

    To use :class:`_orm.Load` directly, instantiate it with the target mapped
    class as the argument.   This style of usage is
    useful when dealing with a :class:`_query.Query`
    that has multiple entities::

        myopt = Load(MyClass).joinedload("widgets")

    The above ``myopt`` can now be used with :meth:`_query.Query.options`,
    where it
    will only take effect for the ``MyClass`` entity::

        session.query(MyClass, MyOtherClass).options(myopt)

    One case where :class:`_orm.Load`
    is useful as public API is when specifying
    "wildcard" options that only take effect for a certain class::

        session.query(Order).options(Load(Order).lazyload('*'))

    Above, all relationships on ``Order`` will be lazy-loaded, but other
    attributes on those descendant objects will load using their normal
    loader strategy.

    .. seealso::

        :ref:`deferred_options`

        :ref:`deferred_loading_w_multiple`

        :ref:`relationship_loader_options`

    """
    def __init__(self, entity) -> None:
        ...
    
    @classmethod
    def for_existing_path(cls, path):
        ...
    
    is_opts_only = ...
    is_class_strategy = ...
    strategy = ...
    propagate_to_loaders = ...
    _of_type = ...
    def process_query(self, query):
        ...
    
    def process_query_conditionally(self, query):
        ...
    
    def __str__(self) -> str:
        ...
    
    @_generative
    def options(self, *opts):
        r"""Apply a series of options as sub-options to this
        :class:`_orm.Load`
        object.

        E.g.::

            query = session.query(Author)
            query = query.options(
                        joinedload(Author.book).options(
                            load_only("summary", "excerpt"),
                            joinedload(Book.citations).options(
                                joinedload(Citation.author)
                            )
                        )
                    )

        :param \*opts: A series of loader option objects (ultimately
         :class:`_orm.Load` objects) which should be applied to the path
         specified by this :class:`_orm.Load` object.

        .. versionadded:: 1.3.6

        .. seealso::

            :func:`.defaultload`

            :ref:`relationship_loader_options`

            :ref:`deferred_loading_w_multiple`

        """
        ...
    
    @_generative
    def set_relationship_strategy(self, attr, strategy, propagate_to_loaders=...):
        ...
    
    @_generative
    def set_column_strategy(self, attrs, strategy, opts=..., opts_only=...):
        ...
    
    @_generative
    def set_generic_strategy(self, attrs, strategy):
        ...
    
    @_generative
    def set_class_strategy(self, strategy, opts):
        ...
    
    def __getstate__(self):
        ...
    
    def __setstate__(self, state):
        ...
    


class _UnboundLoad(Load):
    """Represent a loader option that isn't tied to a root entity.

    The loader option will produce an entity-linked :class:`_orm.Load`
    object when it is passed :meth:`_query.Query.options`.

    This provides compatibility with the traditional system
    of freestanding options, e.g. ``joinedload('x.y.z')``.

    """
    def __init__(self) -> None:
        ...
    
    _is_chain_link = ...
    def __getstate__(self):
        ...
    
    def __setstate__(self, state):
        ...
    


class loader_option(object):
    def __init__(self) -> None:
        ...
    
    def __call__(self, fn):
        ...
    


@loader_option()
def contains_eager(loadopt, attr, alias=...):
    r"""Indicate that the given attribute should be eagerly loaded from
    columns stated manually in the query.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    The option is used in conjunction with an explicit join that loads
    the desired rows, i.e.::

        sess.query(Order).\
                join(Order.user).\
                options(contains_eager(Order.user))

    The above query would join from the ``Order`` entity to its related
    ``User`` entity, and the returned ``Order`` objects would have the
    ``Order.user`` attribute pre-populated.

    When making use of aliases with :func:`.contains_eager`, the path
    should be specified using :meth:`.PropComparator.of_type`::

        user_alias = aliased(User)
        sess.query(Order).\
                join((user_alias, Order.user)).\
                options(contains_eager(Order.user.of_type(user_alias)))

    :meth:`.PropComparator.of_type` is also used to indicate a join
    against specific subclasses of an inherting mapper, or
    of a :func:`.with_polymorphic` construct::

        # employees of a particular subtype
        sess.query(Company).\
            outerjoin(Company.employees.of_type(Manager)).\
            options(
                contains_eager(
                    Company.employees.of_type(Manager),
                )
            )

        # employees of a multiple subtypes
        wp = with_polymorphic(Employee, [Manager, Engineer])
        sess.query(Company).\
            outerjoin(Company.employees.of_type(wp)).\
            options(
                contains_eager(
                    Company.employees.of_type(wp),
                )
            )

    The :paramref:`.contains_eager.alias` parameter is used for a similar
    purpose, however the :meth:`.PropComparator.of_type` approach should work
    in all cases and is more effective and explicit.

    .. seealso::

        :ref:`loading_toplevel`

        :ref:`contains_eager`

    """
    ...

@contains_eager._add_unbound_fn
def contains_eager(*keys, **kw):
    ...

@loader_option()
def load_only(loadopt, *attrs):
    """Indicate that for a particular entity, only the given list
    of column-based attribute names should be loaded; all others will be
    deferred.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    Example - given a class ``User``, load only the ``name`` and ``fullname``
    attributes::

        session.query(User).options(load_only("name", "fullname"))

    Example - given a relationship ``User.addresses -> Address``, specify
    subquery loading for the ``User.addresses`` collection, but on each
    ``Address`` object load only the ``email_address`` attribute::

        session.query(User).options(
                subqueryload("addresses").load_only("email_address")
        )

    For a :class:`_query.Query` that has multiple entities,
    the lead entity can be
    specifically referred to using the :class:`_orm.Load` constructor::

        session.query(User, Address).join(User.addresses).options(
                    Load(User).load_only("name", "fullname"),
                    Load(Address).load_only("email_address")
                )

     .. note:: This method will still load a :class:`_schema.Column` even
        if the column property is defined with ``deferred=True``
        for the :func:`.column_property` function.

    .. versionadded:: 0.9.0

    """
    ...

@load_only._add_unbound_fn
def load_only(*attrs):
    ...

@loader_option()
def joinedload(loadopt, attr, innerjoin=...):
    """Indicate that the given attribute should be loaded using joined
    eager loading.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    examples::

        # joined-load the "orders" collection on "User"
        query(User).options(joinedload(User.orders))

        # joined-load Order.items and then Item.keywords
        query(Order).options(
            joinedload(Order.items).joinedload(Item.keywords))

        # lazily load Order.items, but when Items are loaded,
        # joined-load the keywords collection
        query(Order).options(
            lazyload(Order.items).joinedload(Item.keywords))

    :param innerjoin: if ``True``, indicates that the joined eager load should
     use an inner join instead of the default of left outer join::

        query(Order).options(joinedload(Order.user, innerjoin=True))

     In order to chain multiple eager joins together where some may be
     OUTER and others INNER, right-nested joins are used to link them::

        query(A).options(
            joinedload(A.bs, innerjoin=False).
                joinedload(B.cs, innerjoin=True)
        )

     The above query, linking A.bs via "outer" join and B.cs via "inner" join
     would render the joins as "a LEFT OUTER JOIN (b JOIN c)".   When using
     older versions of SQLite (< 3.7.16), this form of JOIN is translated to
     use full subqueries as this syntax is otherwise not directly supported.

     The ``innerjoin`` flag can also be stated with the term ``"unnested"``.
     This indicates that an INNER JOIN should be used, *unless* the join
     is linked to a LEFT OUTER JOIN to the left, in which case it
     will render as LEFT OUTER JOIN.  For example, supposing ``A.bs``
     is an outerjoin::

        query(A).options(
            joinedload(A.bs).
                joinedload(B.cs, innerjoin="unnested")
        )

     The above join will render as "a LEFT OUTER JOIN b LEFT OUTER JOIN c",
     rather than as "a LEFT OUTER JOIN (b JOIN c)".

     .. note:: The "unnested" flag does **not** affect the JOIN rendered
        from a many-to-many association table, e.g. a table configured
        as :paramref:`_orm.relationship.secondary`, to the target table; for
        correctness of results, these joins are always INNER and are
        therefore right-nested if linked to an OUTER join.

     .. versionchanged:: 1.0.0 ``innerjoin=True`` now implies
        ``innerjoin="nested"``, whereas in 0.9 it implied
        ``innerjoin="unnested"``.  In order to achieve the pre-1.0 "unnested"
        inner join behavior, use the value ``innerjoin="unnested"``.
        See :ref:`migration_3008`.

    .. note::

        The joins produced by :func:`_orm.joinedload` are **anonymously
        aliased**.  The criteria by which the join proceeds cannot be
        modified, nor can the :class:`_query.Query`
        refer to these joins in any way,
        including ordering.  See :ref:`zen_of_eager_loading` for further
        detail.

        To produce a specific SQL JOIN which is explicitly available, use
        :meth:`_query.Query.join`.
        To combine explicit JOINs with eager loading
        of collections, use :func:`_orm.contains_eager`; see
        :ref:`contains_eager`.

    .. seealso::

        :ref:`loading_toplevel`

        :ref:`joined_eager_loading`

    """
    ...

@joinedload._add_unbound_fn
def joinedload(*keys, **kw):
    ...

@joinedload._add_unbound_all_fn
def joinedload_all(*keys, **kw):
    ...

@loader_option()
def subqueryload(loadopt, attr):
    """Indicate that the given attribute should be loaded using
    subquery eager loading.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    examples::

        # subquery-load the "orders" collection on "User"
        query(User).options(subqueryload(User.orders))

        # subquery-load Order.items and then Item.keywords
        query(Order).options(
            subqueryload(Order.items).subqueryload(Item.keywords))

        # lazily load Order.items, but when Items are loaded,
        # subquery-load the keywords collection
        query(Order).options(
            lazyload(Order.items).subqueryload(Item.keywords))


    .. seealso::

        :ref:`loading_toplevel`

        :ref:`subquery_eager_loading`

    """
    ...

@subqueryload._add_unbound_fn
def subqueryload(*keys):
    ...

@subqueryload._add_unbound_all_fn
def subqueryload_all(*keys):
    ...

@loader_option()
def selectinload(loadopt, attr):
    """Indicate that the given attribute should be loaded using
    SELECT IN eager loading.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    examples::

        # selectin-load the "orders" collection on "User"
        query(User).options(selectinload(User.orders))

        # selectin-load Order.items and then Item.keywords
        query(Order).options(
            selectinload(Order.items).selectinload(Item.keywords))

        # lazily load Order.items, but when Items are loaded,
        # selectin-load the keywords collection
        query(Order).options(
            lazyload(Order.items).selectinload(Item.keywords))

    .. versionadded:: 1.2

    .. seealso::

        :ref:`loading_toplevel`

        :ref:`selectin_eager_loading`

    """
    ...

@selectinload._add_unbound_fn
def selectinload(*keys):
    ...

@selectinload._add_unbound_all_fn
def selectinload_all(*keys):
    ...

@loader_option()
def lazyload(loadopt, attr):
    """Indicate that the given attribute should be loaded using "lazy"
    loading.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    .. seealso::

        :ref:`loading_toplevel`

        :ref:`lazy_loading`

    """
    ...

@lazyload._add_unbound_fn
def lazyload(*keys):
    ...

@lazyload._add_unbound_all_fn
def lazyload_all(*keys):
    ...

@loader_option()
def immediateload(loadopt, attr):
    """Indicate that the given attribute should be loaded using
    an immediate load with a per-attribute SELECT statement.

    The :func:`.immediateload` option is superseded in general
    by the :func:`.selectinload` option, which performs the same task
    more efficiently by emitting a SELECT for all loaded objects.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    .. seealso::

        :ref:`loading_toplevel`

        :ref:`selectin_eager_loading`

    """
    ...

@immediateload._add_unbound_fn
def immediateload(*keys):
    ...

@loader_option()
def noload(loadopt, attr):
    """Indicate that the given relationship attribute should remain unloaded.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    :func:`_orm.noload` applies to :func:`_orm.relationship` attributes; for
    column-based attributes, see :func:`_orm.defer`.

    .. seealso::

        :ref:`loading_toplevel`

    """
    ...

@noload._add_unbound_fn
def noload(*keys):
    ...

@loader_option()
def raiseload(loadopt, attr, sql_only=...):
    """Indicate that the given relationship attribute should disallow lazy loads.

    A relationship attribute configured with :func:`_orm.raiseload` will
    raise an :exc:`~sqlalchemy.exc.InvalidRequestError` upon access.   The
    typical way this is useful is when an application is attempting to ensure
    that all relationship attributes that are accessed in a particular context
    would have been already loaded via eager loading.  Instead of having
    to read through SQL logs to ensure lazy loads aren't occurring, this
    strategy will cause them to raise immediately.

    :param sql_only: if True, raise only if the lazy load would emit SQL,
     but not if it is only checking the identity map, or determining that
     the related value should just be None due to missing keys.  When False,
     the strategy will raise for all varieties of lazyload.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    :func:`_orm.raiseload` applies to :func:`_orm.relationship`
    attributes only.

    .. versionadded:: 1.1

    .. seealso::

        :ref:`loading_toplevel`

        :ref:`prevent_lazy_with_raiseload`

    """
    ...

@raiseload._add_unbound_fn
def raiseload(*keys, **kw):
    ...

@loader_option()
def defaultload(loadopt, attr):
    """Indicate an attribute should load using its default loader style.

    This method is used to link to other loader options further into
    a chain of attributes without altering the loader style of the links
    along the chain.  For example, to set joined eager loading for an
    element of an element::

        session.query(MyClass).options(
            defaultload(MyClass.someattribute).
            joinedload(MyOtherClass.someotherattribute)
        )

    :func:`.defaultload` is also useful for setting column-level options
    on a related class, namely that of :func:`.defer` and :func:`.undefer`::

        session.query(MyClass).options(
            defaultload(MyClass.someattribute).
            defer("some_column").
            undefer("some_other_column")
        )

    .. seealso::

        :meth:`_orm.Load.options` - allows for complex hierarchical
        loader option structures with less verbosity than with individual
        :func:`.defaultload` directives.

        :ref:`relationship_loader_options`

        :ref:`deferred_loading_w_multiple`

    """
    ...

@defaultload._add_unbound_fn
def defaultload(*keys):
    ...

@loader_option()
def defer(loadopt, key):
    r"""Indicate that the given column-oriented attribute should be deferred,
    e.g. not loaded until accessed.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    e.g.::

        from sqlalchemy.orm import defer

        session.query(MyClass).options(
                            defer("attribute_one"),
                            defer("attribute_two"))

        session.query(MyClass).options(
                            defer(MyClass.attribute_one),
                            defer(MyClass.attribute_two))

    To specify a deferred load of an attribute on a related class,
    the path can be specified one token at a time, specifying the loading
    style for each link along the chain.  To leave the loading style
    for a link unchanged, use :func:`_orm.defaultload`::

        session.query(MyClass).options(defaultload("someattr").defer("some_column"))

    A :class:`_orm.Load` object that is present on a certain path can have
    :meth:`_orm.Load.defer` called multiple times,
    each will operate on the same
    parent entity::


        session.query(MyClass).options(
                        defaultload("someattr").
                            defer("some_column").
                            defer("some_other_column").
                            defer("another_column")
            )

    :param key: Attribute to be deferred.

    :param \*addl_attrs: This option supports the old 0.8 style
     of specifying a path as a series of attributes, which is now superseded
     by the method-chained style.

        .. deprecated:: 0.9  The \*addl_attrs on :func:`_orm.defer` is
           deprecated and will be removed in a future release.   Please
           use method chaining in conjunction with defaultload() to
           indicate a path.


    .. seealso::

        :ref:`deferred`

        :func:`_orm.undefer`

    """
    ...

@defer._add_unbound_fn
def defer(key, *addl_attrs):
    ...

@loader_option()
def undefer(loadopt, key):
    r"""Indicate that the given column-oriented attribute should be undeferred,
    e.g. specified within the SELECT statement of the entity as a whole.

    The column being undeferred is typically set up on the mapping as a
    :func:`.deferred` attribute.

    This function is part of the :class:`_orm.Load` interface and supports
    both method-chained and standalone operation.

    Examples::

        # undefer two columns
        session.query(MyClass).options(undefer("col1"), undefer("col2"))

        # undefer all columns specific to a single class using Load + *
        session.query(MyClass, MyOtherClass).options(
            Load(MyClass).undefer("*"))

        # undefer a column on a related object
        session.query(MyClass).options(
            defaultload(MyClass.items).undefer('text'))

    :param key: Attribute to be undeferred.

    :param \*addl_attrs: This option supports the old 0.8 style
     of specifying a path as a series of attributes, which is now superseded
     by the method-chained style.

        .. deprecated:: 0.9  The \*addl_attrs on :func:`_orm.undefer` is
           deprecated and will be removed in a future release.   Please
           use method chaining in conjunction with defaultload() to
           indicate a path.

    .. seealso::

        :ref:`deferred`

        :func:`_orm.defer`

        :func:`_orm.undefer_group`

    """
    ...

@undefer._add_unbound_fn
def undefer(key, *addl_attrs):
    ...

@loader_option()
def undefer_group(loadopt, name):
    """Indicate that columns within the given deferred group name should be
    undeferred.

    The columns being undeferred are set up on the mapping as
    :func:`.deferred` attributes and include a "group" name.

    E.g::

        session.query(MyClass).options(undefer_group("large_attrs"))

    To undefer a group of attributes on a related entity, the path can be
    spelled out using relationship loader options, such as
    :func:`_orm.defaultload`::

        session.query(MyClass).options(
            defaultload("someattr").undefer_group("large_attrs"))

    .. versionchanged:: 0.9.0 :func:`_orm.undefer_group` is now specific to a
       particular entity load path.

    .. seealso::

        :ref:`deferred`

        :func:`_orm.defer`

        :func:`_orm.undefer`

    """
    ...

@undefer_group._add_unbound_fn
def undefer_group(name):
    ...

@loader_option()
def with_expression(loadopt, key, expression):
    r"""Apply an ad-hoc SQL expression to a "deferred expression" attribute.

    This option is used in conjunction with the :func:`_orm.query_expression`
    mapper-level construct that indicates an attribute which should be the
    target of an ad-hoc SQL expression.

    E.g.::


        sess.query(SomeClass).options(
            with_expression(SomeClass.x_y_expr, SomeClass.x + SomeClass.y)
        )

    .. versionadded:: 1.2

    :param key: Attribute to be undeferred.

    :param expr: SQL expression to be applied to the attribute.

    .. note:: the target attribute is populated only if the target object
       is **not currently loaded** in the current :class:`_orm.Session`
       unless the :meth:`_orm.Query.populate_existing` method is used.
       Please refer to :ref:`mapper_querytime_expression` for complete
       usage details.

    .. seealso::

        :ref:`mapper_querytime_expression`

    """
    ...

@with_expression._add_unbound_fn
def with_expression(key, expression):
    ...

@loader_option()
def selectin_polymorphic(loadopt, classes):
    """Indicate an eager load should take place for all attributes
    specific to a subclass.

    This uses an additional SELECT with IN against all matched primary
    key values, and is the per-query analogue to the ``"selectin"``
    setting on the :paramref:`.mapper.polymorphic_load` parameter.

    .. versionadded:: 1.2

    .. seealso::

        :ref:`polymorphic_selectin`

    """
    ...

@selectin_polymorphic._add_unbound_fn
def selectin_polymorphic(base_cls, classes):
    ...


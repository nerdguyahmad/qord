.. currentmodule:: qord

.. _api-events:

Events (``qord.events``)
=========================

Qord exposes a rich interface via :class:`Client` class that allows you to listen
to specific gateway events and perform certain operations on those events. In addition
to this, This interface also allows you to create and invoke custom events.


.. _api-events-registering-event-listeners:

Registering event listeners
---------------------------

The recommended way to register an event listener, is to use the :meth:`qord.Client.event`
decorator to decorate the callback coroutine. However when subclassing :class:`Client`, consider
using the :func:`qord.event` decorator. Example::

    @client.event(qord.GatewayEvent.MESSAGE_CREATE)
    async def on_message_create(event):
        pass

    # ---- or ----

    class MyClient(qord.Client):
        @qord.event(qord.GatewayEvent.MESSAGE_CREATE)
        async def on_message_create(event):
            pass

All event listeners must take a single ``event`` parameter that is an instance
of one of :ref:`api-events-event-objects` representing the context of event and
contains data relevant to the invoked event.

The :class:`qord.GatewayEvent` enumeration details the event names that are sent over gateway.

.. note::
    Toggling certain :class:`Intents` flags will also disable or enable related
    gateway events to that intent for your bot. It is recommended to keep at
    least the :attr:`Intents.guilds` intent enabled for proper functioning of library.

.. autofunction:: qord.event


.. _api-events-custom-events:

Custom events
-------------

Custom events are useful for several use cases and library allows you to create
them and easily invoke them.

Inherit a class from :class:`events.BaseEvent` with ``event_name`` parameter
being the name of event. The instance of this class will be passed to the
event listeners as the context of this event.

.. warning::

    Make sure **not** to use an already reserved event name from :class:`GatewayEvent`
    or any other event names provided by the library.

Example::

    from qord import events
    from dataclasses import dataclass

    @dataclass
    class ApplicationSubmit(events.BaseEvent, event_name="application_submit"):
        id: int
        name: str

    @client.event("application_submit")
    async def on_application_submit(event: ApplicationSubmit):
        print("Application submitted.")
        print(f"Name: {event.name}")
        print(f"ID: {event.id}")

You can then invoke the event somewhere else using :meth:`Client.invoke_event` method
and passing the event object::

    event = ApplicationSubmit(id=1, name="Jake")
    client.invoke_event(event)

.. _api-events-base-classes:

Base Classes
------------

These are some base classes for the :ref:`api-events-event-objects`

BaseEvent
~~~~~~~~~

.. autoclass:: qord.events.BaseEvent()
    :members:

BaseGatewayEvent
~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.BaseGatewayEvent()
    :members:


.. _api-events-event-objects:

Event Objects
-------------

The classes documented below expose the data related to a specific gateway event. The
instance of these classes are passed to the event listener coroutines.

GatewayDispatch
~~~~~~~~~~~~~~~

.. autoclass:: qord.events.GatewayDispatch()
    :members:

ShardReady
~~~~~~~~~~

.. autoclass:: qord.events.ShardReady()
    :members:

Ready
~~~~~

.. autoclass:: qord.events.Ready()
    :members:

Resumed
~~~~~~~

.. autoclass:: qord.events.Resumed()
    :members:

UserUpdate
~~~~~~~~~~

.. autoclass:: qord.events.UserUpdate()
    :members:

GuildAvailable
~~~~~~~~~~~~~~

.. autoclass:: qord.events.GuildAvailable()
    :members:

GuildUnavailable
~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.GuildUnavailable()
    :members:

GuildJoin
~~~~~~~~~

.. autoclass:: qord.events.GuildJoin()
    :members:


GuildLeave
~~~~~~~~~~

.. autoclass:: qord.events.GuildLeave()
    :members:

GuildUpdate
~~~~~~~~~~~

.. autoclass:: qord.events.GuildUpdate()
    :members:

RoleCreate
~~~~~~~~~~

.. autoclass:: qord.events.RoleCreate()
    :members:

RoleUpdate
~~~~~~~~~~

.. autoclass:: qord.events.RoleUpdate()
    :members:

RoleDelete
~~~~~~~~~~

.. autoclass:: qord.events.RoleDelete()
    :members:

GuildMemberAdd
~~~~~~~~~~~~~~

.. autoclass:: qord.events.GuildMemberAdd()
    :members:

GuildMemberUpdate
~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.GuildMemberUpdate()
    :members:

GuildMemberRemove
~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.GuildMemberRemove()
    :members:


ChannelCreate
~~~~~~~~~~~~~

.. autoclass:: qord.events.ChannelCreate()
    :members:


ChannelUpdate
~~~~~~~~~~~~~

.. autoclass:: qord.events.ChannelUpdate()
    :members:

ChannelPinsUpdate
~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.ChannelPinsUpdate()
    :members:

ChannelDelete
~~~~~~~~~~~~~

.. autoclass:: qord.events.ChannelDelete()
    :members:

TypingStart
~~~~~~~~~~~

.. autoclass:: qord.events.TypingStart()
    :members:

EmojisUpdate
~~~~~~~~~~~~

.. autoclass:: qord.events.EmojisUpdate()
    :members:

MessageCreate
~~~~~~~~~~~~~

.. autoclass:: qord.events.MessageCreate()
    :members:


MessageUpdate
~~~~~~~~~~~~~

.. autoclass:: qord.events.MessageUpdate()
    :members:


MessageDelete
~~~~~~~~~~~~~

.. autoclass:: qord.events.MessageDelete()
    :members:


MessageBulkDelete
~~~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.MessageBulkDelete()
    :members:

ReactionAdd
~~~~~~~~~~~

.. autoclass:: qord.events.ReactionAdd()
    :members:

ReactionRemove
~~~~~~~~~~~~~~

.. autoclass:: qord.events.ReactionRemove()
    :members:

ReactionClear
~~~~~~~~~~~~~

.. autoclass:: qord.events.ReactionClear()
    :members:

ReactionClearEmoji
~~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.ReactionClearEmoji()
    :members:


ScheduledEventCreate
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.ScheduledEventCreate()
    :members:


ScheduledEventUpdate
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.ScheduledEventUpdate()
    :members:


ScheduledEventDelete
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.ScheduledEventDelete()
    :members:


ScheduledEventUserAdd
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.ScheduledEventUserAdd()
    :members:

ScheduledEventUserRemove
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: qord.events.ScheduledEventUserRemove()
    :members:


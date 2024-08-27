mixpanel-python
==============================

This is the unofficial Mixpanel Python asyncio library. This library allows for
server-side integration of Mixpanel.

To import, export, transform, or delete your Mixpanel data, please see Mixpanel's
`mixpanel-utils package`_.


Installation
------------

The library can be installed using pip::

    pip install https://github.com/Brave-AI-Lab/mixpanel-python-asyncio/archive/master.zip


Getting Started
---------------

Typical usage usually looks like this::

    from mixpanel_asyncio import Mixpanel

    mp = Mixpanel(YOUR_TOKEN)

    # tracks an event with certain properties
    await mp.track(DISTINCT_ID, 'button clicked', {'color' : 'blue', 'size': 'large'})

    # sends an update to a user profile
    await mp.people_set(DISTINCT_ID, {'$first_name' : 'Ilya', 'favorite pizza': 'margherita'})

You can use an instance of the Mixpanel class for sending all of your events
and people updates.


Additional Information
----------------------

* `Help Docs`_
* `Full Documentation`_


.. |travis-badge| image:: https://travis-ci.org/mixpanel/mixpanel-python.svg?branch=master
    :target: https://travis-ci.org/mixpanel/mixpanel-python
.. _mixpanel-utils package: https://github.com/mixpanel/mixpanel-utils
.. _Help Docs: https://www.mixpanel.com/help/reference/python
.. _Full Documentation: http://mixpanel.github.io/mixpanel-python/
.. _mixpanel-python-async: https://github.com/jessepollak/mixpanel-python-async

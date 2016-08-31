djangocms-maps
==============

A universal maps plugin for django CMS, supporting all major map providers.

Supported online map providers:

- Mapbox OpenStreetMap *powered by* `Leaflet.js`_
- Bing Maps
- Google Maps
- HERE WeGo
- ViaMichelin

As of today (2016) all map providers require an API key.

Installation
------------

This plugin requires `django CMS`_ 3.3 (and Django 1.8) or above.

* In your project's `virtualenv`_, run ``pip install djangocms-maps``.
* Add ``'djangocms_maps'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_maps``.

Configuration
-------------

``MAPS_PROVIDERS``
~~~~~~~~~~~~~~~~~~
Allows you to specify the providers you want to offer, their display labels
and sort order in the user interface.  Put a provider on top of the list to
make it the default.

.. code-block:: python

    MAPS_PROVIDERS = [
        ('mapbox', _('Mapbox OSM (API key required)')),
        ('bingmaps', _('Bing Maps (API key required)')),
        ('googlemaps', _('Google Maps (API key required)')),
        ('here', _('HERE WeGo (API key required)')),
        ('viamichelin', _('ViaMichelin (API key required)')),
    ]

``MAPS_BINGMAPS_API_KEY``
~~~~~~~~~~~~~~~~~~~~~~~~~
`API key for Bing Maps`_ (required for using Bing Maps).

``MAPS_GOOGLEMAPS_API_KEY``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
`API key for Google Maps`_ (required for using Google Maps).

``MAPS_HERE_API_KEY``
~~~~~~~~~~~~~~~~~~~~~
`API key for HERE WeGo`_ (required for using HERE maps).

``MAPS_MAPBOX_API_KEY``
~~~~~~~~~~~~~~~~~~~~~~~
`Access token for Mapbox`_ (required for using OSM maps with Mapbox tile layers).

``MAPS_VIAMICHELIN_API_KEY``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`API key for ViaMichelin`_ (required for using ViaMichelin maps).

Translations
------------

If you want to help translate the plugin please do it on `transifex`_.

Developer Resources
-------------------

- Bing:
  - `Dev Center <https://www.bingmapsportal.com/>`_
  - `API docs <https://msdn.microsoft.com/en-us/library/mt712552.aspx>`_
  - `examples <https://msdn.microsoft.com/en-us/library/mt712542.aspx>`_
- Google:
  - `API docs <https://developers.google.com/maps/documentation/javascript/>`_
- HERE:
  - `API docs <https://developer.here.com/>`_
  - `examples <https://developer.here.com/api-explorer/maps-js/>`_
- Mapbox.js / Leaflet.js:
  - `API docs <https://www.mapbox.com/mapbox.js/api/>`_
  - `examples <https://www.mapbox.com/mapbox.js/examples/>`_
  - `Leaflet API docs <http://leafletjs.com/reference.html>`_
- ViaMichelin:
  - `API docs <http://dev.viamichelin.com/map-service.html>`_


.. _Leaflet.js: http://leafletjs.com/
.. _django CMS: https://github.com/divio/django-cms
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _API key for Bing Maps: https://msdn.microsoft.com/en-us/library/mt712556.aspx
.. _API key for Google Maps: https://developers.google.com/maps/documentation/javascript/get-api-key
.. _API key for HERE WeGo: https://developer.here.com/javascript-apis/documentation/v3/maps/common/credentials.html
.. _Access token for Mapbox: https://www.mapbox.com/help/create-api-access-token/
.. _API key for ViaMichelin: http://business-solutions.travel.michelin.com/contact-us/open-a-free-api-test-account.html
.. _transifex: https://www.transifex.com/divio/djangocms-maps/

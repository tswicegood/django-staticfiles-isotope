django-staticfiles-isotope
==========================
Isotope meets Django staticfiles


Usage
-----
This application is meant to be used with `django-staticfiles`_.  Make sure
that staticfiles setup and configured, then install this application using
`pip`_:

::

	pip install django-staticfiles-isotope

Finally, make sure that `isotope` is listed in your ``INSTALLED_APPS``.  You
can use this oneliner to add it as well:

::

	INSTALLED_APPS += ['isotope', ]


Build
-----
`Isotope`_ packages pre-built versions of the code in its Git repository.  No
further tools are necessary to build it.  See ``support/build.py`` for more
information on how data is transferred from the submodule to the Python
package.


License
-------
Isotope is licensed under a `custom license`_.  Please visit their site to see
whether you qualify for a free license.


.. _custom license: http://isotope.metafizzy.co/docs/license.html
.. _django-staticfiles: https://github.com/jezdez/django-staticfiles
.. _pip: http://www.pip-installer.org/
.. _Isotope: http://isotope.metafizzy.co/

========================
Custom Screen Resolution
========================


.. image:: https://img.shields.io/pypi/v/custom_screen_resolution.svg
        :target: https://pypi.python.org/pypi/custom_screen_resolution

.. image:: https://travis-ci.com/anopensourcecoder/custom_screen_resolution.svg?branch=master
        :target: https://travis-ci.com/anopensourcecoder/custom_screen_resolution

.. image:: https://readthedocs.org/projects/custom-screen-resolution/badge/?version=latest
        :target: https://custom-screen-resolution.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/anopensourcecoder/custom_screen_resolution/shield.svg
     :target: https://pyup.io/repos/github/anopensourcecoder/custom_screen_resolution/
     :alt: Updates



Create custom resolution base on screen size, dpi and zoom level.

I find myself to be comfortable with screen DPI between 100 to 140 depends to the distance between display and me. High DPI might be usefull for graphic software but it has issue with remote desktop and older software. Also when you have multiple displays with different DPI.

This software allow to create custom screen resolution that can solve the problem.
It can create custom resolution with same DPI at higher zoom level.
This way you can have both sharp pixel at native resolution while having lower DPI.
You also can use it to have a lower resolution at your comfort DPI level.
This can help to save power and battery life that is important for portable device.
Lower resolution and DPI need less internet bandwidth too.
This can improve remote desktop performance.



* Free software: GNU General Public License v3
* Documentation: https://custom-screen-resolution.readthedocs.io.


Features
--------

* Gui and Cli interface.
* Calculate Width and height base on screen size, dpi and aspect ratio ( via cli and gui )
* Calculate screen size base on resolution and dpi ( via cli)
* Calculate screen size base on screen size and dpi and zoom level ( via cli)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

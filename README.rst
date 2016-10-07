hackathon
==============================

Django project for a Barcelona Data Hackathon. Provides a platform to evaluate model submission for a prediction problem. Kaggle like.


Quickstart
------------

.. code-block:: python

    pip install -r requirements/local.py
    python manage migrate
    python manage createsuperuser
    python manage runserver

Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.org/en/latest/settings.html


Deployment
----------

We providing tools and instructions for deploying using Docker and Heroku.

Heroku
^^^^^^

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-on-heroku.html

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-with-docker.html

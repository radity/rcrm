# Standart Library
from __future__ import absolute_import

# Celery
from rcrm.celery import app as celery_app


__all__ = ['celery_app']

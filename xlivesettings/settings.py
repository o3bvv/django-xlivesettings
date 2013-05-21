# -*- coding: utf-8 -*-
"""
Settings for website app.
"""
from __future__ import unicode_literals

from django.conf import settings

LANGUAGES_DICT = dict(
    getattr(settings, 'LANGUAGES', '')
)

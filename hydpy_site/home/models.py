from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField


class HomePage(Page):
    pass


class HydPyBase(Page):
    body = RichTextField(blank=True)

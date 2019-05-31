# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include, url
from django.contrib import admin


app_name = '{{ cookiecutter.app_name }}'
urlpatterns = [
    url(r'^', include('{{ cookiecutter.app_name }}.urls')),
    url(r'^admin/', admin.site.urls),
]

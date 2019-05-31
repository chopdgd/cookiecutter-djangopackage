# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

from {{ cookiecutter.app_name }}.urls import urlpatterns as {{ cookiecutter.app_name }}_urls


app_name = '{{ cookiecutter.app_name }}'
urlpatterns = [
    url(r'^', include({{ cookiecutter.app_name }}_urls)),
    url(r'^admin/', admin.site.urls),
]

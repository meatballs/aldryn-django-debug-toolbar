# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

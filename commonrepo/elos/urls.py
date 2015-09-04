# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^create/$',
        view=views.MyELOsCreateView.as_view(),
        name="elos-create"
    ),
    url(
        regex=r'^$',
        view=views.MyELOsListView.as_view(),
        name='elos-mylist'
    ),
    url(
        regex=r'^view/(?P<pk>[0-9]+)/$',
        view=views.MyELOsDetailView.as_view(),
        name='elos-view'
    ),
]

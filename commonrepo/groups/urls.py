# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^create/$',
        view=views.GroupsCreateView.as_view(),
        name="groups-create"
    ),
    url(
        regex=r'^all/$',
        view=views.GroupsListView.as_view(),
        name="groups-alllist"
        ),    
    url(
        regex=r'^$',
        view=views.GroupsMyListView.as_view(),
        name='groups-mylist'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.GroupsDetailView.as_view(),
        name='groups-detail'
    ),
    url(
        regex=r'^update/(?P<pk>[0-9]+)/$',
        view=views.GroupsUpdateView.as_view(),
        name='groups-update'
    ),
]
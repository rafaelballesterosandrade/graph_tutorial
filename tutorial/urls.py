# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from django.urls import path

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('callback', views.callback, name='callback'),
  path('calendar', views.calendar, name='calendar'),
  path('usuario_nuevo', views.usuario_nuevo, name='usuario_nuevo'),
  path('usuario_lista', views.usuario_lista, name='usuario_lista'),
  path('usuario_dato', views.usuario_dato, name='usuario_dato'),
]

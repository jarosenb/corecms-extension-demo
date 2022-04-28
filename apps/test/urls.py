"""
.. module:: portal.apps.site_search.urls
   :synopsis: Site Search URLs
"""
from django.urls import re_path
from .views import AddedView

app_name = 'test'
urlpatterns = [
    re_path('', AddedView, name='index'),
]
from django.urls import path, include

extra_urls = [
    path('test/', include('apps.test.urls', namespace='portal_accounts')),
]

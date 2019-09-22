from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('custom_auth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('silk/', include('silk.urls', namespace='silk')),
    ]

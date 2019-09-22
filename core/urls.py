from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
    ]

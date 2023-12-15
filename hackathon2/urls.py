from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('overview/', include('overview.urls'), name='overview'),
]

from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    url('auth/', include('social_django.urls', namespace='social')),
    path('', include('rick.urls',  namespace='rick'))
]

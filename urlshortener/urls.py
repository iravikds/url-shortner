from django.contrib import admin
from django.urls import path, include
from urlshort.views import generate, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlshort.urls')),
    path('generate/', generate, name='generate'),
    path('<str:query>/', index, name='index'),
]

from django.urls import include, path
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'Library', views.LibraryViewSet)

urlpatterns = [
    #path('', views.index, name='Homepage'),
    path('', include(routers.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
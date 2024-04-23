from django.urls import path
from api import views
from django.urls import include
from rest_framework import routers
# from django.views.generic.base import RedirectView


router = routers.DefaultRouter()
router.register(r'api', views.hdtViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    # path('', RedirectView.as_view(url='api/')),
]
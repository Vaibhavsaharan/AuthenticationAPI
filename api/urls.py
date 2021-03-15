from django.urls import  path, include
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^api/validate1$', views.validate_finite_values_entity_util),
    url(r'^api/validate2$', views.validate_numeric_entity_util),
    url(r'$', views.home)
]
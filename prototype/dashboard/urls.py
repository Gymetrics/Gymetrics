from django.conf.urls import url 
from .views import index

urlpatterns = [
    url(r'^channels/', index, name='home'), 
]

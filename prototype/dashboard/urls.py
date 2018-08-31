from django.conf.urls import url 
from .views import index, api_update_gym

urlpatterns = [
    url(r'^channels/', index, name='home'), 
    url(r'^api/gym', api_update_gym, name="api_stream"),
]

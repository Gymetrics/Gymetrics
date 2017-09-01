from django.conf.urls import url 
from .views import index, api_stream_view

urlpatterns = [
    url(r'^channels/', index, name='home'), 
    url(r'^api/stream', api_stream_view, name="api_stream"),
]

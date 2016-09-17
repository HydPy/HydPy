from django.conf.urls import url
from .views import home_page


urlpatterns = [
    url(r'^home/$', home_page, name='homepage'),
]
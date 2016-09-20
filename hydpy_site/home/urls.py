from django.conf.urls import url
from .views import home_page, about_page,events_page


urlpatterns = [
    url(r'^home/$', home_page, name='homepage'),
    url(r'^events/$', events_page, name='events'),
    url(r'^about/$', about_page, name='about_us'),
]
from django.conf.urls import url
from .views import home_page, about_page, events_page, faqs_page


urlpatterns = [
    url(r'^events$', events_page, name='events'),
    url(r'^about$', about_page, name='about_us'),
    url(r'^faqs$', faqs_page, name='faqs_page'),
    url(r'^', home_page, name='homepage'),
]

from django.conf.urls import url
from .views import (
    event_list,
    event_create,
    event_detail,
    event_update,
    event_delete,
)

urlpatterns = [
    url(r'^events/', event_list, name="list"),
    url(r'^host/event/create/$', event_create, name='create'),
    url(r'^e/(?P<slug>[\w-]+)/$', event_detail, name='detail'),
    url(r'^host/event/(?P<slug>[\w-]+)/edit/$', event_update, name='update'),
    url(r'^e/(?P<slug>[\w-]+)/delete/$', event_delete),
]
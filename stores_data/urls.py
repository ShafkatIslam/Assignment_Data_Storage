from django.conf.urls import url
from stores_data import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'store_data'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^mainreg/$', views.mainreg, name='mainreg'),
    url(r'^parent/$', views.parent, name='parent'),
    url(r'^child/$', views.child, name='child'),
    url(r'^(?P<id>[0-9]+)/parent_edit/$', views.parent_edit, name='parent_edit'),
    url(r'^(?P<id>[0-9]+)/child_edit/$', views.child_edit, name='child_edit'),
    url(r'^(?P<id>[0-9]+)/delete_user/$', views.delete_user, name='delete_user'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
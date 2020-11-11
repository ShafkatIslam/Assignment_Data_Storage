from django.conf.urls import url
from stores_data import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from .views import UserAPIView,UserSpecificAPIView,NewParentCreateView,NewChildCreateView
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('userlist/', views.userList, name="userlist"),
    path('users/<int:pk>/', views.userIndividualView, name="users"),
    path('user-create/parent/', views.parentUserCreate, name="user-create-parent"),
    path('user-create/child/', views.childUserCreate, name="user-create-child"),
    path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
    path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
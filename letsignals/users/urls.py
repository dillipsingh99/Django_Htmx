from django.urls import path
from users import views

urlpatterns = [
    path('list/', views.listProfile, name='listProfile'),
    path('create/', views.createProfile, name='createProfile'),
    path('<int:pk>/edit/', views.editProfile, name='editProfile'),
    path('setcookie', views.setcookie),
    path('getcookie', views.showcookie),
    path('update', views.updating_cookie),
    path('delete', views.deleting_cookie),
]
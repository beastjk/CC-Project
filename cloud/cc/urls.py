from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('profilee/',views.ProfileViewset.as_view({ 'get': 'list', 'post': 'create'})),
    path('profileDetails/', views.ProfileViewset.as_view(
        {'post': 'create'})),
    path('profilee/<str:pk>/', views.profilee),
    path('profileupdate/<str:pk>/', views.ProfileViewset.as_view(
        {'put': 'update'})),
    path('profiledelete/<str:pk>',views.profiledelete),
    path('loginn',views.login),
    path('register',views.index)
]



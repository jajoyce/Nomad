from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"), 
    path('about/', views.About.as_view(), name = "about"), 
    path('accounts/signup/', views.Signup.as_view(), name = "signup" ),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('nomads/', views.ProfileList.as_view(), name="profile_list"),
    path('nomads/<int:pk>', views.ProfileDetail.as_view(), name="profile_detail"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    
]
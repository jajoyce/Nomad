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
    path('posts/new', views.PostCreate.as_view(), name='post_create'),
    path('posts/new/<int:pk>', views.PostCityCreate.as_view(), name='post_city_create'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
    path('create-profile/', views.ProfileCreate.as_view(), name='create_profile'),
    path('loggedin/', views.Loggedin.as_view(), name="loggedin"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"), 
    path('about/', views.About.as_view(), name = "about"), 
    path('accounts/signup/', views.Signup.as_view(), name = "signup" ),
    path('loggedin/', views.Loggedin.as_view(), name="loggedin"),
    path('nomads/', views.ProfileList.as_view(), name="profile_list"),
    path('nomads/new', views.ProfileCreate.as_view(), name="profile_create"),
    path('nomads/<int:pk>', views.ProfileDetail.as_view(), name="profile_detail"),
    path('nomads/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),
    path('nomads/<int:pk>/delete', views.ProfileDelete.as_view(), name='profile_delete'),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/new', views.PostCreate.as_view(), name='post_create'),
    path('posts/new/<int:pk>', views.PostCityCreate.as_view(), name='post_city_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
    path('comments/<int:pk>/update', views.CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete', views.CommentDelete.as_view(), name='comment_delete'),
    path('accounts/update/', views.UserUpdate.as_view(), name = "user_update" ),
]
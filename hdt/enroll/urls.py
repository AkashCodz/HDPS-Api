from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('result/', views.result, name='result'),
]
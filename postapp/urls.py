from django.urls import path 
from .import views 
from postapp.views import post_list,post_list_user
from django.contrib.auth.views import LogoutView
from django.conf import settings




urlpatterns = [
    path('',post_list.as_view(), name='post_list'),
    path('postlu',post_list_user.as_view(), name='post_list_user'),
    path('home',views.home,name = 'home'),
    path('base/',views.base , name = 'base'),
    path('login/',views.login , name = 'login'),
    path('register/',views.register , name = 'register'),
    path('logout/',LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),

]

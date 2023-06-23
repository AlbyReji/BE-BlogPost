from django.urls import path 
from .import views 
from postapp.views import post_list,post_list_user



urlpatterns = [
    path('',post_list.as_view(), name='post_list'),
    path('postlu',post_list_user.as_view(), name='post_list_user'),
    path('home',views.home,name = 'home'),
    path('base/',views.base , name = 'base'),
    # path('Post/',post_list.as_view(), name='post_list'),
    path('login/',views.login , name = 'login'),
    path('register/',views.register , name = 'register'),
    path('logout/', views.logout_view, name='logout'),

]

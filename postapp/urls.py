from django.urls import path 
from .import views 
from postapp.views import post_list



urlpatterns = [
    path('',post_list.as_view(), name='post_list'),
    path('home',views.home,name = 'home'),
    path('base/',views.base , name = 'base'),
    # path('Post/',post_list.as_view(), name='post_list'),
    path('login/',views.login , name = 'login'),
    path('register/',views.register , name = 'register'),

]

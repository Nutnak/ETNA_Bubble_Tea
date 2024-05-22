from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name="register"),
    path('orders', views.orders, name="orders"),
    path('profile', views.profilePage, name="profile"),
    path('logout',views.logout, name= 'logout'),
    path('updateUser',views.updateUser, name= "updateUser"),
    path('addBubbletea', views.addBubbletea, name='addBubbletea'),
    # path('deleteBubbletea', views.deleteBubbletea, name='deleteBubbletea')
]

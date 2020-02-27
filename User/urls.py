from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('', views.home, name = "home"),
    path('login', views.login_page, name='login'),
    # path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]
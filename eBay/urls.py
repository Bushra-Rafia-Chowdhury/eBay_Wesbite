from django.contrib import admin
from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='Home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('additem/', views.additem, name="additem"),
]

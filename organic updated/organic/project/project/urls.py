"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login/', views.login),
    path('reg/', views.user_reg),
    path('user_home/', views.user_home),
    path('admin_home/', views.admin_home),
    path('admin_add_product/', views.admin_add_products),
    path('admin_view_product/', views.admin_view_product),
    path('admin_delete/', views.delete_product),
    path('admin_update/', views.update_product),
    path('admin_view_user/', views.admin_view_user),
    path('admin_delete_user/', views.delete_user),
    path('admin_approve_user/', views.approve_user),
    path('user_view_product/', views.user_view_product),
    path('update_profile/', views.updateprofile),
    path('view_history/', views.view_history),
    path('booked_pro/', views.booked_pro),
    path('user_add_product/', views.user_add_products),
    path('payment/', views.payment),
    path('admin_booked_pro/', views.admin_booked_pro),
    path('feedback/', views.feedback),
    path('dboy_reg/', views.dboy_reg),
    path('admin_view_dboy/', views.admin_view_dboy),
    path('admin_delete_dboy/', views.delete_dboy),
    path('admin_approve_dboy/', views.approve_dboy),
    path('dboy_home/', views.dboy_home),
    path('dboy_booked_pro/', views.dboy_booked_pro),
    
 
]

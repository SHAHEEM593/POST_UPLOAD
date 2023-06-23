from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from demo import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('new_post/', views.new_post, name='new_post'),
    path('', views.home, name='home'),
] 

"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from posts.views import home,create_post,update_post,delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('create_post/', create_post, name="create_post"),
    path('update_post/<int:pk>', update_post, name="update_post"),
    path('delete_post/<int:pk>', delete_post, name="delete_post"),
    # path('news', news, name="news"),
]

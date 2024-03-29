"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.views.static import serve
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('blog.urls')),
    #path('blog', include('blog.urls')),
    #path('videos', include('videos.urls')),
    #path('home', include('home.urls')),
    path('',include('home.urls')),




]


# Serve the favicon - Keep for later
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#urlpatterns += [
 #   path('favicon.ico', serve, {
  #          'path': 'favicon.ico',
   #         'document_root': os.path.join(BASE_DIR, 'blog/static'),

    #    }
   # ),
#]


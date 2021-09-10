"""finance_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import urls
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
import rest_framework
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^$', get_swagger_view(title='Finance Cite API')),
    path('api/auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api/finance_manager/', include('finance_manager.urls')),
]

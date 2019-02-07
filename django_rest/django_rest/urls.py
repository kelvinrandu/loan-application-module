"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api import views
from api.database import conn, create_tables

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/', views.index),
    url(r'^api/personal/$', views.personal_details),
    url(r'^api/personal/retrieve/$', views.retrieve_details),
    url(r'^api/personal/update/(?P<user_id>\d+)/$', views.update_details),
    url(r'^api/personal/delete/(?P<user_id>\d+)/$', views.delete_details),
    url(r'^api/address/$', views.address_details),
    url(r'^api/address/retrieve/$', views.retrieve_address_details),
    url(r'^api/address/update/(?P<address_id>\d+)/$', views.update_address_details),
    url(r'^api/address/delete/(?P<address_id>\d+)/$', views.delete_address_details),
   
]

# run migrations during startup
create_tables()

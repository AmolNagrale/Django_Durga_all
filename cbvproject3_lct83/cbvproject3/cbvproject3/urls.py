"""cbvproject3 URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
# from django.conf.urls import url
from cbvapp3 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CompanyListView.as_view(), name='companies'),
    re_path(r'^(?P<pk>\d+)/$', views.CompanyDetailview.as_view()),
    # re_path(r'^(?P<pk>\d+)/$', views.CompanyDetailview.as_view(), name='detail'), 
    #path('', views.CompanyDetailview.as_view()), # page is not redirect on the perticular site
    # path('create/', views.CompanyCreateView.as_view()),
    # url(r'^update/(?P<pk>\d+)/$', views.CompanyUpdateView.as_view()), 
    # url(r'^delete/(?P<pk>\d+)/$', views.CompanyDeleteView.as_view()), 
 ]
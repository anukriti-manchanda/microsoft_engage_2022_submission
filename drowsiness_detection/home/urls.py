from django.contrib import admin
from django.urls import path,include
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#customising the django-admin
admin.site.site_header='Welcome to the Data Portal'
admin.site.site_title='Data Portal'
admin.site.index_title='Data Portal'
urlpatterns = [
    path('', views.index, name='index'),
    path('getStarted', views.getStarted, name='getStarted'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('creator', views.creator, name='creator'),
    path('dashboard', views.dashboard, name='dashboard')
    
]
urlpatterns += staticfiles_urlpatterns()
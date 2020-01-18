"""DR111 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from DR111app import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('alumni/',views.alumlogin, name='alumni'),
    path('clg/',views.clglogin,name='clg'),
    path('collegeLogin/', views.postclglogin, name='postclglogin'),
    path('dte/',views.dtlogin,name='dte'),
    path('postsign/',views.postsign),
    path('logout/',views.logout,name="log"),
    path('Cancel/',views.Cancel,name='cancel'),
    path('register/',views.register,name='register'),
    path('postsignup/',views.postsignup,name='postsignup'),

   path('password_reset/$',views.password_reset,name="password_reset"),
    path('password_reset/done/$',views.password_reset_done,name="password_reset_done"),
    path('password_reset/confirm/(?p<uidb64>[\w-]+)/(?p<token>[\w-]+)/$',views.password_reset_confirm,name="password_reset_confirm"),
    path('password_reset/complete/$',views.password_reset_complete,name="password_reset_complete"),
   # path('',include('django.contrib.auth.urls')),
    path('academic/',views.academic,name="academic"),
    path('professional/',views.professional,name="prof"),
    path('alumniregistration/',views.register,name="alumniregistration_1"),
    path('dir/',views.dir,name="dir"),
    path('collsearch/',views.collsearch,name="collsearch"),
    path('postcollsearch/', views.postcollsearch, name="postcollsearch"),
  #  path('password_reset/$',auth_views.password_reset,name="password_reset"),
  #  path('password_reset/done/$',auth_views.password_reset_done,name="password_reset_done"),
   # path('password_reset/confirm/(?p<uidb64>[\w-]+)/(?p<token>[\w-]+)/$',auth_views.password_reset_confirm,name="password_reset_confirm"),
   # path('password_reset/complete/$',auth_views.password_reset_complete,name="password_reset_complete"),
   # path('',include('django.contrib.auth.urls'))
]

"""DOMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from orders.models import Collected
from orders import views as my_order
from orders import views
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
)

# NOTE: This project was written for Django 1.x, which exposed the auth views
# (`auth.login`, `auth.logout`, `auth.password_change`) as plain functions.
# Those were removed in Django 1.11 / 2.1 and replaced with class-based views.
# Django 2.2.17 keeps the deprecated `url()` alias, so the regex routes below
# are left unchanged; only the three auth views are modernised here.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_order.index, name='home'),
    url(r'^orders$', my_order.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    url(r'^order/new/$', my_order.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),
    url(r'^collect_now$', my_order.eggcollections, name='collect_now'),
    url(r'^collect$', my_order.collections, name='collections'),
    url(r'^collected$', my_order.collections, name='collections'),
    url(r'^collected/delete/(?P<collected_id>\d+)/$', my_order.collectiondestroy, name='delete'),
    url(r'^users/login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^users/logout/$', LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^users/change_password/$', login_required(PasswordChangeView.as_view(success_url='/', template_name='change_password.html')), name='change_password'),
]
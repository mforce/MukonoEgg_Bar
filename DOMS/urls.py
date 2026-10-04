"""DOMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

This project was originally written for Django 1.x, which used the function
based `url()` helper with regex routes. `url()` was deprecated in Django 3.1
and removed in 4.0; routes here use `path()` (path converters) where possible
and `re_path()` only where a regex is genuinely needed.
"""
from django.urls import path, re_path
from django.contrib import admin
from orders.models import Collected  # noqa: F401  (used by templates/admin.py historically)
from orders import views as my_order
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    # Order list / detail / CRUD
    path('', my_order.index, name='home'),
    path('orders', my_order.index, name='home'),
    path('order/new/', my_order.new, name='new'),
    re_path(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    re_path(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    re_path(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),

    # Egg collection tracking
    path('collect_now', my_order.eggcollections, name='collect_now'),
    path('collect', my_order.collections, name='collections'),
    path('collected', my_order.collections, name='collections'),
    re_path(r'^collected/delete/(?P<collected_id>\d+)/$', my_order.collectiondestroy, name='delete'),

    # Auth views (function-based auth.login/logout/password_change were removed
    # in Django 1.11/2.1; these are the class-based equivalents).
    path('users/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('users/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path(
        'users/change_password/',
        login_required(PasswordChangeView.as_view(success_url='/', template_name='change_password.html')),
        name='change_password',
    ),
]
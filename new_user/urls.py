"""
new_user URL Configuration
"""
from django.conf.urls import url
from new_user import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.AuthorView.as_view())),
    url(r'^thanks/$', views.ThanksView.as_view()),
]

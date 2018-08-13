from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # 主页
    url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='learning_logs/index.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
]

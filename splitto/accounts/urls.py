from django.urls import include, re_path
from . import views

app_name = 'accounts'

urlpatterns =[
    re_path(r'^signup/$', views.signup_view.as_view(), name = 'signup'),
    re_path(r'^login/$', views.login_view.as_view(), name = 'login')
]

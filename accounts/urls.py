"""MyBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from accounts import views
from accounts.views import SignUpView, Signin, Homepage, Homepagemain, SignOutView,change_password


from django.contrib.auth import views as auth_views


urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    path("signin/",Signin.as_view(),name='login'),
    path("home/",Homepage.as_view(),name="home"),
    path("homepage/", Homepagemain, name="homemain"),
    path("logout/", SignOutView, name="logout"),
    path("changepassword/", change_password, name='change_password'),


path("password-reset/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',subject_template_name='accounts/password_reset_subject.txt'),
     name="password_reset"),
path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
     name="password_reset_done"),
path("password-reset-confirm/<uidb64>/<token>/",
     auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
     name="password_reset_confirm"),
path("password-reset-complete/",
     auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
     name="password_reset_complete"),

]


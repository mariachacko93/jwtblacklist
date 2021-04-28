from django.urls import path
from . import views
from app.views import LogoutAllView,LogoutView
  
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name ='hello'),
    #  path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logoutall/', LogoutAllView.as_view(), name='auth_logout_all'),

    path('logout/', LogoutView, name='auth_logout'),

]




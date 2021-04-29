from django.urls import path
from . import views
from app.views import LogoutView,LogoutAllView
  
urlpatterns = [
    path('api/login/', views.HelloView.as_view(), name ='hello'),
    path('api/logoutall/', LogoutAllView, name='auth_logout_all'),
    path('api/logout/', LogoutView, name='auth_logout'),

]




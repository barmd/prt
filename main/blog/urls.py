from django.urls import path
from . import views

urlpatterns = [
    #--------------Posts
    path('', views.home, name = "home"),
    path('contact/', views.ContactPageView.as_view(), name = "contact"),

]
from django.urls import path
from . import views
urlpatterns = [path('', views.home, name="home"),
                path('tenant/<str:pk_test>/', views.tenant, name="tenant"),
                path('landlord/<str:pk>/', views.landlord,  name="landlord"),
                path('rent/<str:pk>/', views.rent, name="rent"),
               path('register/', views.registerPage, name="register"),
               path('login/', views.loginPage, name="login"),
               path('logout/', views.logoutUser, name="logout"),

               ]

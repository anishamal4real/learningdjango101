from django.urls import path, include
from . import views
from .views import  TenantAPIView, TenantDetailAPIView, TenantListGenericAPIView,TenantDetailGenericAPIView, LandlordAPIView, LandlordDetailAPIView, LandlordDetailGenericAPIView, LandlordListGenericAPIView, RentDetailGenericAPIView


urlpatterns = [path('', views.home, name="home"),
               path('tenant/<str:pk_test>/', views.tenant, name="tenant"),
               path('landlord/<str:pk>/', views.landlord,  name="landlord"),
               path('rent/<str:pk>/', views.rent, name="rent"),
               path('register/', views.registerPage, name="register"),
               path('login/', views.loginPage, name="login"),
               path('logout/', views.logoutUser, name="logout"),
               path('tenantapi/', TenantAPIView.as_view()),
               path('tenantapidetail/<int:pk>', TenantDetailAPIView.as_view()),
               path('generic/tenant/', TenantListGenericAPIView.as_view()),
               path('generic/tenantdetail/<int:pk>/', TenantDetailGenericAPIView.as_view()),
               path('landlordapi/', LandlordAPIView.as_view()),
               path('landlordapidetail/<int:pk>', LandlordDetailAPIView.as_view()),
               path('generic/landlord/', LandlordListGenericAPIView.as_view()),
               path('generic/landlorddetail/<int:pk>/', LandlordDetailGenericAPIView.as_view()),
               path('generic/rentdetail/<int:pk>/', RentDetailGenericAPIView.as_view()),
               
               ]

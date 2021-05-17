from django.urls import path,include
from . import views
from .views  import TenantViewSet, LandlordViewSet, TenantAPIView, TenantDetailAPIView, TenantListGenericAPIView, TenantDetailGenericAPIView 
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('tenant',TenantViewSet, basename='tenant')
urlpatterns = [path('', views.home, name="home"),
                path('tenant/<str:pk_test>/', views.tenant, name="tenant"),
                path('landlord/<str:pk>/', views.landlord,  name="landlord"),
                path('rent/<str:pk>/', views.rent, name="rent"),
               path('register/', views.registerPage, name="register"),
               path('login/', views.loginPage, name="login"),
               path('logout/', views.logoutUser, name="logout"),
               path('viewset',include(router.urls)),
               path('viewset/<int:pk>',include(router.urls)),
                path('tenantapi/',TenantAPIView.as_view()),
                path('tenantapidetail/<int:pk>', TenantDetailAPIView.as_view()),
                 path('generic/tenant/', TenantListGenericAPIView.as_view()),
    path('generic/tenantdetail/<int:pk>/', TenantDetailGenericAPIView.as_view())

                #path('generic/article/', TenantListGenericAPIView.as_view()),
                #path('generic/detail/<int:pk>/', TenantDetailGenericAPIView.as_view())
            
 

               ]

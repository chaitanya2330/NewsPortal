from django.urls import path,include
from .views import UserViewset,NewsDetailViewSet,NewsViewApi
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
router = DefaultRouter()
router.register('crud', UserViewset, basename='user')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/news/',NewsViewApi.as_view()),
    path('api/news/<int:pk>',NewsDetailViewSet.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]



from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet

from .views.auth_view import LoginView, LogoutView
from .views.world_view import WorldViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'worlds', WorldViewSet, basename='world')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]

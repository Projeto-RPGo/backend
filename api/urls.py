from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, CharacterViewSet, RaceViewSet, NPCViewSet, AffiliationViewSet, DomainViewSet, SkillViewSet, MCFViewSet, SpecializationViewSet, MaxDomViewSet

from .views.auth_view import LoginView, LogoutView
from .views.world_view import WorldViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'worlds', WorldViewSet, basename='world')
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'race', RaceViewSet, basename='race')
router.register(r'domain', DomainViewSet, basename='domain')
router.register(r'npc', NPCViewSet, basename='npc')
router.register(r'affiliation', AffiliationViewSet, basename='affiliation')
router.register(r'skill', SkillViewSet, basename='skill')
router.register(r'mcf', MCFViewSet, basename='mcf')
router.register(r'specialization', SpecializationViewSet, basename='specialization')
router.register(r'maxdom', MaxDomViewSet, basename='maxdom')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]

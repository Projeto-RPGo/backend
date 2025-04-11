from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (AffiliationViewSet, CharacterViewSet, DomainViewSet,
                       ItemViewSet, MaxDomViewSet, MCFViewSet, NPCViewSet,
                       QuestViewSet, RaceViewSet, SkillViewSet,
                       SpecializationViewSet, UserViewSet, WorldViewSet)

from .views.auth_view import LoginView, LogoutView

router = DefaultRouter()

router.register(r'affiliation', AffiliationViewSet, basename='affiliation')
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'domain', DomainViewSet, basename='domain')
router.register(r'item', ItemViewSet, basename='item')
router.register(r'maxdom', MaxDomViewSet, basename='maxdom')
router.register(r'mcf', MCFViewSet, basename='mcf')
router.register(r'npc', NPCViewSet, basename='npc')
router.register(r'quest', QuestViewSet, basename='quest')
router.register(r'race', RaceViewSet, basename='race')
router.register(r'skill', SkillViewSet, basename='skill')
router.register(r'specialization', SpecializationViewSet,
                basename='specialization')
router.register(r'users', UserViewSet, basename='user')
router.register(r'worlds', WorldViewSet, basename='world')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('domain/<int:domain_id>/details', DomainViewSet.get_domain_details, name="get_domain_details"),
    path('domain/<int:domain_id>/character/<int:character_id>/', DomainViewSet.get_character_domain_data, name="get_character_domain_data"),
]

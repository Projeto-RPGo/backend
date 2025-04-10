from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Character
from ..models.character import MaxDomMastery, MCFMastery, SkillMastery, SpecializationMastery
from ..models.domain import Domain
from ..models.maxdom import MaxDom
from ..models.mcf import MCF
from ..models.skill import Skill
from ..models.specialization import Specialization
from ..serializers.domain_serializer import DomainSerializer


class DomainViewSet(viewsets.ModelViewSet):

    queryset = Domain.objects.all().order_by('-name')
    serializer_class = DomainSerializer

    def list(self, request):
        """
        Handles the GET request to list all domains.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the list of domains.
        """

        return super().list(request)

    def create(self, request):
        """
        Handles the HTTP POST request to create a new domain.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: The HTTP response object containing the created domain.
        """

        return super().create(request)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP GET request to retrieve a single domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to retrieve.
        Returns:
            Response: The HTTP response object containing the domain.
        """

        return super().retrieve(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PUT request to update a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to update.
        Returns:
            Response: The HTTP response object containing the updated domain.
        """

        return super().update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP PATCH request to partially update a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to update.
        Returns:
            Response: The HTTP response object containing the updated domain.
        """

        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Handles the HTTP DELETE request to delete a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk, *args, **kwargs)

    @api_view(["GET"])
    def get_domain_details(request, domain_id):
        try:
            domain = Domain.objects.get(pk=domain_id)
        except Domain.DoesNotExist:
            return Response({"error": "Domínio não encontrado."}, status=404)

        skills = Skill.objects.filter(
            domain1=domain) | Skill.objects.filter(domain2=domain)
        habilidades = [
            {
                "id": skill.skill_id,
                "nome": skill.name,
                "slots": [skill.slot1, skill.slot2, skill.slot3, skill.slot4, skill.slot5],
            }
            for skill in skills
        ]

        mcfs = MCF.objects.filter(skill_id__in=skills)
        mcf = [
            {
                "id": mcf.mcf_id,
                "idHab1": mcf.skill_id.skill_id,
                "nome": mcf.name,
                "slots": [mcf.slot1, mcf.slot2, mcf.slot3, mcf.slot4, mcf.slot5],
            }
            for mcf in mcfs
        ]

        especializacoes = Specialization.objects.filter(skill_id__in=skills)
        especializacoes_list = [
            {
                "id": esp.specialization_id,
                "idHab1": esp.skill_id.skill_id,
                "nome": esp.name,
                "descricao": esp.description,
            }
            for esp in especializacoes
        ]

        maxdoms = MaxDom.objects.filter(skill_id__in=skills)
        dominio_max = (
            {
                "id": maxdom.max_dom_id,
                "idHab1": maxdom.skill_id.skill_id,
                "nome": maxdom.name,
                "descricao": maxdom.description,
            }
            if maxdoms.exists() else None
        )

        response_data = {
            "habilidades": habilidades,
            "mcf": mcf,
            "especializacoes": especializacoes_list,
            "dominioMax": dominio_max,
        }

        return Response(response_data)
    
    @api_view(["GET"])
    def get_character_domain_data(request, domain_id, character_id):
        try:
            domain = Domain.objects.get(pk=domain_id)
            character = Character.objects.get(pk=character_id)
        except (Domain.DoesNotExist, Character.DoesNotExist):
            return Response({"error": "Domínio ou Personagem não encontrado."}, status=404)

        # Skills relacionadas ao domínio que o personagem possui
        skill_mastery = SkillMastery.objects.filter(player_id=character, skill_id__domain1=domain) | \
                        SkillMastery.objects.filter(player_id=character, skill_id__domain2=domain)

        habilidades = []
        skill_ids = []
        for mastery in skill_mastery:
            skill = mastery.skill_id
            skill_ids.append(skill.skill_id)
            slots = [skill.slot1, skill.slot2, skill.slot3, skill.slot4, skill.slot5][:mastery.slot]
            habilidades.append({
                "id": skill.skill_id,
                "nome": skill.name,
                "slots": slots
            })

        # MCFs relacionados
        mcf_mastery = MCFMastery.objects.filter(player_id=character, mcf_id__skill_id__in=skill_ids)
        mcf = []
        for mastery in mcf_mastery:
            mcf_obj = mastery.mcf_id
            mcf.append({
                "id": mcf_obj.mcf_id,
                "idHab1": mcf_obj.skill_id.skill_id,
                "nome": mcf_obj.name,
                "slots": [mcf_obj.slot1, mcf_obj.slot2, mcf_obj.slot3, mcf_obj.slot4, mcf_obj.slot5][:mastery.slot]
            })

        # Especializações relacionadas
        specialization_mastery = SpecializationMastery.objects.filter(
            player_id=character, specialization_id__skill_id__in=skill_ids)
        especializacoes = []
        for esp in specialization_mastery:
            esp_obj = esp.specialization_id
            especializacoes.append({
                "id": esp_obj.specialization_id,
                "idHab1": esp_obj.skill_id.skill_id,
                "nome": esp_obj.name,
                "descricao": esp_obj.description
            })

        # MaxDom relacionado (assumindo apenas um por habilidade)
        maxdom_mastery = MaxDomMastery.objects.filter(
            player_id=character, mcf_id__skill_id__in=skill_ids).first()
        dominio_max = None
        if maxdom_mastery:
            maxdom = maxdom_mastery.mcf_id
            dominio_max = {
                "id": maxdom.max_dom_id,
                "idHab1": maxdom.skill_id.skill_id,
                "nome": maxdom.name,
                "descricao": maxdom.description
            }

        response_data = {
            "habilidades": habilidades,
            "mcf": mcf,
            "especializacoes": especializacoes,
            "dominioMax": dominio_max,
        }

        return Response(response_data)

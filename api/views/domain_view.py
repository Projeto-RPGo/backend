from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.skill import Skill
from ..models.mcf import MCF 
from ..models.specialization import Specialization
from ..models.maxdom import MaxDom
from ..models.domain import Domain
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

    def retrieve(self, request, pk=None):
        """
        Handles the HTTP GET request to retrieve a single domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to retrieve.
        Returns:
            Response: The HTTP response object containing the domain.
        """

        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        """
        Handles the HTTP PUT request to update a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to update.
        Returns:
            Response: The HTTP response object containing the updated domain.
        """

        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        """
        Handles the HTTP PATCH request to partially update a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to update.
        Returns:
            Response: The HTTP response object containing the updated domain.
        """

        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        """
        Handles the HTTP DELETE request to delete a domain.
        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the domain to delete.
        Returns:
            Response: The HTTP response object containing a success message.
        """

        return super().destroy(request, pk)
    
    @api_view(["GET"])
    def get_domain_details(request, domain_id):
        try:
            domain = Domain.objects.get(pk=domain_id)
        except Domain.DoesNotExist:
            return Response({"error": "Domínio não encontrado."}, status=404)
        
        skills = Skill.objects.filter(domain1=domain) | Skill.objects.filter(domain2=domain)
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
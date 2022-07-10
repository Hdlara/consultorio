from django.db import transaction
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response

from ..serializers import PacienteSerializer

from ...models import Paciente, Exame


class PacienteViewSet(ListCreateAPIView):
    """
    Lista e cria pacientes
    """
    serializer_class = PacienteSerializer

    def get_queryset(self):

        params = self.request.query_params
        queryset = Paciente.objects.all().order_by('id')

        if 'id' in params:
            queryset = Paciente.objects.filter(
                id=params['id']
            )

        elif 'nome' in params:
            queryset = Paciente.objects.filter(
                nome__icontains=params['nome']
            ).order_by("nome")

        elif 'altura' in params:
            queryset = Paciente.objects.filter(
                altura=params['altura']
            )

        return queryset

    @method_decorator(transaction.atomic)
    def post(self, request):

        paciente = request.data['id']

        if Paciente.objects.filter(
                id=paciente,
        ).exists():
            serializer = PacienteSerializer(
                instance=request.data,
                data=request.data,
                context={
                    "id": paciente,
                }
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(status=status.HTTP_200_OK)
        else:
            serializer = PacienteSerializer(
                data=request.data,
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)


class PacienteDelete(DestroyAPIView):
    """
    deleta paciente
    """

    def destroy(self, request, **kwargs):
        id = self.kwargs['id']

        if Paciente.objects.filter(
                id=id,
        ).exists():
            self.perform_destroy(id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {
                    "erro": "Não foi possivel encontrar nenhum paciente com o"
                            " id informado."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def perform_destroy(self, id):
        exames = Exame.objects.filter(paciente=id)
        exames.delete()
        paciente = Paciente.objects.filter(id=id)
        paciente.delete()


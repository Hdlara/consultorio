from django.db import transaction
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response

from ..serializers import ExameSerializer
from ...models import Exame, Paciente


class ExameViewSet(ListCreateAPIView):
    """
    Lista e cria exame
    """
    serializer_class = ExameSerializer

    def get_queryset(self):

        params = self.request.query_params
        queryset = Exame.objects.all()

        if 'id_exame' in params:
            queryset = Exame.objects.filter(
                id_exame=params['id_exame']
            )

        elif 'altura_menor' in params:
            id = Paciente.objects.filter(
                altura__lte=params['altura_menor']
            ).values_list('id')

            queryset = Exame.objects.filter(paciente__in=id)

        elif 'altura_maior' in params:
            id = Paciente.objects.filter(
                altura__gte=params['altura_maior']
            ).values_list('id')

            queryset = Exame.objects.filter(paciente__in=id)

        return queryset

    @method_decorator(transaction.atomic)
    def post(self, request):

        exame = request.data['id_exame']

        if Exame.objects.filter(
                id_exame=exame,
        ).exists():
            serializer = ExameSerializer(
                instance=request.data,
                data=request.data,
                context={
                    "id": exame,
                }
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(status=status.HTTP_200_OK)
        else:
            serializer = ExameSerializer(
                data=request.data,
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)


class ExameDelete(DestroyAPIView):
    """
    deleta exame
    """

    def destroy(self, request, **kwargs):
        id = self.kwargs['id']

        if Exame.objects.filter(
                id_exame=id,
        ).exists():
            exames = Exame.objects.filter(id_exame=id)
            exames.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {
                    "erro": "Não foi possivel encontrar nenhum exame com o"
                            "id informado."
                },
                status=status.HTTP_400_BAD_REQUEST
            )


from django.urls import path

from .views import (
    ExameViewSet,
    PacienteViewSet,
    ExameDelete,
    PacienteDelete
)

urlpatterns = [
    path(
        'exame',
        ExameViewSet.as_view(),
    ),

    path(
        'paciente',
        PacienteViewSet.as_view(),
    ),

    path(
        'excluir-exame/<str:id>',
        ExameDelete.as_view(),
    ),

    path(
        'excluir-paciente/<str:id>',
        PacienteDelete.as_view(),
    )
]

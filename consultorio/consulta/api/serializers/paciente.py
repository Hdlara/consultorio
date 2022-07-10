from rest_framework import serializers

from ...models import Paciente


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = (
         'id', 'nome', 'altura', 'endereco'
        )

    def update(self, instance, dados_validados):
        id = self.context.get("id")

        paciente = Paciente.objects.filter(
            id=id,
        )

        paciente_atualizado = paciente.update(**dados_validados)

        return paciente_atualizado

    def create(self, dados_validados):
        return Paciente.objects.create(**dados_validados)

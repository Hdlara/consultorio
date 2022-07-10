from rest_framework import serializers

from ...models import Exame


class ExameSerializer(serializers.ModelSerializer):
    data = serializers.DateField(format="%d/%m/%Y", source="data_exame")
    altura = serializers.SerializerMethodField()
    nome_paciente = serializers.SerializerMethodField()

    class Meta:
        model = Exame
        fields = (
            'id_exame', 'nome_profissional', 'nome_paciente',
            'paciente', 'altura', 'data'
        )

    def get_altura(self, obj):
        return obj.paciente.altura

    def get_nome_paciente(self, obj):
        return obj.paciente.nome

    def update(self, instance, dados_validados):
        id = self.context.get("id")

        exame = Exame.objects.filter(
            id_exame=id,
        )

        paciente_atualizado = exame.update(**dados_validados)

        return paciente_atualizado

    def create(self, dados_validados):
        return Exame.objects.create(**dados_validados)
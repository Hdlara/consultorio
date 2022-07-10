from django.db import models


class Paciente(models.Model):
    id = models.SmallAutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    endereco = models.CharField(max_length=100)


class Exame(models.Model):
    id_exame = models.SmallAutoField(primary_key=True, editable=False)
    nome_profissional = models.CharField(max_length=100)
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE
    )
    data_exame = models.DateField()
    create_at = models.DateField(auto_now_add=True)

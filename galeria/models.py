from django.db import models


class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Fotografia [nome=(self.nome)]'

# use o comando makemigrations para definir a estrutura de como sera sua tabela no banco de dados 
# python manage.py makemigrations

# use o comando para criar sua tabela no banco de dados
# python manage.py migrate
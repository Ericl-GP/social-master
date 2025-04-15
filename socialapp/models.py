from django.db import models

# Create your models here.
class Post(models.Model):
    usuario = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'@{self.usuario} - {self.hora.strftime("%d/%m/%Y %H:%M")}'
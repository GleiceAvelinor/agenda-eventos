from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    date = models.DateTimeField(verbose_name='Data e Hora')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Criado em')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

def get_data_evento(self):
    return self.date.strftime('%Y-%m-%d %H:%M')
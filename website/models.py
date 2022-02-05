from django.db import models

# Create your models here.
class Contato(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField("e-mail", max_length=254)
    endereco = models.CharField("endereço", max_length=100)
    mensagem = models.TextField()
    noticias = models.BooleanField("notícias")

    class Meta:
        verbose_name = ("contato")
        verbose_name_plural = ("contatos")

    def __str__(self):
        return self.nome



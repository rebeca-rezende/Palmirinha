from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__ (self):
        return self.nome
    

    

class Receita(models.Model):
    
    GRAU_DIFICULDADE = [
        ('F', 'Fácil'),
        ('M', 'Moderado'),
        ('D', 'Difícil')
    ]

    nome = models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=2000)
    modo_de_preparo = models.TextField(max_length=8000)
    grau_de_dificuldade = models.CharField(max_length=10, choices=GRAU_DIFICULDADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__ (self):
        return self.nome
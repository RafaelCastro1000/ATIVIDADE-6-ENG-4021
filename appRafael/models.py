from django.db import models

class Trofeus(models.Model): #Definição do modelo Trofeus que é uma classe de python que herda de models.Model(Base para todos os modelos)
  nome = models.CharField(max_length = 50) # É um campo de caracter(string) que representa o nome do trófeu tendo um tamanho máximo de 50 caracteres
  data = models.DateField() # É um campo de data que representa quando o troféu foi conquistado
  descricao = models.TextField() #É um campo de texto que representa detalhes da conquista

class Jogadores(models.Model):  #Definição do modelo Jogadores que é uma classe de python que herda de models.Model(Base para todos os modelos)
  nome = models.CharField(max_length = 50)   # É um campo de caracter(string) que representa o nome do jogador tendo um tamanho máximo de 50 caracteres
  posicao = models.CharField(max_length=50)   # É um campo de caracter(string) que representa o posição do jogador tendo um tamanho máximo de 50 caracteres
  numero_camisa = models.CharField(max_length=3)  # É um campo de caracter(string) que representa o número de camisa tendo um tamanho máximo de 3 caracteres
  caracteristicas = models.TextField()   #É um campo de texto que representa caracteristicas do jogador
  aprovação = models.BooleanField() #É um campo que armazena um valor boolenao (True ou False) e representa de o jogador é aprovado pelo usuário ou não


from django.contrib import admin   #Importa o módulo admin
from .models import Trofeus,Jogadores  #Importa os dois modelos criados

admin.site.register(Trofeus) #Regitra o modelo Trofeus para ser utilizado na interface administrativa do Django
admin.site.register(Jogadores) #Regitra o modelo Jogadores para ser utilizado na interface administrativa do Django



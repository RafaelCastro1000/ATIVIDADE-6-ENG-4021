from django.shortcuts import render,redirect #Importa as funções render,redirect que são utilizadas para renderizar templates HTML e redirecionar o usuário para outras páginas.
from .models import Trofeus,Jogadores #Importar os modelos necessários



def home(request): #Função que apresenta a página principal so site pro usuário
    # Obtém todos os objetos Trofeus e Jogadores do banco de dados
    trofeus = Trofeus.objects.all()
    jogadores = Jogadores.objects.all()
    context = {"trofeus": trofeus, "jogadores":jogadores}  # Cria um dicionário de contexto com as informações obtidas
    return render(request, "home.html", context=context) # Renderiza o template "home.html" com o contexto fornecido


def create_trofeus(request): #  Função para criar um troféu no sistema
    if request.method == "POST": # Verifica se o método da requisição é POST
       # Cria um novo objeto Trofeus com base nos dados da requisição
        Trofeus.objects.create(nome=request.POST["nome"], 
                               data=request.POST["data"],
                               descricao=request.POST["descricao"])
        return redirect("home") # Redireciona para a página "home" após a criação

    return render(request, "trofeus_form.html") # Renderiza o template "trofeus_form.html" para exibir o formulário de criação de trofeus

def create_jogadores(request):# Função para criar um jogador no sistema
    if request.method == "POST": # Verifica se o método da requisição é POST
        if "aprovação" not in request.POST: # Verifica se o campo de "aprovação" está presente nos dados da requisição
            aprovação = False
        else:
            aprovação = True
        # Cria um novo objeto Jogadores com base nos dados da requisição
        Jogadores.objects.create(nome=request.POST["nome"],
                             posicao=request.POST["posicao"],
                             numero_camisa=request.POST["numero_camisa"],
                             caracteristicas=request.POST["caracteristicas"],
                                 aprovação=aprovação)
        return redirect("home")  # Redireciona para a página "home" após a criação

    return render(request, "jogadores_form.html") # Renderiza o template "jogadores_form.html" para exibir o formulário de criação de jogadores

def update_trofeu(request, trofeu_id): #Função que atualiza o troféu especifico do banco de dados
    trofeu = Trofeus.objects.get(id=trofeu_id) # Recupera o objeto do troféu a partir do trofeu_id fornecido

    trofeu.data = trofeu.data.strftime('%Y-%m-%d') # Converte a data do troféu para o formato correto (string no formato 'YYYY-MM-DD')
  
    if request.method == "POST": # Verifica se o método da requisição é POST
        # Atualiza os campos do troféu com base nos dados da requisição
        trofeu.nome = request.POST["nome"]
        trofeu.data = request.POST["data"]
        trofeu.descricao = request.POST["descricao"]
        trofeu.save() # Salva as alterações no banco de dados
        return redirect("home")  # Redireciona para a página "home" após a atualização

    return render(request, "trofeus_form.html", context={"trofeu": trofeu})  # Renderiza o template "trofeus_form.html" para exibir o formulário de edição do troféu e passa o objeto do troféu como contexto para o template
    


def delete_trofeu(request, trofeu_id): # Função com que exclui um troféu especifico do banco de dados
    trofeu = Trofeus.objects.get(id=trofeu_id) # Recupera o objeto do troféu a partir do trofeu_id fornecido
    if request.method == "POST": # Verifica se o método da requisição é POST
        if "confirm" in request.POST: # Verifica se o campo "confirm" está presente nos dados da requisição
            trofeu.delete() # Remove o troféu do banco de dados
            return redirect("home")  # Redireciona para a página "home" após a exclusão


    return render(request, "delete_trofeu.html", context={"trofeu": trofeu})# Renderiza o template "delete_trofeu.html" para exibir a página de confirmação de exclusão do troféu e passa o objeto do troféu como contexto para o template


def update_jogador(request, jogador_id): #Função que atualiza o jogador especifico do banco de dados
    jogador = Jogadores.objects.get(id=jogador_id)  # Recupera o objeto do jogador a partir do jogador_id fornecido
  
    if request.method == "POST":  # Verifica se o método da requisição é POST
        # Atualiza os campos do jogador com os dados enviados no formulário
        jogador.nome = request.POST["nome"] 
        jogador.posicao = request.POST["posicao"]
        jogador.numero_camisa = request.POST["numero_camisa"]
        jogador.caracteristicas = request.POST["caracteristicas"]
        if "aprovação" not in request.POST: # Verifica se o campo "aprovação" não está presente nos dados da requisição
            jogador.aprovação = False
        else:
            jogador.aprovação = True
        jogador.save()# Salva as alterações no objeto do jogador no banco de dados
        return redirect("home") # Redireciona para a página "home" após a atualização

    return render(request, "jogadores_form.html", context={"jogador": jogador})# Renderiza o template "jogadores_form.html" para exibir o formulário de edição do jogador e passa o objeto do jogador como contexto para o template
    

def delete_jogador(request, jogador_id): # Função com que exclui um jogador especifico do banco de dados
   jogador = Jogadores.objects.get(id=jogador_id) # Recupera o objeto do jogador a partir do jogador_id fornecido
   if request.method == "POST":  #Verifica se o método da requisição é POST
        if "confirm" in request.POST: # Verifica se o campo "confirm" está presente nos dados da requisição
            jogador.delete() # Exclui o jogador
            return redirect("home")  # Redireciona para a página "home" após a exclusão

   return render(request, "delete_jogadores.html", context={"jogador": jogador})  # Renderiza o template "delete_jogadores.html" para exibir o formulário de confirmação de exclusão e passa o objeto do jogador como contexto para o template
   






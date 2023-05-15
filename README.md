# ATIVIDADE-6-ENG-4021

1) Gerar a SECRET_KEY através do código vindo dos comandos abaixo:
python
import secrets
secrets.token_urlsafe(32)

2)Criar um app e incluir no instaled apps:
python3 manage.py startapp <nomedoapp>
  
3)Criar a pasta templates:
Adicionar o link dela em setting.py usando os.path.join(BASE_DIR,'templates') 
  
4)Fazer as migrações dos modelos:
python manage.py makemigrations nome_do_app
python manage.py migrate
  
5)Criar um superusuário para acessar o admin:
python manage.py createsuperuser
  
  
  

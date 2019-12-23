## INSTALAÇÃO

Requisitos: Docker, docker-compose

### Execução

Dentro da pasta do projeto, rode o comando `docker-compose up -d` para instalar os contêineres. 

Vá tomar um café...

Instalados os catêineres, execute `docker-compose exec web python manage.py migrate` para realizar as migrations. Após as migrations, para criar um super usuário, rode `docker-compose exec web python manage.py createsuperuser`

Acesse `localhost:8000` no browser.
## INSTALAÇÃO

Requisitos: Docker, docker-compose

### Execução

Dentro da pasta do projeto, rode o comando `docker-compose up -d` para instalar os contêineres, logo após, execute `docker-compose exec web python manage.py migrate` para realizar as migrations.
Vá tomar um café...
Após as migrations, para criar um super usuário, rode `docker-compose exec web python manage.py createsuperuser`

Acesse `localhost:8000` no browser.
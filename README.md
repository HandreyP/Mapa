Project Map, created to learn a framework Django.

Step-by-Step:
//criar ambiente virtual:

python -m venv "nome_do_ambiente_virtual"
cd "nome_do_ambiente_virtual"
cd scripts
activate

//instalar o django:
pip install django

cd "endereço_da_pasta_onde_sera_criado_o_projeto

django-admin startproject "nome_projeto"
django admin startapp "nome_da_aplicacao"

//verificar funcionalidade:
python manage.py runserver

//criar admin:
python manage.py createsuperuser

//fazer as migrações
python manage.py makemigrations
//aplicar as migraçoções:
python manage.py migrate

//fazer as instalações dos programas:
pip install -r requirements.txt
aplicar as instalações:
pip freeze

//abrir o projeto no visualstudio:
code .

// Abrir um terminal para testes em shell
python manage.py shell

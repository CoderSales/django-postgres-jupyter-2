python -m venv .venv
source .venv/Scripts/activate
pip install psycopg2
pip install Django
django-admin startproject dj_jupyter .
django-admin startapp nbs
project/settings.py INSTALLED_APPS 'nbs'
----------------------------------------
pip install jupyter
-------------------

app/views.py
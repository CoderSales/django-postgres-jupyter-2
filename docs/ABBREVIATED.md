python -m venv .venv
source .venv/Scripts/activate
pip install psycopg2
pip install Django
django-admin startproject dj_jupyter .

-------------------------------------------------
IGNORE NEXT 2 LINES:
-------------------------------------------------
django-admin startapp Not_Specified
project/settings.py INSTALLED_APPS 'Not_Specified'
----------------------------------------
pip install jupyter
-------------------


------------------------------
IGNORE NEXT LINE NOT USED YET:
------------------------------
app/views.py
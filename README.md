# django-postgres-jupyter-2
see django-postgres-jupyter for docs


## Mac setup

Use Python **3.14**. The existing `.venv` on this Mac already uses it.
Run these commands from this repository folder:

```bash
if [ -n "${VIRTUAL_ENV:-}" ]; then deactivate; fi
while [ "${CONDA_SHLVL:-0}" -gt 0 ]; do conda deactivate || break; done
if [ ! -d .venv ]; then
    uv venv --python 3.14 --seed .venv
fi &&
source .venv/bin/activate &&
python -c 'import sys; assert sys.version_info[:2] == (3, 14), "This project needs Python 3.14; the existing environment uses another version."' &&
python -m pip install -r requirements.txt &&
python -m pip check &&
python manage.py check
```

In VS Code, select this repository's `.venv/bin/python`. Creation is skipped
when `.venv` already exists. On later visits, activate it with
`source .venv/bin/activate`.

The dependencies use Django 6.1.1 and include `psycopg2-binary` for local
PostgreSQL development without a compiler or `pg_config`, plus Pillow for image
uploads. A PostgreSQL server and matching database settings are still needed
to run the app against PostgreSQL.

`Pipfile` is the dependency source; `Pipfile.lock` and `requirements.txt` are
resolved together. After changing dependencies, regenerate both files:

```bash
uvx --from pipenv==2026.8.0 pipenv lock &&
uvx --from pipenv==2026.8.0 pipenv requirements > requirements.txt
```

### Manual pip install and freeze

With `.venv` active, install the saved packages:

```bash
python -m pip install -r requirements.txt
```

After intentional package changes and testing, save a manual snapshot:

```bash
python -m pip freeze > requirements.txt
```

These are `pip install` and `pip freeze`, run through the selected Python.
`freeze` overwrites `requirements.txt` and does not update `Pipfile.lock`.
Use the Pipfile workflow above to keep this repository's dependency files aligned.

## Assistance reference

Environment setup, dependency fixes, and documentation were assisted by
[ChatGPT](https://chatgpt.com/) and [OpenAI Codex](https://openai.com/codex/).

## Earlier tutorial references and setup notes


# [django-postgres-jupyter](https://github.com/CoderSales/django-postgres-jupyter/blob/main/README.md)

Links:
------
- [gist](https://gist.github.com/codingforentrepreneurs/76e570d759f83d690bf36a8a8fa4cfbe)
- [code](https://www.codingforentrepreneurs.com/blog/use-django-in-jupyter/)
- [tutorial](https://youtu.be/t3mk_u0rprM?t=110)


- [completed tutorial django psql](https://youtu.be/unFGJhIvHU4?t=82)

- [psql jupyter](https://youtu.be/CDa1Xz-leQQ?t=8)

- GitHub [django-postgres](https://github.com/CoderSales/django-postgres)


References:
-----------
- [ABBREVIATED.md](https://github.com/CoderSales/django-postgres/blob/main/docs/ABBREVIATED-POST-RUN.md)

Dependencies:
-------------
jupyter


Note:
-----
cfehome should be project name

python -m venv .venv

source .venv/Scripts/activate

pip install psycopg2

pip install Django

django-admin startproject project .

django-admin startapp app

project/settings.py INSTALLED_APPS 'app' app/views.py

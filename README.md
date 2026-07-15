# Mukono Egg Bar Django Order Management System

## About this application

Created by **MarkDawn**[_`PyDawn`_]....some of the content in this project was provided by **_Inzamul Haque_**.
##### Framework: Django 5.2 LTS (originally 1.10.1; modernised)
##### Language : Python 3.13

## Getting started (development)

The project runs on **Python 3.13** inside a virtualenv. Python 3.13 is provided
via [pyenv](https://github.com/pyenv/pyenv) so the system Python (3.14) is not
touched.

```fish
# one-time: install pyenv (if not already installed)
git clone --depth=1 https://github.com/pyenv/pyenv.git ~/.pyenv
# add to ~/.config/fish/config.fish:
#   set -gx PYENV_ROOT $HOME/.pyenv
#   fish_add_path $PYENV_ROOT/bin
#   pyenv init - fish | source

# inside the project directory
pyenv install 3.13.14       # only if not already installed
python -m venv .venv
source .venv/bin/activate.fish
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
#    -> http://127.0.0.1:8000/
```

### Configuration via environment variables (optional)

`DOMS/settings.py` reads from environment so production values don't need code
edits:

- `DJANGO_SECRET_KEY` — override the dev secret key (required in production).
- `DJANGO_DEBUG` — set to `0` to disable debug mode.
- `DJANGO_ALLOWED_HOSTS` — space-separated list of allowed hosts.

Create an admin user:

```fish
python manage.py createsuperuser
```

### Notes on the modernisation to Django 5.2 LTS / Python 3.13

The original code targeted Django 1.10 / Python 3.6 and would not import on
modern Python. The following were updated so it runs on a current, supported
LTS stack:

- `requirements.txt` — target Django **5.2.16 LTS**, whitenoise 6.9, and
  django-widget-tweaks 1.5.1 (transitive deps left to the resolver).
- `DOMS/urls.py` — replaced the removed `url()` helper with `path()` and
  `re_path()`; the function-based auth views (`auth.login`, `auth.logout`,
  `auth.password_change`) are already class-based from the 2.2 baseline.
- `DOMS/settings.py` — migrated `STATICFILES_STORAGE` to the Django 4.2+ `STORAGES`
  dict; removed the deprecated `USE_L10N` setting; added `DEFAULT_AUTO_FIELD`
  (`BigAutoField`); read `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` from
  environment variables; `BASE_DIR` is now a `pathlib.Path`.
- `orders/models.py` — `Order.delivery_date` now passes the `timezone.now`
  callable (not its import-time result), fixing the fixed-default warning.
- `orders/migrations/*.py` — six historical migrations imported
  `django.utils.timezone.utc`, removed in Django 5.0; switched to
  `datetime.timezone.utc`. A new migration `0009` records the `BigAutoField`
  `id` changes and the corrected `delivery_date` default.
- `orders/templates/*.html` — `{% load staticfiles %}` (removed in Django 3.0)
  replaced with `{% load static %}`. The two logout links in `layout.html` are
  now POST forms, since `LogoutView` requires POST as of Django 5.0.

### Earlier baseline (kept for history)

Before the LTS upgrade the project was made runnable on Python 3.9 + Django
2.2.17 by replacing the removed function-based auth views, dropping the
`DjangoWhiteNoise` wrapper, and replacing the deleted
`whitenoise.django.GzipManifestStaticFilesStorage`. See the git history for
that baseline commit.


## Features
- Add order
- Add egg collection data
- Export Order (pdf, csv)
- Edit / Delete Order
- Search Order
- Print Invoice
- Cool & Easy interface

## Applicability
Can be customised to be used in Restaurants, Cafe, etc


### Contact me 
Twitter: @xxendiwala <br>
Email: mxxendiwala@gmail.com, mcdawnking@gmail.com

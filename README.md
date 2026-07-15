# Mukono Egg Bar Django Order Management System

## About this application

Created by **MarkDawn**[_`PyDawn`_]....some of the content in this project was provided by **_Inzamul Haque_**.
##### Framework: Django 2.2.17 (originally 1.10.1; modernised to run on modern Python)
##### Language : Python 3.9

## Getting started (development)

The project runs on **Python 3.9** inside a virtualenv. Python 3.9 is provided
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
pyenv install 3.9.18        # only if not already installed
python -m venv .venv
source .venv/bin/activate.fish
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
#    -> http://127.0.0.1:8000/
```

Create an admin user:

```fish
python manage.py createsuperuser
```

### Notes on the modernisation

The original code targeted Django 1.10 / Python 3.6 and would not import on
modern Python. The following were updated so it runs on Python 3.9 + Django
2.2.17:

- `DOMS/urls.py` — replaced the removed function-based auth views
  (`auth.login`, `auth.logout`, `auth.password_change`) with their
  class-based equivalents (`LoginView`, `LogoutView`, `PasswordChangeView`).
- `DOMS/wsgi.py` — removed the `DjangoWhiteNoise` wrapper (deleted in
  whitenoise 4.x); static files are now served through `WhiteNoiseMiddleware`.
- `DOMS/settings.py` — replaced the removed
  `whitenoise.django.GzipManifestStaticFilesStorage` with the DEBUG-aware
  storage selection (default storage in dev,
  `whitenoise.storage.CompressedManifestStaticFilesStorage` in prod) and added
  `STATIC_ROOT`.
- `requirements.txt` — trimmed to the dependencies the code actually imports
  (`Django`, `django-widget-tweaks`, `whitenoise`) plus Django 2.2's own
  runtime deps. The previous file bundled an unrelated stack (Wagtail, Kivy,
  pandas/matplotlib, Windows-only wheels, dev tooling) and could not install on
  modern Python.


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

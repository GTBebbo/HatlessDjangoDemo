# Django Demo

## Setup

First setup your virtual environment:

```
python -m venv .venv
```

Activate the virtual environment and install requirements

```
# Windows
.venv\Scripts\activate.bat
pip install -r requirements.txt
# Linux
.venv\bin\activate
pip install -r requirements.txt
```

## Running the server

Migrate the database, run tests, run the server:

```
python manage.py migrate
python manage.py test
python manage.py runserver 80
```
# STAC-Inventory

A Django project for STAC inventory management system.

## Local Deployment

1. Create a new virtual environment and activate it.

```console
$ pyvenv inv
$ source inv/bin/activate
```

2. Install dependencies.

```console
$ pip install -r requirements.txt
```

3. Create the database.

```console
$ python manage.py migrate
```

6. Launch the development server:

```console
$ python manage.py runserver
```

7. Visit the url http://127.0.0.1:8000/ on your browser.
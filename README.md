# django-rest-boilerplate #

An easy to use project boilerplate for Django(2.2.4) and Django Rest Framework(3.10.2) that follows best practices.

## Features ##

- [Django Rest Framework](https://www.django-rest-framework.org/) for REST capabilities.
- [Django Rest Auth](https://django-rest-auth.readthedocs.io/) To manage authorization as REST.
- [Python Decouple](https://github.com/henriquebastos/python-decouple) environment variables for sensitive data.
- [Django Cors Headers](https://github.com/adamchainz/django-cors-headers) for handling the server headers required for Cross-Origin Resource Sharing (CORS).

## Quickstart ##

Make sure you have [virtualenv installed](https://virtualenv.pypa.io/). Then install the requirements in your virtualenv:

    $(env) pip install -r requirments.txt

Create `__init__.py` inside settings folder and put the environment you want to run (development/production):
    
    from .development import *  # runs development settings

Migrate your database
   
    ./manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    ./manage.py runserver

### Settings for Production ###

Sensitive data is store in a .env file that is not uploaded to the repository for security reasons, there's a .env.example for examples:

    SECRET_KEY=your-secret-key
    DB_NAME=your-db-name
    DB_USER=your-db-user-name
    DB_PASSWORD=your-db-password
    DB_HOST=your-host(e.g. 127.0.0.1)

### TODO ###
 - Everything OK for now.
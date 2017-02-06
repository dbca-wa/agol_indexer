# agol_indexer

### Production Libraries
- django version 1.10.5

### Development
- django_gulp - 2.5.0 (https://pypi.python.org/pypi/django-gulp/2.5.0)

##### NPM - 3.10.10
- browser-sync: 2.18.7
- concurrently: 3.1.0
- gulp:3.9.1
- gulp-concat: 2.6.1
- gulp-sass: 3.1.0
- gulp-util: 3.0.8
- run-sequence: 1.2.2

### Front End Libraries (in repo)
- semantic-ui (css & js) - 2.2.7
- jquery - 3.1.1


## Installation

Create a new virtualenv and install required libraries using `pip`:

    pip install -r requirements.txt

## Environment variables

This project uses **django-confy** to set environment variables (in a `.env` file).
The following variables are required for the project to run:

    DATABASE_URL="postgis://USER:PASSWORD@HOST:5432/DATABASE_NAME"

Variables below may also need to be defined (context-dependent):

    SECRET_KEY="ThisIsASecretKey"
    DEBUG=True

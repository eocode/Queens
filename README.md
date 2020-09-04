<div align="center">
  <img width="64" src="https://image.flaticon.com/icons/svg/862/862737.svg" alt="Queens">
  <h3 align="center">Queens</h3>
  <p align="center">
    Solve Eight Queens Puzzle
  </p>
  <p align="center">
    <a href="https://github.com/eocode/Queens/blob/master/LICENSE">
      	<img src="https://img.shields.io/badge/License-BSD3-blue.svg"  alt="license badge"/>
    </a>
    <a href="https://travis-ci.org/eocode/Queens">
        <img src="https://img.shields.io/travis/eocode/Queens.svg?label=flask-queens" alt="Build Status">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/pypi/pyversions/Flask.svg?style=flat-square"  alt="python badge">
    </a>
  </p>
</div>

## Description Tasks

1. Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens
2. Iterate over N and store the solutions in postgres using SQLAlchemy
3. Write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
5. Setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

## Based on a cookiecutter technique

This microservice has been generated since a cookiecutter development by eocode (me) for this project with the next command 

```bash
cookiecutter https://github.com/ActivandoIdeas/Cookiecutter-Flask
```

See the details here: https://github.com/ActivandoIdeas/Cookiecutter-Flask

You can base your next developments on that template or contribute to improve it

## Dependencies

* Flask
* python-dotenv
* Flask-sqlalchemy
* Psycopg2
* Pytest
* Flask-migrate
* Bootstrap
* Pytest
* Coverage
* Setuptools
* Numpy

## Features

* N Queens Problem
* Dockerized
* Travis-CI
* Flask Blueprints
* Divide envs
* Extensible
* PostgreSQL

## Development tools

* Pycharm - IDE
* Black - Code format

## How to clone

You can clone this repository

    git clone https://github.com/eocode/queens

## Development configuration

Rename .env.example to .env file

And add your configuration

## Use on local
To install this project just type

Create virtual enviroment:

    $ python -m venv env

Active your enviroment

Install dependencies

    $ pip install -r app/requirements/prod.txt
    $ pip install -r app/requirements/test.txt

Run the project

    $ flask run
    
## Install app

If you want to install the app use

```bash
python setup.py develop
```
    
## Dockerized app

Start app

```bash
docker compose up -d
```

Stop app

```bash
docker compose down
```

Rebuild app

```bash
docker-compose up -d --build
```

Access to command line interface

```bash
docker exec -it flask-app bash
```

## Run migrations

By default migrations foldar has been add to .gitignore

Open Terminal

```bash
docker exec -it flask-app bash
```

Init database migrations

```bash
flask db init
```

Generate migrations

```bash
flask db migrate
```

Run migrations

```bash
flask db upgrade
```

Show more commands

```bash
flask db
```

## Prepare enviroments

Configure for test, execute sqlite db

```bash
python app/enviroment.py test
```

Configure for dev or production, execute data in postgresql instance

```bash
python app/enviroment.py prod
```

## Run tests

On Docker

```bash
docker-compose exec queens-app pytest
```

or only

```bash
pytest
```

## Coverage of project

```bash
coverage report
coverage html
```

## File structure

* **core** (Flask configurations project)
  * **init** (Base config app)
  * **database** (Settings for SQLAlchemy)
  * **settings** (Injectable settings app)
* **modules** Project modules
  * **queens** (Main blueprint Flask module) 
* **migrations** (Database version app - Don't tracked)
* **tests** (Test of project)

## Preview

Your image project previews

## How to contribute

* See contributting file

https://github.com/eocode/Queens/blob/master/CONTRIBUTTING.md

# License

View in https://github.com/eocode/Queens/blob/master/LICENSE

<div align="center">
  <img width="64" src="https://image.flaticon.com/icons/svg/862/862737.svg" alt="Queens">
  <h3 align="center">Queens</h3>
  <p align="center">
    Solve N Queens Puzzle
  </p>
  <p align="center">
    <a href="https://github.com/eocode/Queens/blob/master/LICENSE">
      	<img src="https://img.shields.io/badge/License-BSD3-blue.svg"  alt="license badge"/>
    </a>
    <a href="https://travis-ci.org/eocode/Queens">
        <img src="https://img.shields.io/travis/eocode/Queens.svg?label=flask-queens" alt="Build Status">
    </a>
    <a href="https://codecov.io/gh/eocode/Queens">
        <img src="https://codecov.io/gh/eocode/Queens/branch/master/graph/badge.svg" />
    </a>
  </p>
</div>

## Summary<!-- omit in toc -->
- [Demo N Queens](#demo-n-queens)
- [The n*n queens problem](#the-nn-queens-problem)
- [Project solution](#project-solution)
  - [File structure](#file-structure)
  - [The algorithm](#the-algorithm)
  - [Results of algorithm](#results-of-algorithm)
    - [For 14*14 board](#for-1414-board)
    - [For 15*15 board](#for-1515-board)
- [How it is build?](#how-it-is-build)
  - [Dependencies](#dependencies)
  - [Features](#features)
  - [Development tools](#development-tools)
- [How to use](#how-to-use)
  - [Based on a cookiecutter technique](#based-on-a-cookiecutter-technique)
  - [How to clone](#how-to-clone)
  - [Development configuration](#development-configuration)
  - [Use on local](#use-on-local)
  - [Install app](#install-app)
  - [Dockerized app](#dockerized-app)
  - [Run migrations](#run-migrations)
  - [Prepare enviroments](#prepare-enviroments)
  - [Run tests](#run-tests)
  - [Ejecute coverage report](#ejecute-coverage-report)
- [How to contribute](#how-to-contribute)
- [License](#license)

# Demo N Queens

Main view, choise n board and simulate the game, if it has been calculated, the answer show in moment

<div align="center">
  <img src="/app/img/demo.png" alt="Demo Queens">
</div>

Next view all possible solutions

<div align="center">
  <img src="/app/img/demo_2.png" alt="Demo Queens">
</div>

# The n*n queens problem

Problem details: https://en.wikipedia.org/wiki/Eight_queens_puzzle

1. Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens
2. Iterate over N and store the solutions in postgres using SQLAlchemy
3. Write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
5. Setup Travis CI (or similar) for your public GitHub repo to run the tests automatically


# Project solution

## File structure

* **core** (Flask configurations project)
  * **envs** (Configuration environments)
  * **requirements** (Project dependencies)
  * **extensions** (Instance for access to db in modules)
  * **img** (Images of project)
  * **init** (Base config app)
  * **database** (Settings for SQLAlchemy)
  * **settings** (Injectable settings in app)
* **modules** Project modules
  * **queens** (Main blueprint with clean implementation) 
    * **algorithms** (Switch algorithm)
    * **connections** (Utilities for database connection)
    * **simulation** (Core elements of the project)
    * **solutions** (Manage results of the algorithm)
    * **utilities** (Project tilities)
* **migrations** (Database version app - Don't tracked)
* **labs** (Codding problem and test solutions to pass in module queens, this folder won't pass for testing)
* **tests** (Test of project)

## The algorithm

You can see the algorithm in ``modules/queens/algorithms``

This is the solution Number 4, see all solutions in ``labs folder``

```python
def __n_queens(self, board, col, positions):
    """Last N Queens Algorithm
    Development by @eocode
    Version 4
    """
    if col == len(board):
        self.__solutions.add_solution(
            board, len(self.__solutions.get_solutions()) + 1
        )
        return True

    for row in range(len(board)):
        if row in positions.keys() and col in positions[row]:
            apply, values = Queen.attack(row, col, copy.deepcopy(positions))
            if apply:
                board[row][col] = 1
                self.__n_queens(board, col + 1, values)
                board[row][col] = 0
```

## Results of algorithm

### For 14*14 board

Test algorithm with n boards > 8

<div align="center">
  <img src="/app/img/res_2.png" alt="14*15 Queens">
</div>

Time in minutes

<div align="center">
  <img src="/app/img/res_2_time.png" alt="14*14 Queens">
</div>

### For 15*15 board

<div align="center">
  <img src="/app/img/res_1.png" alt="15*15 Queens">
</div>

Time in minutes

<div align="center">
  <img src="/app/img/res_1_time.png" alt="15*15 Queens Time">
</div>

# How it is build?

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

* N Queens Problem algorithm with labs to analyze problem
* Dockerized (test and development envs)
* Travis-CI and codecov integration
* Flask Blueprints
* TDD (Test Driven Development) Testing with 10 n*n and every core part of the app for up coverage
* Divide envs 
* Extensible
* PostgreSQL
* Paginate results for show solutions
* Web application for view solutions and interact
* Show list of board with all solutions procesed
* Simulate n*n boards until 10 minutes

## Development tools

* Pycharm - IDE
* Black - Code format

# How to use

## Based on a cookiecutter technique

This microservice has been generated since a cookiecutter development by eocode (me) for this project with the next command 

```bash
cookiecutter https://github.com/ActivandoIdeas/Cookiecutter-Flask
```

See the details here: https://github.com/ActivandoIdeas/Cookiecutter-Flask

You can base your next developments on that template or contribute to improve it

 
```bash
# Only execute this (keep the code cleen)
black .
```

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

## Ejecute coverage report

```bash
coverage run -m pytest
coverage report
coverage html
```

# How to contribute

* See contributting file

https://github.com/eocode/Queens/blob/master/CONTRIBUTTING.md

# License

View in https://github.com/eocode/Queens/blob/master/LICENSE

# Setup and Runnig this project

## Setting up Python environment

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with <br />

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
python3 -m venv venv
```

That will create a new folder `venv` in your project directory. Next activate it with this command on mac/linux:

```
source venv/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

## Setting up postgresql database

### Install Postgresql **_Linux_**

```
sudo apt-get install libpq-dev python-dev
```

```
sudo apt-get install postgresql postgresql-contrib
```

### Install Postgresql **_Windows_**

[Tutorial PostgreSQL windows](https://www.postgresqltutorial.com/install-postgresql/)

### Setup Database and User in PostgreSQL

Based on these settings in [settings.py](/src/project/project/settings.py)

```python
DATABASES = {
    "default": {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ecommerce",
        "USER": "ecomgraph",
        "PASSWORD": "ecomgraph",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

Follow the following steps

1. Enter into postgres admin terminal
    - **Linux** : `sudo su - postgres`
2. create database
    - **Linux** : `createdb ecommerce`
3. create user called ecomgraph with password ecomgraph using the `createuser` command of postgresql
    - **Linux** : `createuser -P`
4. enter psql shell and grant all permissions to this user.
    - **All OS** : `psql`

```SQL
grant all privileges on database ecommerce to ecomgraph
```

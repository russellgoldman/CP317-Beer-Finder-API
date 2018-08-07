# API for CP317-Beer-Finder application

## Installation
Clone this Git repository and unfreeze the requirements.txt file to gain access to a venv depencency folder.

```shell
source venv/bin/activate
pip3 install -r requirements.txt
```

## Updating Dependencies
After updating dependencies on your venv, you **MUST** re-freeze the requirements.txt file.
```shell
source venv/bin/activate
pip3 freeze > requirements.txt
```

## Updating Models.py
```shell
flask-sqlacodegen --flask --outfile models.py postgres://hatfznjj:hcAJJv82Hpnt6tjc2OH5oIzFTuQmd6N4@stampy.db.elephantsql.com:5432/hatfznjj
```
After running this, remove the following in models.py:
- t_pg_stat_statements table

Then if migrations folder is missing, run:
```shell
python3 manage.py db init
python3 manage.py db migrate
```

Otherwise just run:
```shell
python3 manage.py db migrate
```
##

## Heroku Servers
There are two Heroku servers, one for staging (test server) and another for production.

- Staging: https://beer-finder-app-stage.herokuapp.com/
- Production: https://beer-finder-app.herokuapp.com/

## Updating the Heroku Servers
To push to the staging server, commit to the API GitHub repository and then enter...

```shell
git push stage master
```

To push to the production server, commit to the API GitHub repository and then enter...

```shell
git push pro master
```

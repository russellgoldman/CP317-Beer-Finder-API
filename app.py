from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from models includes db
from models import *
app = Flask(__name__)

POSTGRES = {
    'user': 'hatfznjj',
    'pw': 'hcAJJv82Hpnt6tjc2OH5oIzFTuQmd6N4',
    'db': 'hatfznjj',
    'host': 'stampy.db.elephantsql.com',
    'port': '5432',
}

#flask-sqlacodegen --flask --outfile models.py postgres://hatfznjj:hcAJJv82Hpnt6tjc2OH5oIzFTuQmd6N4@stampy.db.elephantsql.com:5432/hatfznjj
#sqlacodegen --outfile c:/models.py postgres://hatfznjj:hcAJJv82Hpnt6tjc2OH5oIzFTuQmd6N4@stampy.db.elephantsql.com:5432/hatfznjj
#postgres://hatfznjj:hcAJJv82Hpnt6tjc2OH5oIzFTuQmd6N4@stampy.db.elephantsql.com:5432/hatfznjj
# connection to DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

@app.route('/')
def hello():
    sql = """SELECT * from home_beer"""
    result = db.engine.execute(sql)
    arr = []
    for row in result:
        arr.append(row)

    return ','.join(str(i) for i in arr)
    db_session.remove()

def search(filters):
    #search returns a list of accuracy percentages for each beer based on a set of filters that are passed in
    sql = """SELECT * from home_beer"""
    result = db.engine.execute(sql)
    beers = []
    accuracies = []
    for row in result:
        beers.append(row)

    numFilters = 0
    for filter in filters:
        if filter != "":
            numFilters+=1

    for beer in beers:
        for filter in filters:
            i = 0
            accuracy = 0
            if beer[i] == filter and filter!="":
                accuracy+=1
            accuracies.append(accuracy/numFilters)

    return accuracies

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# enable debug mode
app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()

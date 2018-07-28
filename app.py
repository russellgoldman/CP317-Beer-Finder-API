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
    #search section
    sql = """SELECT * from home_beer"""
    result = db.engine.execute(sql)
    beers = []
    for row in result:
        beers.append(row)

    accuracies = []
    #accuracies is a list of the percentage matching to the filters
    #if beer #2 of 4 matches 3/5 of the filters passed in,
    #accuracies will be [0,0.6,0,0]

    numFilters = 0
    for filter in filters:
        if filter != "":
            numFilters+=1

    for beer in beers:
        #for now, beer.containerType and beer.taste do not exist
        i = 0
        accuracy = 0
        if beer.alcoholVolume == filters[0] and filters[0]!="":
            accuracy+=1
        if beer.brand == filters[1] and filters[1]!="":
            accuracy+=1
        if beer.bodyType == filters[2] and filters[2] != "":
            accuracy+=1
        if beer.containerType == filters[3] and filters[3] != "":
            accuracy+=1
        if beer.taste == filters[4] and filters[4] != "":
            accuracy+=1
        accuracies.append(accuracy/numFilters)

    #sort section
    high = 1
    sortedBeers = []

    #for each level of accuracy, from high to low,
    #checks all beers to see if it matches the level of accuracy and appends to sortedBeers
    #upgrade would be to skip over beers that are of a higher accuracy
    for i in range(numFilters,-1,-1):
        j = 0
        for beer in beers:
            if accuracies[j] == i/numFilters:
                sortedBeers.append(beer)

    return sortedBeers
    db_session.remove()


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/test')
def test():
    sql = """SELECT * from home_beer"""
    result = db.engine.execute(sql)
    arr = []
    for row in result:
        arr.append(row)
    return str(arr[0].id)

# enable debug mode
app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()

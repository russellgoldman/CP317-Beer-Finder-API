from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from models includes db
from models import *
from functions import searchFunc
from functions import top_picksFunc
import json
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

class Beer(object):
    alcoholVolume = 0.0
    brandName = ""
    bodyTypeName = ""
    containerType = []
    taste = []
    def __init__(self, alcoholVolume, brandName, bodyTypeName, containerType, taste):
        self.alcoholVolume = alcoholVolume
        self.brandName = brandName
        self.bodyTypeName = bodyTypeName
        self.containerType = containerType
        self.taste = taste

@app.route('/')
def hello():
    sql = """SELECT * from home_beer"""
    result = db.session.execute(sql)
    arr = []
    for row in result:
        arr.append(row)

    return ','.join(str(i) for i in arr)
    db_session.remove()

@app.route('/search/results', methods = ['POST'])
def search():
    filters = request.get_json()
    #search section
    #sql = """SELECT * from home_beer"""
    beers = HomeBeer.query.all()
    beersList = []

    for beer in beers:
        alcoholVolume = beer.alcoholVolume
        brandName = beer.brand.brandName
        bodyTypeName = beer.bodyType.bodyTypeName
        containerTypes = []
        containerTypeLookups = HomeBeerContainerType.query.all()
        for key in containerTypeLookups:
            if key.beer_id == beer.id:
                containerTypes.append(key.containertype.containerTypeName)
        tasteTypes = []
        tasteTypeLookups = HomeBeerTaste.query.all()
        for key in tasteTypeLookups:
            if key.beer_id == beer.id:
                tasteTypes.append(key.taste.tasteName)
        """
        print(alcoholVolume)
        print(brandName)
        print(bodyTypeName)
        print(containerTypes)
        print(tasteTypes)
        """
        newBeer = Beer(alcoholVolume, brandName, bodyTypeName, containerTypes, tasteTypes)
        beersList.append(newBeer)

    results = json.dumps(searchFunc(beersList, filters), default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return results
    db_session.remove()


@app.route('/<name>+<color>')
def hello_name(name, color):
    return "Hello {}{}!".format(color, name)

@app.route('/test')
def test():
    sql = """SELECT * from home_beer"""
    result = db.engine.execute(sql)
    arr = []
    for row in result:
        arr.append(row)
    return str(arr[0].id)
@app.route('/test2')
def test2():
    sql = """SELECT * from home_beer"""
    result = db.engine.execute(sql)
    arr = []
    for row in result:
        arr.append(row)

    return str(top_picksFunc(arr,db))
# enable debug mode
app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()

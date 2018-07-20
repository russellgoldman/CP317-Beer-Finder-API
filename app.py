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

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# enable debug mode
app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()

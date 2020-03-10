from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir,'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Happy_days(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=False)
    content = db.Column(db.String(200), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class Happy_daysSchema(ma.Schema):
    class Meta:
        fields = ( 'id','title', 'content' )

happy_daysschema = Happy_daysSchema()
happy_daysschema = Happy_daysSchema(many=True)

#endpoint to create new happy days
@app.route('/happy_days', methods = ["POST"])
def add_happy_days():
    title = request.json['title']
    content = request.json['content']

    new_happy_days = Happy_days(title, content)

    db.session.add(new_happy_days)
    db.session.commit()

    happy_days = Happy_days.query.get(new_happy_days.id)

    return happy_daysschema.jsonify(happy_days)

# Endpoint to query all guides
@app.route("/happy_days", methods=["GET"])
def get_happy_days():
    all_happy_days = Happy_days.query.all()
    result = happy_daysschema.dump(all_happy_days)
    return jsonify(result)


#endpoint for querying a single item
@app.route("/happy_days/<id>", methods = ["PUT"])
def get_happy_day(id):
    happy_days = Happy_days.query.get(id)
    return happy_daysschema.jsonify(happy_days)



if __name__ == '__main__':
    app.run(debug=True) 

from flask import Flask, request,jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tatoeba@localhost/tatoeba'

class Sentences(db.Model):
    __tablename__ = 'sentences'
    id = db.Column(db.Integer, primary_key = True)
    lang = db.Column(db.String(4))
    text = db.Column(db.LargeBinary)
    correctness = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)
    dico_id = db.Column(db.Integer)
    hasaudio = db.Column(db.String)
    lang_id = db.Column(db.Integer)

@app.route('/sentences/', methods=['GET'])

def sentences():
    if request.method == 'GET':
        results = Sentences.query.limit(10).offset(0).all()
    json_results = []
    for result in results:
        d = {'id': result.id,
           'lang': result.lang,
           'text': result.text,
           'correctness': result.correctness,
           'user_id': result.user_id,
           'created': result.created,
           'modified': result.modified,
           'dico_id': result.dico_id,
           'hasaudio': result.hasaudio,
           'lang_id': result.lang_id
           }
        json_results.append(d)
    return jsonify(items=json_results)

@app.route('/sentence/<int:sentence_id>', methods=['GET'])

def sentence(sentence_id):
    if request.method == "GET":
        result = Sentences.query.filter_by(id = sentence_id).first()
        json_result = {'id': result.id,
            'lang': result.lang,
            'text': result.text,
            'correctness': result.correctness,
            'user_id': result.user_id,
            'created': result.created,
            'modified': result.modified,
            'dico_id': result.dico_id,
            'hasaudio': result.hasaudio,
            'lang_id': result.lang_id
            }    
        return jsonify(items=json_result)



if __name__ == '__main__':
    app.run(debug=True)

 
    

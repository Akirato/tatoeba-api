This is a API system for tatoeba.org built on python-flask

Setting Up:
    sudo apt-get install python-pip
    pip install virtualenv

Setup development Environment by :
    cd sentences
    virtualenv venv
    . venv/bin/activate
    pip install flask
    pip install flask-sqlalchemy
    pip install mysql-python


Usage: [Just the present implementation.]
    Run routes.py using "$python routes.py"    
    It runs it on localhost:5000

    Run "curl localhost:5000/sentences/" to get all sentence table entries in database.
    Run "curl localhost:5000/sentence/sentence_id" to get that sentence.

source venv/bin/activate
export FLASK_APP=microblog.py
flask run
FLASK_APP=microblog.py
flask db init
flask db migrate
flask db upgrade
flask db migrate -m "posts table"
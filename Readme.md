source venv/bin/activate
    export FLASK_APP=microblog.py
//////////////////////
flask run
FLASK_APP=microblog.py
//////////////////
flask db init
flask db migrate
flask db upgrade
flask db migrate -m "posts table"
pip freeze > requirements.txt 
docker build --tag python-docker 
docker images
docker run -d -p 5000:5000 python-docker
docker ps
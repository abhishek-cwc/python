$env.flask_ENV="development"
$env.PATH=1
source virtaulenv/bin/activate
flask run

python3 -m venv virtualenv
pip install flask

source virtaulenv/bin/activate
PYTHONDONTWRITEBYTECODE=1 flask run
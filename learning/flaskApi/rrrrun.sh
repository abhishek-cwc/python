$env.flask_ENV="development"
$env.PATH=1
source virtaulenv/bin/activate
flask run

source virtaulenv/bin/activate
PYTHONDONTWRITEBYTECODE=1 flask run
$env.flask_ENV="development"
$env.PATH=1
source virtaulenv/bin/activate
flask run

python3 -m venv virtualenv
source virtualenv/bin/activate
pip install flask
pip install mysql-connector-python

source virtualenv/bin/activate
PYTHONDONTWRITEBYTECODE=1 flask run

API:
http://localhost:5000/getCustomerByEmail/john.doe@example.com
http://localhost:5000/getAllCustomer
http://localhost:5000/createCustomer
{
  "name": "Test2",
  "email": "testsku2@gmail.com",
  "password": "123456"
}
http://localhost:5000/getThirdParty

mysql connector
pip install mysql-connector-python
------------

jwt
pip install pyjwt
------------------

CREATE TABLE Customer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO Customer (name, email, password) VALUES ('John Doe', 'john.doe@example.com', '123456');

=========================
djangoweb
python3 -m venv virtualdenv
source virtualdenv/bin/activate
pip install django


django-admin startproject my_site
python3 manage.py startapp my_app
python3 manage.py runserver

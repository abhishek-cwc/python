$env.flask_ENV="development"
$env.PATH=1
source virtaulenv/bin/activate
flask run

python3 -m venv virtualenv
pip install flask

source virtaulenv/bin/activate
PYTHONDONTWRITEBYTECODE=1 flask run

pip install mysql-connector-python


CREATE TABLE Customer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO Customer (name, email, password) VALUES ('John Doe', 'john.doe@example.com', '123456');

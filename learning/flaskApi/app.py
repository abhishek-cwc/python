from flask import Flask

app = Flask(__name__)

@app.route("/home")
def welcome():
    return "welcome"

import controller.Customer as Customer

if __name__ == "__main__":
    app.run(port=8000)


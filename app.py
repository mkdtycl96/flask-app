from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/home')
def index():
    return "hello flask"

@app.route("/users/<user_id>",methods = ["GET","POST","PUT","DELETE"])
def parameter(user_id):
    if request.method == "GET":

        return "GET method"
    elif request.method == "POST":
        data = request.form
        return data
    elif request.method == "PUT":

        return "PUT method"
    else :
        return "DELETE method"
    return user_id
app.run()
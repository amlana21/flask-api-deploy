from flask import Flask,jsonify,make_response
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URL')
mongo = PyMongo(app)

@app.route("/")
def home_page():
    all_users = mongo.db.users.find()
    users=[]
    for rw in all_users:
        rw.pop('_id')
        users.append(rw)
    print(users)
    resp=make_response(jsonify(users),200)
    # resp=make_response(jsonify(status='done'),200)
    return resp

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
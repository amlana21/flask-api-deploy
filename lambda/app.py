from flask import Flask,jsonify,make_response
import os
import boto3


app = Flask(__name__)
USERS_TABLE = os.environ['USERS_TABLE']
client = boto3.client('dynamodb')


@app.route("/users/<username>")
def home_page(username):
    resp = client.get_item(
        TableName=USERS_TABLE,
        Key={
            'userName': { 'S': username }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'User does not exist'}), 404
    
    # resp=make_response(jsonify(users),200)
    resp=make_response(jsonify(userName=item.get('userName').get('S'),name=item.get('name').get('S')),200)
    return resp

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
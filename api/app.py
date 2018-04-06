import uuid 
import redis
from flask import Flask ,abort, request ,jsonify,redirect


app = Flask(__name__)
redisDB = redis.Redis(host='redis', port=6379)

def tryStoreUrl(url):
    """
    Generate unique string with 7 character
    If this key not exits in redis: store with key= {unique string}, value = url 
    if exits: retry
    """
    uniqueID =  uuid.uuid4().hex[:7]
    if not redisDB.setnx(uniqueID,url):
        tryStoreUrl(url)
    return uniqueID

@app.route('/',methods = ['POST'])
def post():

    if not request.json or 'url' not in request.json:
        abort(400)
    url = request.json.get('url')
    uniqueID = tryStoreUrl(url)
    return "{0}{1}".format(request.url_root,uniqueID)


@app.route('/<id>',methods = ['GET'])
def get(id):
    url =redisDB.get(id)
    if not url:
        abort(404)
    return redirect(url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
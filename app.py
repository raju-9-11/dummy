from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from data import countries
app = Flask(__name__)
CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',methods=['GET'])
def home():
    return jsonify(countries)
@app.route('/data',methods=['GET'])
def filter():
    if 'Country' in request.args:
        name = request.args['Country']
    else:
        return jsonify(countries)
    results=[]
    for i in countries:
        if i['country'] == name:
            results.append(i)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
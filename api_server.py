from flask import Flask, request, jsonify

import search_word

app = Flask(__name__)

from flask_cors import CORS, cross_origin

CORS(app)

@app.route('/search/<word>')
def search(word):
    definition_list = search_word.getDefinition(word)
    definition = ''
    for defi in definition_list:
        definition += ',' + defi
    
    if len(definition) != 0:
        definition = definition[1:]

    return jsonify({'definition': definition})
 
if __name__ == "__main__":
    app.run(port=5050)

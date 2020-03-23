"""
@author: jzaron
"""

from flask import jsonify, make_response, request

from fetcher import app
from fetcher import operations

mock_i = 0

@app.route('/api/v1.0/content/text/scrapFromUrl', methods=['PUT'])
def scrap_text():
    operations.scrap_text(request.args['url']) 
    return ('', 200)

@app.route('/api/v1.0/content/text/fromUrl', methods=['GET'])
def get_text():
    text = operations.get_text(request.args['url']) or ''
    return jsonify({'text' : text})

# @app.route('/api/v1.0/content/images/get', methods=['GET'])
# def get_image():
#     return send_file(filename, mimetype='image/gif')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)


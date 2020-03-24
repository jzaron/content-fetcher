"""
@author: jzaron
"""

from flask import jsonify, make_response, request, send_file

from fetcher import app
from fetcher import operations

mock_i = 0

@app.route('/api/v1.0/content/text/scrapFromSite', methods=['PUT'])
def scrap_text():
    operations.scrap_text(request.args['site']) 
    return ('', 200)

@app.route('/api/v1.0/content/text/fromSite', methods=['GET'])
def get_text():
    text = operations.get_text(request.args['site'])
    if text:
        return jsonify({'text' : text})
    return jsonify({})

@app.route('/api/v1.0/content/image/scrapFromSite', methods=['PUT'])
def scrap_images():
    operations.scrap_images(request.args['site']) 
    return ('', 200)

@app.route('/api/v1.0/content/image/fromSite', methods=['GET'])
def list_images():
    return jsonify(operations.list_images(request.args['site']))

@app.route('/api/v1.0/content/image/get', methods=['GET'])
def get_image():
    file = operations.get_image(request.args['id'])
    if file:
        return send_file(file, mimetype='image/gif')
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)


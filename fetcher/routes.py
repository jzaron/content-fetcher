"""
@author: jzaron
"""

from flask import jsonify, make_response, request

from fetcher import app, db
from fetcher.model.base import URL

@app.route('/api/v1.0/content/text/fetch', methods=['PUT'])
def get_text():
    db.session.add(URL(url = request.args['url']))
    db.session.commit()
    return jsonify({'url-args': request.args['url']})

@app.route('/api/v1.0/content/images/fetch', methods=['PUT'])
def get_images():
    urls = URL.query.all()
    print(urls)
    return jsonify(str(urls))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
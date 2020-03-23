from flask import Flask, jsonify, make_response, request
from config.config import AppConfig

app = Flask(__name__)

@app.route('/api/v1.0/content/text/fetch', methods=['PUT'])
def get_text():
    return jsonify({'url-args': request.args['url']})

@app.route('/api/v1.0/content/images/fetch', methods=['PUT'])
def get_images():
    return jsonify({'url-args': request.args['url']})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(port = AppConfig.APP_PORT, debug=True)


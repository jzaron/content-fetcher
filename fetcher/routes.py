"""
@author: jzaron
"""

from flask import jsonify, make_response, request, send_file

from fetcher import app
from fetcher import operations

#TODO: errors handling
#TODO: handling no resource like task/site/text/image cases
#TODO: some endpoint to search site id using URL
#TODO: some convenience endpoints


@app.route('/api/v1.0/task/run/scrapText', methods=['PUT'])
def scrap_text():
    task_id = operations.scrap_text(request.args['site'])
    if task_id:
        return jsonify({'task_id': task_id})
    return jsonify({})

@app.route('/api/v1.0/task/run/scrapImages', methods=['PUT'])
def scrap_images():
    task_id = operations.scrap_images(request.args['site'])
    if task_id:
        return jsonify({'task_id': task_id})
    return jsonify({})

@app.route('/api/v1.0/task/<task_id>', methods=['GET'])
def get_task(task_id):
    task = operations.get_task(task_id)
    if task:
        return jsonify({
            'id': task.id,
            'category': task.category,
            'site_id': task.site.id,
            'site_url': task.site.url,
            'progress': task.get_progress(),
            'finished': task.finished})
    return jsonify({})

@app.route('/api/v1.0/site/<int:site_id>', methods=['GET'])
def get_site(site_id):
    site = operations.get_site(site_id)
    if site:
        import sys
        return jsonify({
            'id' : site.id,
            'url': site.url,
            'text_id': site.text[0].id if site.text else '' ,
            'image_ids' : [image.id for image in site.images] if site.images else []
            })
    return jsonify({})

@app.route('/api/v1.0/content/text/<int:text_id>', methods=['GET'])
def get_text(text_id):
    text = operations.get_text(text_id)
    if text:
        return jsonify({
            'id' : text_id,
            'text': text
            })
    return jsonify({})

@app.route('/api/v1.0/content/image/<int:image_id>', methods=['GET'])
def get_image(image_id):
    file = operations.get_image(image_id)
    if file:
        return send_file(file, mimetype='image/gif')
    return jsonify({})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)


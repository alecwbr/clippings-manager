from . import api
from .. import db
from ..models import Tag
from flask import jsonify

@api.route('/tags')
def get_tags():
    tags = Tag.query.all()
    return jsonify(tags)

@api.route('/tag/<int:id>')
def get_tag(id):
    tag = Tag.query.get(id)
    if tag is None:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    tag_json = {'name': tag.name, 'clips': tag.clips}
    return jsonify(tag_json)

@api.route('/tag/create', methods=['POST'])
def create_tag():
    name = request.json.get('name')
    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()
    return jsonify(tag), 201, {'location': url_for('get_tag', id=tag.id)}
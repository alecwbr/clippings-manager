from . import api
from .. import db
from ..models import Author, Clip, Tag
from flask import jsonify, request

# return all clips grouped with their author
@api.route('/clips', methods=['GET'])
def get_all_clips():
    clips = Clip.query.all()
    return jsonify(clips)

# return one clip
@api.route('/clips/<int:id>')
def get_clip(id):
    clip = Clip.query.get(id)
    if clip is None:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    clip_json = clip.to_json()
    clip_json['author'] = clip.author.name
    return clip_json

@api.route('/clips/update/<int:id>', methods=['PUT'])
def update_clip(id):
    clip = Clip.query.get(id)
    if clip is None:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    tag_name = request.json.get('tag_name')
    tag = Tag.query.filter_by(name=tag_name).first()
    if tag is None:
        new_tag = Tag(name=tag_name)
        clip.tags.append(new_tag)
        db.session.add(clip)
        db.session.commit()
        return jsonify(clip)
    clip.tags.append(tag)
    db.session.add(clip)
    db.session.commit()
    return jsonify(clip)

@api.route('/clips/<int:id>', methods=['DELETE'])
def delete_clip(id):
    clip = Clip.query.get(id)
    if clip is None:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    db.session.delete(clip)
    db.session.commit()
    response = jsonify(clip)
    response.status_code = 200
    return response
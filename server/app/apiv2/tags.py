from . import apiv2
from .. import db
from ..models import Tag, Clip
from flask import jsonify, url_for, request

@apiv2.route('/tags')
def get_tags():
    tags = Tag.query.all()
    tags_list = []
    for tag in tags:
        tags_list.append(tag.to_json())

    json = {
        '_links': {
            'self': { 'href': url_for('.get_tags', _external=True) }
        },
        'count': len(tags_list),
        'tags': tags_list
    }
    return jsonify(json)

@apiv2.route('/tags/<int:tag_id>')
def get_tag(tag_id):
    pass

@apiv2.route('/clips/<int:clip_id>/tags')
def get_clip_tags(clip_id):
    clip = Clip.query.get(clip_id)
    tags_list = []
    for tag in clip.tags:
        tags_list.append(tag.to_json())
    json = {
        '_links': {
            'self': { 'href': url_for('.get_clip_tags', _external=True, clip_id=clip_id) },
            'clip': { 'href': url_for('.get_clip', _external=True, clip_id=clip_id) }
        },
        'count': len(tags_list),
        'tags': tags_list
    }
    return jsonify(json)
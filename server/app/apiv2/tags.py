from . import apiv2
from .. import db
from ..models import Tag, Clip
from flask import jsonify, url_for, request, current_app

@apiv2.route('/tags')
def get_tags():
    tags = Tag.query.all()
    tags_list = []
    for tag in tags:
        tags_list.append(tag.to_json())

    json_res = {
        '_links': {
            'self': { 'href': url_for('.get_tags', _external=True) }
        },
        'count': len(tags_list),
        'tags': tags_list
    }
    return jsonify(json_res)

@apiv2.route('/tags/<int:tag_id>')
def get_tag(tag_id):
    pass

@apiv2.route('/clips/<int:clip_id>/tags')
def get_clip_tags(clip_id):
    page = request.args.get('page', 1, type=int)
    pagination = Clip.query.filter_by(id=clip_id).first().tags.paginate(
        page, per_page=current_app.config['TAGS_PER_PAGE'], error_out=False
    )
    tags = pagination.items
    prev_p = url_for('.get_clip_tags', _external=True, clip_id=clip_id, page=page-1) if pagination.has_prev else None
    next_p = url_for('.get_clip_tags', _external=True, clip_id=clip_id, page=page+1) if pagination.has_next else None

    tags_list = []
    for tag in tags:
        tags_list.append(tag.to_json())
    json_res = {
        '_links': {
            'self': { 'href': url_for('.get_clip_tags', _external=True, clip_id=clip_id) },
            'prev': { 'href': prev_p },
            'next': { 'href': next_p }
        },
        'count': pagination.total,
        'tags': tags_list
    }
    return jsonify(json_res)
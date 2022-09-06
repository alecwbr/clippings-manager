from . import apiv2
from .. import db
from ..models import Clip
from flask import jsonify, url_for, request, current_app

@apiv2.route('/authors/<int:author_id>/clips')
def get_author_clips(author_id):
    page = request.args.get('page', 1, type=int)
    pagination = Clip.query.filter_by(author_id=author_id).paginate(
        page, per_page=current_app.config['CLIPS_PER_PAGE'], error_out=False)
    clips = pagination.items
    prev_p = url_for('.get_author_clips', _external=True, author_id=author_id, page=page-1) if pagination.has_prev else None
    next_p = url_for('.get_author_clips', _external=True, author_id=author_id, page=page+1) if pagination.has_next else None
    
    clip_list = []
    for clip in clips:
        clip_list.append(clip.to_json_v2())

    return jsonify({
        '_links': {
            'self': { 'href': url_for('.get_author_clips', _external=True, author_id=author_id, page=page) },
            'prev': { 'href': prev_p },
            'next': { 'href': next_p }
        },
        'count': pagination.total,
        'clips': clip_list
    })

@apiv2.route('/authors/<int:author_id>/clips/<int:clip_id>')
def get_author_clip(author_id, clip_id):
    clip = Clip.query.filter_by(author_id=author_id, id=clip_id).first()
    return jsonify(clip.to_json_v2())

@apiv2.route('/books/<int:book_id>/clips')
def get_book_clips(book_id):
    page = request.args.get('page', 1, type=int)
    pagination = Clip.query.filter_by(book_id=book_id).paginate(
        page, per_page=current_app.config['CLIPS_PER_PAGE'], error_out=False
    )
    clips = pagination.items
    prev_p = url_for('.get_book_clips', _external=True, book_id=book_id, page=page-1) if pagination.has_prev else None
    next_p = url_for('.get_book_clips', _external=True, book_id=book_id, page=page+1) if pagination.has_next else None

    clips_list = []
    for clip in clips:
        clips_list.append(clip.to_json_v2())

    return jsonify({
        '_links': {
            'self': { 'href': url_for('.get_book_clips', _external=True, book_id=book_id, page=page) },
            'prev': { 'href': prev_p },
            'next': { 'href': next_p }
        },
        'count': pagination.total,
        'clips': clips_list
    })

@apiv2.route('/books/<int:book_id>/clips/<int:clip_id>')
def get_book_clip(book_id, clip_id):
    clip = Clip.query.filter_by(book_id=book_id, id=clip_id).first()
    return jsonify(clip.to_json_v2())
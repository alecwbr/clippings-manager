from . import apiv2
from .. import db
from ..models import Author
from flask import jsonify, url_for, request, current_app

@apiv2.route('/authors')
def get_authors():
    page = request.args.get('page', 1, type=int)
    pagination = Author.query.paginate(
        page, per_page=current_app.config['AUTHORS_PER_PAGE'], error_out=False)
    authors = pagination.items
    prev_p = url_for('.get_authors', _external=True, page=page-1) if pagination.has_prev else None
    next_p = url_for('.get_authors', _external=True, page=page+1) if pagination.has_next else None
    
    author_list = []
    for author in authors:
        author_list.append(author.to_json())
    
    return jsonify({
        '_links': {
            'self': { 'href': url_for('.get_authors', _external=True, page=page) },
            'prev': { 'href': prev_p },
            'next': { 'href': next_p } 
        },
        'count': pagination.total,
        'authors': author_list
    })

@apiv2.route('/authors/<int:author_id>')
def get_author(author_id):
    author = Author.query.get(author_id)
    return jsonify(author.to_json())
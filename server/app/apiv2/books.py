from . import apiv2
from .. import db
from ..models import Author, Book
from flask import jsonify, url_for, request, current_app

@apiv2.route('/authors/<int:author_id>/books')
def get_books(author_id):
    page = request.args.get('page', 1, type=int)
    pagination = Book.query.filter_by(author_id=author_id).paginate(page, per_page=current_app.config['BOOKS_PER_PAGE'], error_out=False)
    books = pagination.items
    prev_p = None
    if pagination.has_prev:
        prev_p = url_for('.get_books', _external=True, page=page-1)
    next_p = None
    if pagination.has_next:
        next_p = url_for('.get_books', _external=True, page=page+1)
    
    book_list = []
    for book in books:
        book_list.append(book.to_json())

    return jsonify({
        '_links': {
            'self': { 'href': url_for('.get_books', _external=True, author_id=author_id) },
            'author': { 'href': url_for('.get_author', _external=True, author_id=author_id) },
            'prev': { 'href': prev_p },
            'next': { 'href': next_p }
        },
        'count': pagination.total,
        'books': book_list
    })
    

@apiv2.route('/authors/<int:author_id>/books/<int:book_id>')
def get_book(author_id, book_id):
    book = Book.query.filter_by(author_id=author_id, id=book_id).first()
    return jsonify(book.to_json())
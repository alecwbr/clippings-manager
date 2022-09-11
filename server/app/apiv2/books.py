from . import apiv2
from .. import db
from ..models import Author, Book
from flask import jsonify, url_for, request, current_app

@apiv2.route('/books')
def get_books():
    page = request.args.get('page', 1, type=int)
    pagination = Book.query.paginate(
        page, per_page=current_app.config['BOOKS_PER_PAGE'], error_out=False
    )
    books = pagination.items
    prev_p  = url_for('.get_books', _external=True, page=page-1) if pagination.has_prev else None
    next_p = url_for('.get_books', _external=True, page=page+1) if pagination.has_next else None
    
    book_list = []
    for book in books:
        book_list.append(book.to_json())

    json_res = {
        '_links': {
            'self': { 'href': url_for('.get_books', _external=True, page=page) },
            'prev': { 'href': prev_p },
            'next': { 'href': next_p } 
        },
        'count': pagination.total,
        'books': book_list
    }

    return jsonify(json_res)

@apiv2.route('/books/<int:book_id>')
def get_book(book_id):
    book = Book.query.get(book_id)
    return jsonify(book.to_json())

@apiv2.route('/authors/<int:author_id>/books')
def get_author_books(author_id):
    page = request.args.get('page', 1, type=int)
    pagination = Book.query.filter_by(author_id=author_id).paginate(
        page, per_page=current_app.config['BOOKS_PER_PAGE'], error_out=False
    )
    books = pagination.items
    prev_p = url_for('.get_author_books', _external=True, author_id=author_id, page=page-1) if pagination.has_prev else None
    next_p = url_for('.get_author_books', _external=True, author_id=author_id, page=page+1) if pagination.has_next else None
    
    book_list = []
    for book in books:
        book_list.append(book.to_json())

    json_res = {
        '_links': {
            'self': { 'href': url_for('.get_author_books', _external=True, author_id=author_id, page=page) },
            'prev': { 'href': prev_p },
            'next': { 'href': next_p }
        },
        'count': pagination.total,
        'books': book_list
    }

    return jsonify(json_res)
    

@apiv2.route('/authors/<int:author_id>/books/<int:book_id>')
def get_author_book(author_id, book_id):
    book = Book.query.filter_by(author_id=author_id, id=book_id).first()
    return jsonify(book.to_json())
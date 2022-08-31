from . import api
from .. import db
from ..models import Book
from flask import jsonify

@api.route('/books')
def get_books():
    books = Book.query.with_entities(Book.name).all()
    return jsonify(books)

@api.route('/books/<int:book_id>')
def get_book(book_id):
    book = Book.query.get(book_id)
    return jsonify(book)
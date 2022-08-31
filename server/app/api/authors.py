from . import api
from .. import db
from ..models import Author, Book
from flask import jsonify, request

@api.route('/authors', methods=['GET'])
def get_all_authors():
    authors = Author.query.all()
    return jsonify(authors)

@api.route('/authors/<int:id>', methods=['GET'])
def get_author(id):
    author = Author.query.get(id)
    return jsonify(author)

@api.route('/authors/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get(id)
    db.session.delete(author)
    db.session.delete(author.clips)
    db.session.commit()
    return jsonify(author)

##########
# author clips
##########
@api.route('/authors/<int:id>/clips')
def get_author_clips(id):
    author = Author.query.get(id)
    return jsonify(author.to_json_with_clips_field())

@api.route('/authors/<int:author_id>/clips/<int:clip_id>', methods=['GET'])
def get_author_clip(author_id, clip_id):
    pass

@api.route('/authors/<int:author_id>/clips/<int:clip_id>', methods=['DELETE'])
def delete_author_clip(author_id, clip_id):
    pass

##########
# author books
##########
@api.route('/authors/<int:author_id>/books/<int:book_id>')
def get_author_book(author_id, book_id):
    author_book = Author.query.get(author_id).join(Book)
    return jsonify(author_book)

@api.route('/authors/<int:author_id>/books', methods=['GET'])
def get_author_books(author_id):
    author = Author.query.get(author_id)
    return jsonify(author.to_json_with_books_field())
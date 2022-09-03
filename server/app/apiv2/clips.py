from . import apiv2
from .. import db
from ..models import Author
from flask import jsonify, url_for

@apiv2.route('/authors/<int:author_id>/clips')
def get_author_clips(author_id):
    pass

@apiv2.route('/books/<int:book_id>/clips')
def get_book_clips(book_id):
    pass
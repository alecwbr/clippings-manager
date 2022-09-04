from . import apiv2
from .. import db
from ..models import Tag
from flask import jsonify, url_for, request

@apiv2.route('/clips/<int:clip_id>/tags')
def get_clip_tags(clip_id):
    pass
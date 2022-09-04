from flask import Blueprint

apiv2 = Blueprint('apiv2', __name__)

from . import authors, books, clips, tags
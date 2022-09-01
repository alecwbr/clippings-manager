from datetime import datetime
from dataclasses import dataclass
from app import db

clip_tag = db.Table('clip_tag',
                    db.Column('clip_id', db.Integer, db.ForeignKey('clip.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )

@dataclass
class Tag(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Tag "{self.name}">'


@dataclass
class Clip(db.Model):
    id: int
    clip_type: str
    location: str
    date: str
    highlight: str
    author_id: int
    book_id: int
    tags: Tag

    id = db.Column(db.Integer, primary_key=True)
    clip_type = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(20))
    date = db.Column(db.DateTime(timezone=True))
    highlight = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    tags = db.relationship('Tag', secondary=clip_tag, backref='clips')

    def date_to_string(self):
        return datetime.strftime(self.date, '%A, %B %d, %Y %I:%M:%S %p')

    def to_json(self):
        json_clip = {
            'id': self.id,
            'clip_type': self.clip_type,
            'location': self.location,
            'date': self.date_to_string(),
            'highlight': self.highlight
        }
        return json_clip

    def __repr__(self):
        return f'<Clip "{self.title}">'

@dataclass
class Book(db.Model):
    id: int
    name: str
    author_id: int
    clips: Clip

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    clips = db.relationship('Clip', backref='book')

@dataclass
class Author(db.Model):
    id: int
    name: str
    books: Book

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', backref='author')
    clips = db.relationship('Clip', backref='author')

    def to_json_with_clips_field(self):
        clips_arr = []
        for clip in self.clips:
            clips_arr.append({
                'id': clip.id,
                'type': clip.clip_type,
                'location': clip.location,
                'date': clip.date,
                'highlight': clip.highlight
            })
        json_author = {
            'id': self.id,
            'author': self.name,
            'clips': clips_arr
        }
        return json_author

    def to_json_with_books_field(self):
        books_arr = []
        for book in self.books:
            books_arr.append({
                'id': book.id,
                'name': book.name
            })
        json_author = {
            'id': self.id,
            'author': self.name,
            'books': books_arr
        }
        return json_author
            

    def __repr__(self):
        return f'<Author "{self.name}">'
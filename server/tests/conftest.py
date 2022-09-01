import pytest
from app import create_app, db
from unittest import mock
from clippings_parser import ClippingsParser
from app.models import Author, Clip, Book

MOCK_FILE_CONTENT = '''Test Book (Fake Author)
- Your Highlight on Location 1337 | Added on Saturday, August 20, 2022 2:05:00 AM

This is a test highlight
==========
Test Book Two (Fake Author Two)
- Your Bookmark on Location 727 | Added on Sunday, August 21, 2022 3:00:00 PM


==========
'''

BAD_MOCK_FILE_CONTENT = '''Test data
Test data
Test
Test
Test
Test
Test
Test
Test
'''

@pytest.fixture
def mock_file_handle():
    handle = mock.patch('builtins.open', mock.mock_open(read_data=MOCK_FILE_CONTENT))
    yield handle

@pytest.fixture
def bad_mock_file_handle():
    handle = mock.patch('builtins.open', mock.mock_open(read_data=BAD_MOCK_FILE_CONTENT))
    yield handle

@pytest.fixture
def app(mock_file_handle):
    app = create_app('testing')
    with app.app_context():
        with mock_file_handle:
            parser = ClippingsParser(mock_file_handle)
            clips = parser.get_clips()
        db.drop_all()
        db.create_all()

        for clip in clips:
            new_clip = Clip(clip_type=clip.clip_type, location=clip.location, date=clip.date, highlight=clip.highlight) 
            author = Author.query.filter_by(name=clip.author).first()
            book = Book.query.filter_by(name=clip.book_title).first()
            if author is None:
                author = Author(name=clip.author)

            if book is None:
                book = Book(name=clip.book_title)

            book.clips.append(new_clip)
            author.books.append(book)
            author.clips.append(new_clip)
            db.session.add(author)

        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
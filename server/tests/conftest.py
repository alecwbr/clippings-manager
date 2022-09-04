import pytest
import random
import datetime
from dataclasses import dataclass
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
Test Book Three (Fake Author)
- Your Highlight on Location 100 | Added on Thursday, September 1, 2022 9:00:00 AM

This is a test highlight
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

@dataclass
class FakerData:
    title: str
    author: str
    clip_type: str
    location: str
    date_time: datetime.datetime
    highlight: str

@pytest.fixture
def fake_data_list():
    data = []
    return data

@pytest.fixture
def faker_mock_file(faker, fake_data_list):
    clip_types_list = ['Highlight', 'Bookmark', 'Note']
    FAKER_FILE = ''
    for _ in range(30):
        author = faker.name()
        title = faker.catch_phrase()
        location = random.randint(1, 2000)
        clip_type = random.choice(clip_types_list)
        highlight = faker.paragraph(nb_sentences=3) if clip_type == 'Highlight' else ''
        date_time = faker.date_time_this_decade().strftime('%A, %B %d, %Y %I:%M:%S %p')

        fake_data = FakerData(author=author, title=title, location=location, clip_type=clip_type, highlight=highlight, date_time=date_time)

        fake_data_list.append(fake_data)
        FAKER_FILE += (f'{fake_data.title} ({fake_data.author})\n'
                       f'- Your {fake_data.clip_type} on Location {fake_data.location} | Added on {fake_data.date_time}\n'
                       f'\n'
                       f'{fake_data.highlight}\n'
                       f'==========\n')
    return FAKER_FILE

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
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
def fake_data_list(faker):
    data = []
    AUTHORS_NUM = 10
    BOOKS_NUM = 5
    CLIPS_NUM = 5
    clip_types_list = ['Highlight', 'Bookmark', 'Note']
    
    for i in range(AUTHORS_NUM):
        author = faker.unique.name()
        for x in range(BOOKS_NUM):
            book_title = faker.unique.catch_phrase()
            for j in range(CLIPS_NUM):
                location_section = random.randint(1, 2000)
                location = f'{location_section}-{location_section+123}' 
                clip_type = random.choice(clip_types_list)
                highlight = faker.paragraph(nb_sentences=3) if clip_type == 'Highlight' else ''
                date_time = faker.date_time_this_decade().strftime('%A, %B %d, %Y %I:%M:%S %p')
                fake_data = FakerData(author=author, title=book_title, location=location, clip_type=clip_type, highlight=highlight, date_time=date_time)
                data.append(fake_data)

    random.shuffle(data)
    yield data
    del data

@pytest.fixture
def faker_mock_file(fake_data_list):
    FAKER_FILE = ''

    for data in fake_data_list:
        FAKER_FILE += (f'{data.title} ({data.author})\n'
                       f'- Your {data.clip_type} on Location {data.location} | Added on {data.date_time}\n'
                       f'\n'
                       f'{data.highlight}\n'
                       f'==========\n')
    yield FAKER_FILE
    del FAKER_FILE

@pytest.fixture
def mock_file_handle(faker_mock_file):
    with mock.patch('builtins.open', mock.mock_open(read_data=faker_mock_file)) as handle:
        yield handle

@pytest.fixture
def bad_mock_file_handle():
    with mock.patch('builtins.open', mock.mock_open(read_data=BAD_MOCK_FILE_CONTENT)) as handle:
        yield handle

@pytest.fixture
def parsed_clips(mock_file_handle):
    parser = ClippingsParser(mock_file_handle)
    return parser.get_clips()

@pytest.fixture
def app(parsed_clips):
    app = create_app('testing')
    with app.app_context():
        db.drop_all()
        db.create_all()

        for clip in parsed_clips:
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
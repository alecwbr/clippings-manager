import os
from datetime import datetime
from app import db
from unittest import mock
import pytest
from clippings_parser import ClippingsParser, ParsingError

MOCK_FILE_CONTENTS = '''\ufeffTest Book (Fake Author)
- Your Highlight on Location 1337 | Added on Saturday, August 20, 2022 2:05:00 AM

This is a test highlight
==========
Test Book Two (Fake Author)
- Your Bookmark on Location 727 | Added on Sunday, August 21, 2022 3:00:00 PM


==========
'''

BAD_MOCK_FILE_CONTENTS = '''Test data
Test data
Test
Test
Test
Test
Test
Test
Test
'''

def test_clippings_parser():
    with mock.patch("builtins.open", mock.mock_open(read_data=MOCK_FILE_CONTENTS)) as mock_file:
        parser = ClippingsParser(mock_file)
        clips = parser.get_clips()
        assert clips is not None
        assert clips[0].book_title == 'Test Book'
        assert clips[0].author == 'Fake Author'
        assert clips[0].clip_type == 'Highlight'
        assert clips[0].location == '1337'
        assert clips[0].date == datetime(2022, 8, 20, 2, 5)
        assert clips[0].highlight == 'This is a test highlight'

def test_clippings_parser_parsing_error():
    with mock.patch('builtins.open', mock.mock_open(read_data=BAD_MOCK_FILE_CONTENTS)) as mock_file:
        parser = ClippingsParser(mock_file)
        with pytest.raises(ParsingError):
            parser.get_clips()
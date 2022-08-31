import os
from datetime import datetime
from app import db
from unittest import mock
import pytest
from clippings_parser import ClippingsParser, ParsingError

def test_clippings_parser(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert clips is not None
        assert clips[0].book_title == 'Test Book'
        assert clips[0].author == 'Fake Author'
        assert clips[0].clip_type == 'Highlight'
        assert clips[0].location == '1337'
        assert clips[0].date == datetime(2022, 8, 20, 2, 5)
        assert clips[0].highlight == 'This is a test highlight'

def test_clippings_parser_parsing_error(bad_mock_file_handle):
    with bad_mock_file_handle:
        parser = ClippingsParser(bad_mock_file_handle)
        with pytest.raises(ParsingError):
            parser.get_clips()
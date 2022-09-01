import os
from datetime import datetime
from app import db
from unittest import mock
import pytest
from clippings_parser import ClippingsParser, ParsedClip, ParsingError

def test_clippings_parser_parsing_error(bad_mock_file_handle):
    with bad_mock_file_handle:
        parser = ClippingsParser(bad_mock_file_handle)
        with pytest.raises(ParsingError):
            parser.get_clips()

def test_clippings_parser_get_clips_returns_type_ParsedClip(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        assert parser.get_clips() is not None

def test_clippings_parser_is_correct_size(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert len(clips) == 2

def test_clippings_parser_book_title(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert clips[0].book_title == 'Test Book'

def test_clippings_parser_author(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert clips[0].author == 'Fake Author'

def test_clippings_parser_clip_type(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert clips[0].clip_type == 'Highlight'

def test_clippings_parser_location(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert clips[0].location == '1337'

def test_clippings_parser_date(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert clips[0].date == datetime(2022, 8, 20, 2, 5)

def test_clippings_parser_book_title(mock_file_handle):
    with mock_file_handle:
        parser = ClippingsParser(mock_file_handle)
        clips = parser.get_clips()
        assert clips[0].highlight == 'This is a test highlight'

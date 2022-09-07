import os
from datetime import datetime, timezone
from app import db
from unittest import mock
import pytest
from clippings_parser import ClippingsParser, ParsingError

def test_clippings_parser_parsing_error(bad_mock_file_handle):
    parser = ClippingsParser(bad_mock_file_handle)
    with pytest.raises(ParsingError):
        clips = parser.get_clips()
        next(clips)

def test_clippings_parser_get_clips_is_not_none(mock_file_handle):
    parser = ClippingsParser(mock_file_handle)
    assert parser.get_clips() is not None

def test_clippings_parser_is_correct_size(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert len(list(clips)) == len(fake_data_list)

def test_clippings_parser_book_title(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert next(clips).book_title == fake_data_list[0].title

def test_clippings_parser_author(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert next(clips).author == fake_data_list[0].author

def test_clippings_parser_clip_type(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert next(clips).clip_type == fake_data_list[0].clip_type

def test_clippings_parser_location(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert next(clips).location == fake_data_list[0].location

def test_clippings_parser_date(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert next(clips).date == datetime.strptime(fake_data_list[0].date_time, '%A, %B %d, %Y %I:%M:%S %p').astimezone()

def test_clippings_parser_book_title(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert next(clips).highlight == fake_data_list[0].highlight

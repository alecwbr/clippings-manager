import os
from datetime import datetime, timezone
from app import db
from unittest import mock
import pytest
from clippings_parser import ClippingsParser, ParsingError

def test_clippings_parser_parsing_error(bad_mock_file_handle):
    parser = ClippingsParser(bad_mock_file_handle)
    with pytest.raises(ParsingError):
        parser.get_clips()

def test_clippings_parser_get_clips_is_not_none(mock_file_handle):
    parser = ClippingsParser(mock_file_handle)
    assert parser.get_clips() is not None

def test_clippings_parser_is_correct_size(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert len(clips) == len(fake_data_list)

def test_clippings_parser_book_title(parsed_clips, fake_data_list):
    assert parsed_clips == fake_data_list

def test_clippings_parser_author(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert clips[0].author == fake_data_list[0].author

def test_clippings_parser_clip_type(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert clips[0].clip_type == fake_data_list[0].clip_type

def test_clippings_parser_location(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert clips[0].location == fake_data_list[0].location

def test_clippings_parser_date(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert clips[0].date == datetime.strptime(fake_data_list[0].date_time, '%A, %B %d, %Y %I:%M:%S %p').astimezone()

def test_clippings_parser_book_title(mock_file_handle, fake_data_list):
    parser = ClippingsParser(mock_file_handle)
    clips = parser.get_clips()
    assert clips[0].highlight == fake_data_list[0].highlight

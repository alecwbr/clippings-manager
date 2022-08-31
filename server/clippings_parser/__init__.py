import re
import itertools
from datetime import datetime
from dataclasses import dataclass
from app.models import Clip
from typing import List

class ParsedClip:
    book_title: str
    author: str
    clip_type: str
    date: datetime
    location: str
    highlight: str

    def __init__(self, book_title, author, clip_type, date, location, highlight):
        self.book_title = book_title
        self.author = author
        self.clip_type = clip_type
        self.date = date
        self.location = location
        self.highlight = highlight

class ClippingsParser():
    clips: List[ParsedClip]

    def __init__(self, my_clippings_file):
        self.__my_clippings_file = my_clippings_file
        self.clips = []

    def __parse_clip_title(self, clip):
        self.__clean_title_author = clip[0].lstrip("\ufeff").rstrip()
        clip_title = self.__clean_title_author.split('(')[0].rstrip()
        return clip_title

    def __parse_clip_author(self, clip):
        author = re.findall(r"\(([^)]+)\)$", self.__clean_title_author)[0]
        return author

    def __parse_clip_type(self, clip):
        if 'Bookmark' in clip[1]:
            return 'Bookmark'
        elif 'Highlight' in clip[1]:
            return 'Highlight'
        elif 'Note' in clip[1]:
            return 'Note'
        else:
            return None

    def __parse_clip_date(self, clip):
        sub_str = '| Added on '
        sub_str_len = len(sub_str)
        clip_len = len(clip[1])
        added_on_index = clip[1].find(sub_str)
        date = clip[1][added_on_index + sub_str_len : clip_len].rstrip()
        return datetime.strptime(date, '%A, %B %d, %Y %I:%M:%S %p')

    def __parse_clip_location(self, clip):
        sub_str = 'Location '
        sub_str_len = len(sub_str)
        added_on_index = clip[1].find(' | Added on ')
        on_location_index = clip[1].find(sub_str)
        location = clip[1][on_location_index + sub_str_len : added_on_index]
        return location

    def __parse_clip_highlight(self, clip):
        return clip[3].rstrip() 

    def get_clips(self) -> List[ParsedClip]:
        book_clips = []
        with open(self.__my_clippings_file) as f:
            for key, group in itertools.groupby(f, lambda line: line.startswith('==========')):
                if not key:
                    book_clips.append(list(group))
        for clip in book_clips:
            title = self.__parse_clip_title(clip)
            author = self.__parse_clip_author(clip)
            clip_type = self.__parse_clip_type(clip)
            date = self.__parse_clip_date(clip)
            location = self.__parse_clip_location(clip)
            highlight = self.__parse_clip_highlight(clip)

            parsed_clip = ParsedClip(book_title=title, author=author, clip_type=clip_type, date=date, location=location, highlight=highlight)
            self.clips.append(parsed_clip)
        
        return self.clips
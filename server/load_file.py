import sys
from app import create_app, db
from app.models import Author, Clip, Book
from clippings_parser import ClippingsParser

def main():
    app = create_app('development')

    parser = ClippingsParser(sys.argv[1])
    clips = parser.get_clips()

    with app.app_context():
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

if __name__ == '__main__':
    main()
def test_get_author_clips_returns_correct_json(client):
    with client:
        response = client.get('/api/v2/authors/1/clips')
        assert response.json == {
            '_links': {
                'self': { 'href': 'http://localhost/api/v2/authors/1/clips' },
                'author': { 'href': 'http://localhost/api/v2/authors/1' },
                'prev': { 'href': None },
                'next': { 'href': None }
            },
            'count': 2,
            'clips': [
                {
                    '_links': {
                        'self': { 'href': 'http://localhost/api/v2/authors/1/clips/1' },
                        'book': { 'href': 'http://localhost/api/v2/books/1' },
                        'collections/tags': { 'href': 'http://localhost/api/v2/clips/1/tags'}
                    },
                    'id': 1,
                    'clip_type': 'Highlight',
                    'location': '1337',
                    'date': 'Saturday, August 20, 2022 02:05:00 AM',
                    'highlight': 'This is a test highlight',
                    'author_id': 1,
                    'author_name': 'Fake Author',
                    'book_id': 1,
                    'book_name': 'Test Book'
                },
                {
                    '_links': {
                        'self': { 'href': 'http://localhost/api/v2/authors/1/clips/3' },
                        'book': { 'href': 'http://localhost/api/v2/books/3' },
                        'collections/tags': { 'href': 'http://localhost/api/v2/clips/3/tags'}
                    },
                    'id': 3,
                    'clip_type': 'Highlight',
                    'location': '100',
                    'date': 'Thursday, September 01, 2022 09:00:00 AM',
                    'highlight': 'This is a test highlight',
                    'author_id': 1,
                    'author_name': 'Fake Author',
                    'book_id': 3,
                    'book_name': 'Test Book Three'
                }
            ]
        }
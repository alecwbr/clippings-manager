def test_api_get_books_returns_correct_json(client):
    with client:
        response = client.get('/api/v2/authors/1/books')
        assert response.json == {
            '_links': {
                'self': { 'href': 'http://localhost/api/v2/authors/1/books' },
                'author': { 'href': 'http://localhost/api/v2/authors/1' },
                'prev': { 'href': None },
                'next': { 'href': None }
            },
            'count': 2,
            'books': [
                {
                    '_links': {
                        'self': { 'href': 'http://localhost/api/v2/authors/1/books/1' },
                        'collections/clips': { 'href': 'http://localhost/api/v2/books/1/clips' }
                    },
                    'id': 1,
                    'name': 'Test Book',
                    'author_id': 1,
                    'author_name': 'Fake Author'
                },
                {
                    '_links': {
                        'self': { 'href': 'http://localhost/api/v2/authors/1/books/3' },
                        'collections/clips': { 'href': 'http://localhost/api/v2/books/3/clips' }
                    },
                    'id': 3,
                    'name': 'Test Book Three',
                    'author_id': 1,
                    'author_name': 'Fake Author'
                }
            ]
        }

def test_api_get_book_returns_correct_json(client):
    with client:
        response = client.get('/api/v2/authors/1/books/1')
        assert response.json == {
            '_links': {
                'self': { 'href': 'http://localhost/api/v2/authors/1/books/1' },
                'collections/clips': { 'href': 'http://localhost/api/v2/books/1/clips' }
            },
            'id': 1,
            'name': 'Test Book',
            'author_id': 1,
            'author_name': 'Fake Author'
        }
def test_api_get_author_returns_correct_json(client):
    with client:
        response = client.get('/api/v2/authors/1')
        assert response.json == {
            '_links': {
                'self': { 'href': 'http://localhost/api/v2/authors/1' },
                'collections/books': { 'href': 'http://localhost/api/v2/authors/1/books' },
                'collections/clips': { 'href': 'http://localhost/api/v2/authors/1/clips' }
            },
            'id': 1,
            'name': 'Fake Author'
        }

def test_api_get_authors_returns_correct_json(client):
    with client:
        response = client.get('/api/v2/authors')
        assert response.json == {
            '_links': {
                'self': { 'href': 'http://localhost/api/v2/authors' },
                'prev': { 'href': None },
                'next': { 'href': None }
            },
            'count': 2,
            'authors': [
                {
                    '_links': {
                        'self': { 'href': 'http://localhost/api/v2/authors/1' },
                        'collections/books': { 'href': 'http://localhost/api/v2/authors/1/books' },
                        'collections/clips': { 'href': 'http://localhost/api/v2/authors/1/clips' }
                    },
                    'id': 1,
                    'name': 'Fake Author'
                },
                {
                    '_links': {
                        'self': { 'href': 'http://localhost/api/v2/authors/2' },
                        'collections/books': { 'href': 'http://localhost/api/v2/authors/2/books' },
                        'collections/clips': { 'href': 'http://localhost/api/v2/authors/2/clips' }
                    },
                    'id': 2,
                    'name': 'Fake Author Two'
                }
            ]
        }
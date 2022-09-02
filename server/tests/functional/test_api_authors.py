def test_api_get_authors_response_json_is_not_none(client):
    with client:
        response = client.get('/api/authors')
        assert response.status_code == 200
        assert response.json is not None

def test_api_get_authors_response_json_is_correct_length(client):
    with client:
        response = client.get('/api/authors')
        assert len(response.json) == 2

def test_api_get_author_response_json(client):
    with client:
        response = client.get('/api/authors/1')
        assert response.json == {
            'id': 1,
            'name': 'Fake Author',
            'books': [
                {
                    'id': 1,
                    'name': 'Test Book',
                    'author_id': 1,
                    'clips': [
                        {
                            'id': 1,
                            'clip_type': 'Highlight',
                            'location': '1337',
                            'date': 'Sat, 20 Aug 2022 02:05:00 GMT',
                            'highlight': 'This is a test highlight',
                            'author_id': 1,
                            'book_id': 1,
                            'tags': []
                        }
                    ]
                },
                {
                    'id': 3,
                    'name': 'Test Book Three',
                    'author_id': 1,
                    'clips': [
                        {
                            'id': 3,
                            'clip_type': 'Highlight',
                            'location': '100',
                            'date': 'Thu, 01 Sep 2022 09:00:00 GMT',
                            'highlight': 'This is a test highlight',
                            'author_id': 1,
                            'book_id': 3,
                            'tags': []
                        }
                    ]
                }
            ]
        }

def test_api_delete_author_returns_author(client):
    with client:
        response = client.delete('/api/authors/1')
        assert response.json == {
            'id': 1,
            'author': 'Fake Author',
            'books_num': 2,
            'clips_num': 2
        }

def test_api_delete_author_clip_returns_deleted_clip_if_successful(client):
    with client:
        response = client.delete('/api/authors/1/clips/1')
        assert response.json['id'] == 1

def test_api_delete_author_clip_returns_error_if_author_id_and_clip_id_not_valid(client):
    with client:
        response = client.delete('/api/authors/2/clips/1')
        assert response.json['error'] == 'not found'
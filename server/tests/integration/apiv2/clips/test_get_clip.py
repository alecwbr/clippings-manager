import pytest

endpoints_list = ['/api/v2/authors/1/clips/1', '/api/v2/books/1/clips/1']

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_has_links_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'self', 'author', 'book', 'collections/tags'}.issubset(response.json['_links'])

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'id', 'clip_type', 'location', 'date', 'highlight',
                'author_id', 'author_name', 'book_id', 'book_name'}.issubset(response.json)
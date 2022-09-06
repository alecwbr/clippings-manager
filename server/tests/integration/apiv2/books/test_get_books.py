import pytest

endpoints_list = ['/api/v2/books', '/api/v2/authors/1/books']

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_root_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'count', 'books'}.issubset(response.json)

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_books_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'id', 'name', 'author_id', 'author_name'}.issubset(response.json['books'][0])
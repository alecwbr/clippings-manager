import pytest

endpoints_list = ['/api/v2/authors']

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_root_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'count', 'authors'}.issubset(response.json)

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_books_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'id', 'name'}.issubset(response.json['authors'][0])
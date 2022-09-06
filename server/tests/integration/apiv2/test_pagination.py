import pytest

endpoints_list = ['/api/v2/authors',
                  '/api/v2/books',
                  '/api/v2/authors/1/books', 
                  '/api/v2/authors/1/clips',
                  '/api/v2/books/1/clips'
                 ]

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_pagination_links_self_json(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert response.json['_links']['self']['href'] == f'http://localhost{endpoint}?page=1'

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_pagination_links_prev_json(client, endpoint):
    with client:
        response = client.get(f'{endpoint}?page=2')
        assert response.json['_links']['prev']['href'] == f'http://localhost{endpoint}?page=1'

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_pagination_links_next_json(client, endpoint):
    with client:
        response = client.get(f'{endpoint}?page=2')
        assert response.json['_links']['next']['href'] == f'http://localhost{endpoint}?page=3'

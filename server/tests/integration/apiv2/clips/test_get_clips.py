import pytest

endpoints_list = ['/api/v2/authors/1/clips']

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_root_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'count', 'clips'}.issubset(response.json)

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_clips_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'id', 'clip_type', 'location', 'date', 'highlight',
                'author_id', 'author_name', 'book_id', 'book_name'}.issubset(response.json['clips'][0])
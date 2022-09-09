import pytest

endpoints_list = ['/api/v2/clips/1/tags', '/api/v2/tags']

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_root_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'count', 'tags'}.issubset(response.json)

@pytest.mark.parametrize('endpoint', endpoints_list)
def test_clips_object_has_keys(client, endpoint):
    with client:
        response = client.get(endpoint)
        assert {'_links', 'id', 'name'}.issubset(response.json['tags'][0])

def test_clip_tag_value(client):
    with client:
        response = client.get(endpoints_list[0])
        assert response.json['tags'][0]['name'] == 'tag1'
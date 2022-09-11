def test_post_tags_creates_tag_for_clip(client):
    with client:
        json_req = {
            'name': 'exampletag'
        }
        response = client.post('/api/v2/clips/1/tags', json=json_req)
        assert response.json['name'] == 'exampletag'
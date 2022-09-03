def test_api_get_clips_response_json_is_not_none(client):
    with client:
        response = client.get('/api/v1/clips')
        assert response.status_code == 200
        assert response.json is not None

def test_api_get_clips_response_json_is_correct_length(client):
    with client:
        response = client.get('/api/v1/clips')
        assert len(response.json) == 3

def test_api_get_clip_response_json_is_not_none(client):
    with client:
        response = client.get('/api/v1/clips/1')
        assert response.json is not None

def test_api_get_clip_response_json(client):
    with client:
        response = client.get('/api/v1/clips/1')
        assert response.json == {
            'id': 1,
            'author': 'Fake Author',
            'clip_type': 'Highlight',
            'highlight': 'This is a test highlight',
            'location': '1337',
            'date': 'Saturday, August 20, 2022 02:05:00 AM'
        }

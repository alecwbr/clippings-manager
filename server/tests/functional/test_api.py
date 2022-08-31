from app.models import Author, Clip

def test_api_get_all_clips(client):
    with client:
        response = client.get('/api/clips')
        assert response.status_code == 200
        assert response.json != None

def test_api_get_one_clip(client):
    with client:
        response = client.get('/api/clips/1')
        assert response.status_code == 200
        assert response.json != None
        assert response.json['id'] == 1
        assert response.json['author'] == 'Fake Author'
        assert response.json['clip_type'] == 'Highlight'
        assert response.json['highlight'] == 'This is a test highlight'
        assert response.json['location'] == '1337'
        assert response.json['date'] == 'Saturday, August 20, 2022 02:05:00 AM'

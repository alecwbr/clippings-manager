def test_api_get_authors_response_json_is_not_none(client):
    with client:
        response = client.get('/api/authors')
        assert response.status_code == 200
        assert response.json is not None

def test_api_get_authors_response_json_is_correct_length(client):
    with client:
        response = client.get('/api/authors')
        assert len(response.json) == 2
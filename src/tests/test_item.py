def test_get_item(api_client):
    response = api_client.get("/api/v1/item")
    assert response.status_code == 200
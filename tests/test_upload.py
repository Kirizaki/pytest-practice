def test_upload_returns_id(client):
    # arrange: create test data
    payload = {
        "content": "JESIOTR"
    }

    # act: run SUT
    response = client.post(
        "/upload",
        params=payload
    )

    # assert: check the expected result
    assert response.status_code == 200
    data = response.json()
    assert "id" in data


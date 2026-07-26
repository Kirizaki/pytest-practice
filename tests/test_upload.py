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


def test_download_uploaded_file(client):
    # arrange
    test_content = "JESIOTR to smaczna ryba."
    upload_response = client.post(
        "/upload",
        params={
            "content": test_content
        }
    )
    file_id = upload_response.json()["id"]

    # act
    response = client.get(
        f"/download/{file_id}"
    )

    # assert
    assert response.status_code == 200
    assert response.json()["content"] == test_content


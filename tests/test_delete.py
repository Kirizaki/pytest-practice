def test_delete_uploaded_file(client):
    # arrange
    upload_response = client.post(
        "/upload",
        params={
            "content": "another jesiotr..."
        }
    )
    file_id = upload_response.json()["id"]

    # act
    delete_response = client.delete(
        f"/file/{file_id}"
    )

    # assert
    assert delete_response.status_code == 200
    assert delete_response.json()["deleted"] is True


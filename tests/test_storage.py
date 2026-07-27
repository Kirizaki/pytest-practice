def test_download_storage_failure(client, mocker):
    # arrange
    mocker.patch(
        "app.main.storage.get",
        side_effect=Exception("Storage down :(")
    )

    # act
    response = client.get(
        "/download/jesiotr"
    )

    # assert
    assert response.status_code == 500


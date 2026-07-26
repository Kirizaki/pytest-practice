def test_download_missing_file_returns_404(client):
    # arrange
    fake_id = "i-want-to-believe"

    # act
    response = client.get(
        f"/download/{fake_id}"
    )

    # assert
    assert response.status_code == 404


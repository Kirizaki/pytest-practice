from concurrent.futures import ThreadPoolExecutor

def test_multiple_uploads_create_unique_files(client):
    # arrange
    amount = 100
    def upload_file(i):
        response = client.post(
            "/upload",
            params={ "content": f"file-{i}"}
        )
        return response.json()["id"]

    # act
    with ThreadPoolExecutor(max_workers=10) as executor:
        ids = list(executor.map(upload_file, range(amount)))
    
    # assert
    assert len(ids) == amount
    assert len(set(ids)) == amount


def test_upload_stress(client):
    # arrange
    def upload():
        return client.post(
            "/upload",
            params={ "content": "stress"}
        )
    
    # act
    with ThreadPoolExecutor(max_workers=50) as executor:
        responses = list(executor.map(lambda _: upload(), range(200)))

    # assert
    assert all(r.status_code == 200 for r in responses)


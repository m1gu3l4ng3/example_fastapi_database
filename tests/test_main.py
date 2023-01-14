from fastapi.testclient import TestClient

def test_main(client_app: TestClient, mocker) -> None:
    """
    """
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value.json.return_value = {
        "slideshow": {
		    "author": "Yours Truly"
            }
        }
    response = client_app.post(
        "/api/v1/score",
        json={
	        "score_math": 10,
	        "score_science": 8,
	        "score_chemistry": 7
        }
    )

    print(response.json())
    assert response.status_code == 200
    assert response.json()['slideshow']['author'] == "Yours Truly"

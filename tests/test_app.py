from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange
    # (FastAPI app initialized)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities
    assert "Gym Class" in activities

def test_signup_success():
    # Arrange
    activity_name = "Gym Class"
    email = "test_student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

def test_signup_duplicate_error():
    # Arrange
    activity_name = "Gym Class"
    email = "double_signup@mergington.edu"

    # Act - First signup
    client.post(f"/activities/{activity_name}/signup?email={email}")
    # Act - Second signup (duplicate)
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"

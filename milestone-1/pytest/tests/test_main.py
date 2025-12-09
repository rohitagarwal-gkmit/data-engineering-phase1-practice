from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestHelloWorld:
    def test_hello_world(self) -> None:
        """Test the hello_world endpoint.

        Returns:
            None
        """

        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

    def __repr__(self):
        return "TestHelloWorld"


class TestRepeatMessage:
    def __repr__(self):
        return "TestRepeatMessage"

    def test_repeat_message(self) -> None:
        """Test the repeat_message endpoint.

        Returns:
            None
        """

        message = "Test Message"
        response = client.post("/", params={"message": message})
        assert response.status_code == 200
        assert response.json() == {"You sent": message}

    def test_repeat_no_message(self) -> None:
        """Test the repeat_message endpoint with no message.
        Returns:
            None
        """

        response = client.post("/")
        assert response.status_code == 422

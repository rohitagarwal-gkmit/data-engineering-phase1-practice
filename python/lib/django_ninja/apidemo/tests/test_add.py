from django.test import TestCase, Client
from apidemo.schemas.add import AddRequest, AddResponse


class AddAPITestCase(TestCase):
    """Test case for the /add API endpoint."""

    def setUp(self):
        """Set up the test client."""

        self.client = Client()

    def test_add_api_correct_value(self):
        """Test the addition API endpoint."""

        # Prepare the request payload
        payload = AddRequest(a=3, b=5).model_dump()

        # Make a POST request to the /add endpoint
        response = self.client.post(
            "/api/add", data=payload, content_type="application/json"
        )
        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Parse the response JSON
        response_data = response.json()

        # Validate the response against the AddResponse schema
        add_response = AddResponse(**response_data)

        # Assert that the result is correct
        self.assertEqual(add_response.result, 8)

    def test_api_missing_fields(self):
        """Test the addition API endpoint with missing fields."""

        # Prepare the request payload with missing 'b'
        payload = {"a": 3}

        # Make a POST request to the /add endpoint
        response = self.client.post(
            "/api/add", data=payload, content_type="application/json"
        )

        # Check that the response status code is 422 Unprocessable Entity
        self.assertEqual(response.status_code, 422)

    def test_api_invalid_types(self):
        """Test the addition API endpoint with invalid types."""

        # Prepare the request payload with invalid types
        payload = {"a": "three", "b": 5}

        # Make a POST request to the /add endpoint
        response = self.client.post(
            "/api/add", data=payload, content_type="application/json"
        )

        # Check that the response status code is 422 Unprocessable Entity
        self.assertEqual(response.status_code, 422)

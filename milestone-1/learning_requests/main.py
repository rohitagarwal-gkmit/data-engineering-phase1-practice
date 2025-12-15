import requests
import os


RESPONSE_STORE_DIR = "responses/"
os.makedirs(RESPONSE_STORE_DIR, exist_ok=True)


def try_get_request() -> None:
    """
    GET request to fetch all objects from the API and store the response in a JSON file.
    """

    # Request module - GET request
    get_response = requests.get("https://api.restful-api.dev/objects")
    print("response body", get_response.json())
    with open(f"{RESPONSE_STORE_DIR}get_response.json", "w") as f:
        f.write(get_response.text)


def try_post_request() -> str:
    # Request module - POST request
    """
    POST request to create a new object in the API and store the response in a JSON file.

    Returns: id (str): The ID of the created object.
    """
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    }

    post_response = requests.post("https://api.restful-api.dev/objects", json=data)
    global id
    id = post_response.json().get("id")

    print("response body", post_response.json())

    with open(f"{RESPONSE_STORE_DIR}post_response.json", "w") as f:
        f.write(post_response.text)

    return id


def try_put_request(id: str) -> None:
    # Request module - PUT request
    """
    PUT request to update an existing object in the API and store the response in a JSON file.
    """

    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver",
        },
    }

    put_response = requests.put(f"https://api.restful-api.dev/objects/{id}", json=data)

    with open(f"{RESPONSE_STORE_DIR}put_response.json", "w") as f:
        f.write(put_response.text)

    print("response body", put_response.json())


def try_patch_request(id: str) -> None:
    # Request module - PATCH request
    """
    PATCH request to update an existing object in the API and store the response in a JSON file.
    """

    data = {"name": "Apple MacBook Pro 16 (Updated Name)"}

    patch_response = requests.patch(
        f"https://api.restful-api.dev/objects/{id}", json=data
    )
    print("response body", patch_response.json())

    with open(f"{RESPONSE_STORE_DIR}patch_response.json", "w") as f:
        f.write(patch_response.text)


def try_delete_request(id: str) -> None:
    # Request module - DELETE request
    """
    DELETE request to remove an existing object in the API and store the response in a JSON file.
    """

    delete_response = requests.delete(f"https://api.restful-api.dev/objects/{id}")

    delete_response_json = delete_response.json()

    print(delete_response_json["message"])

    with open(f"{RESPONSE_STORE_DIR}delete_response.json", "w") as f:
        f.write(delete_response.text)


if __name__ == "__main__":
    id = ""

    try_get_request()
    id = try_post_request()
    try_put_request(id=id)
    try_patch_request(id=id)
    try_delete_request(id=id)

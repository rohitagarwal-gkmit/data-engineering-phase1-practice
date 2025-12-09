from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world() -> dict:
    """Hello World endpoint.

    Returns:
        dict: A dictionary with a greeting message.
    """

    return {"Hello": "World"}


@app.post("/")
def repeat_message(message: str) -> dict:
    """Repeat Message endpoint.

    Args:
        message (str): The message to be repeated.

    Returns:
        dict: A dictionary with the repeated message in format {"You sent": message}.
    """

    return {"You sent": message}

from pydantic import BaseModel


# Request schema - {"a": int, "b": int}
class AddRequest(BaseModel):
    """
    Request schema for addition.

    Args:
        a (int): First integer.
        b (int): Second integer.
    """

    a: int = 1
    b: int = 2


# Response schema - {"result": int}
class AddResponse(BaseModel):
    """
    Response schema for addition result.

    Args:
        result (int): The sum of the two integers.
    """

    result: int

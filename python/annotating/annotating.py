from fastapi import Query
from typing import Annotated


def search(q: Annotated[str, Query(max_length=20)]):
    if len(q) > 20:
        raise TypeError("Query exceeds maximum length of 20 characters.")
    return q


# Python Learning Notes - Annotating with typing.Annotated
# The typing.Annotated type hint allows you to add metadata to type hints.
# This is useful for frameworks like FastAPI that can use this metadata for validation, serialization,
# and documentation generation.
# In the example above, we use Annotated to specify that the query parameter 'q'
# should have a maximum length of 20 characters.
# This metadata is provided by FastAPI's Query class, which defines additional constraints for query parameters

print(search("example query"))  # Example usage
print(search("qwertyuiopasdfghjkqwertyuioasdfghjkl"))  # Exceeds max_length example

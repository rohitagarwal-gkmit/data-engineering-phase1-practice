from typing import Callable

# Python Learning Notes - Return Type Annotations
# Return type annotations in Python are hints that indicate the expected return type of a function.
# They are not enforced at runtime but can be checked by static type checkers like mypy
# Use type hints consistently for clarity and tooling, but don't rely on them for runtime safety.
# Tools like mypy or IDEs (e.g., VS Code with Pylance) can flag mismatches.
# If you want enforcement, look into libraries that add runtime checks, but that's not standard.


# Function with return type annotation
def add1(a: int, b: int) -> int:
    """Adds two integers and returns an integer.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b


# Function with multiple possible return types
def add(a: int, b: int) -> int | float | str:
    """Adds two integers and returns different types based on conditions.
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        int | float | str: The sum of the two integers, or "zero" if both are zero, or a float if the sum is negative.
    """

    if a == 0 and b == 0:
        return "zero"
    if a < 0:
        return float(a + b)

    return a + b


# Function that returns another function
def return_a_function() -> Callable[[int, int], int]:
    """Returns a function that adds two numbers.

    Returns:
        callable: A function that takes two integers and returns their sum.
    """

    def inner_add(x: int, y: int) -> int:
        """Adds two integers.

        Args:
            x (int): First integer.
            y (int): Second integer.

        Returns:
            int: The sum of the two integers.
        """
        return x + y

    return inner_add


# Example function with None return type
def log_message(msg: str) -> None:
    """Logs a message to the console.

    Args:
        msg (str): The message to log.

    Returns:
        None
    """
    print(msg)


print(add1(3, 4.9))

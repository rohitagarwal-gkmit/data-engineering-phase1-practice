import sys
from pydantic import BaseModel, ValidationError


# cli argv schema - {"a": int, "b": int}
class CliArgs(BaseModel):
    """
    Command line arguments schema for addition.
    Args:
        a (int): First integer.
        b (int): Second integer.
    """

    a: int
    b: int


try:
    # Parse command line arguments
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    args = CliArgs(a=a, b=b)

    # Perform addition
    result = args.a + args.b

    # Output result
    print(f"Result of adding {args.a} and {args.b} is: {result}")
except (IndexError, ValueError):
    print("Please provide two integer arguments.")
except ValidationError as e:
    print("Validation error:", e)

class MathHelper:
    """A helper class for basic mathematical operations.

    Methods:
        add(a, b): Returns the sum of a and b.
        subtract(a, b): Returns the difference of a and b.
        multiply(a, b): Returns the product of a and b.
        divide(a, b): Returns the quotient of a and b.
        power(a, b): Returns a raised to the power of b.
    """

    @staticmethod
    def add(a: int | float, b: int | float) -> int | float:
        """Returns the sum of a and b.
        Args:
            a (int | float): The first number.
            b (int | float): The second number.
        Returns:
            int | float: The sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a: int | float, b: int | float) -> int | float:
        """Returns the difference of a and b.
        Args:
            a (int | float): The first number.
            b (int | float): The second number.
        Returns:
            int | float: The difference of a and b.
        """

        return a - b

    @staticmethod
    def multiply(a: int | float, b: int | float) -> int | float:
        """Returns the product of a and b.
        Args:
            a (int | float): The first number.
            b (int | float): The second number.
        Returns:
            int | float: The product of a and b.
        """

        return a * b

    @staticmethod
    def divide(a: int | float, b: int | float) -> int | float:
        """Returns the quotient of a and b.
        Args:
            a (int | float): The numerator.
            b (int | float): The denominator.
        Returns:
            int | float: The quotient of a and b.
        Raises:
            ValueError: If b is zero.
        """

        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: int | float, b: int | float) -> int | float:
        """Returns a raised to the power of b.
        Args:
            a (int | float): The base number.
            b (int | float): The exponent.
        Returns:
            int | float: The result of a raised to the power of b. and b are assumed to be non-negative.
        """
        if b == 0:
            return 1

        return a**b

import pandas as pd


class MathHelperBase:
    """A helper class for basic mathematical operations. base python and no dataFrames used.

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


class MathHelperWithDataFrames:
    """A helper class for basic mathematical operations using pandas DataFrames.

    Methods:
        add(df1, df2): Returns the element-wise sum of two DataFrames.
        subtract(df1, df2): Returns the element-wise difference of two DataFrames.
        multiply(df1, df2): Returns the element-wise product of two DataFrames.
        divide(df1, df2): Returns the element-wise quotient of two DataFrames.
    """

    @staticmethod
    def add(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Returns the element-wise sum of two DataFrames.
        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.
        Returns:
            pd.DataFrame: The element-wise sum of df1 and df2.
        """

        return df1.add(df2)

    @staticmethod
    def subtract(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Returns the element-wise difference of two DataFrames.
        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.
        Returns:
            pd.DataFrame: The element-wise difference of df1 and df2.
        """
        return df1.subtract(df2)

    @staticmethod
    def multiply(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Returns the element-wise product of two DataFrames.
        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.
        Returns:
            pd.DataFrame: The element-wise product of df1 and df2.
        """
        return df1.multiply(df2)

    @staticmethod
    def divide(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Returns the element-wise quotient of two DataFrames.
        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.
        Returns:
            pd.DataFrame: The element-wise quotient of df1 and df2.
        """
        return df1.divide(df2)

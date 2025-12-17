class Test:

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def add(self) -> int:
        return self.a + self.b

    # what are classmethod and staticmethod in python

    # Class methods are methods that are bound to the class and not the instance of the class.
    # They can access and modify class state that applies across all instances of the class.
    # Static methods, on the other hand, do not have access to the instance (self) or class (cls) and
    # are used to group functions that have some logical connection to the class.

    # Example of classmethod and staticmethod

    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        return a * b

    # Right Static Method
    @staticmethod
    def test_method() -> str:
        return "This is a static method"

    # Wrong Static Method
    @staticmethod
    def wrong_test_method() -> int:
        try:
            return self.a + self.b
        except:
            return "Can't use the self in the static method"


test = Test(5, 10)


print(test.add())  # Method
print(Test.multiply(3, 4))  # Class Method
print(Test.test_method())  # Statc Method - Right one
print(Test.wrong_test_method())  # Statc Method - Wrong one

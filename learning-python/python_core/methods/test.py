class Test:

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def add(self) -> int:
        return self.a + self.b

    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        return a * b

    @staticmethod
    def test_method() -> str:
        return "This is a static method"


test = Test(5, 10)


print(Test.multiply(3, 4))

print(test.add())

print(Test.test_method())

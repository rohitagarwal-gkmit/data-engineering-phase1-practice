from typeguard import typechecked


@typechecked
def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(5, 10)
print(f"Result of adding numbers: {result}")

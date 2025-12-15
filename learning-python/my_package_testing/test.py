from rohit_math_helper import MathHelper
from nax_hello import say_hello

if __name__ == "__main__":
    print(say_hello.print_hello("Rohit"))

    print("Addition:", MathHelper.add(10, 5))
    print("Subtraction:", MathHelper.subtract(10, 5))
    print("Multiplication:", MathHelper.multiply(10, 5))
    print("Division:", MathHelper.divide(10, 5))
    print("Power:", MathHelper.power(2, 3))

# MathHelper Package

This package provides basic mathematical operations such as addition, subtraction, multiplication, and division.

## Installation

To install the package, use pip:

```bash
pip install mathhelper
```

## Usage

Here's how to use the MathHelper package:

the package provide 2 classes MathHelperBase and MathHelperWithDataFrames.

the MathHelperBase class provides basic mathematical operations:

- Addition
- Subtraction
- Multiplication
- Division
- power

- Example:

```python
from mathhelper import MathHelperBase
result_add = MathHelper.add(5, 3)
result_subtract = MathHelper.subtract(5, 3)
result_multiply = MathHelper.multiply(5, 3)
result_divide = MathHelper.divide(5, 3)
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
```

the MathHelperWithDataFrames class extends MathHelperBase and adds support for operations on pandas DataFrames.

- Example:

```python
import pandas as pd
from mathhelper import MathHelperWithDataFrames
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
math_helper_df = MathHelperWithDataFrames()
result_df_add = math_helper_df.add(df, 10)
print("DataFrame Addition:\n", result_df_add)
```

# Python Program Structure

## Structure Characteristics

- Uses indentation(best practice is 4 spaces) to define code blocks
- Everything nested under a condition, loop, or function must be indented properly

# Python Comments

## Comment Characteristics

### Single line starts with a #

- `# this is a comment`

### Multi line start with 3 " then comment then ends with 3 "

`"""
This is a multi line comment
"""`

# Variables and Naming

## Characteristics

### Python uses dynamic typing - no need to declare types

`name = "Python"`
`age = 48` 

## Naming Rules

- Use `snake_case`
- No special symbols or spaces
- Must start with a letter or _

# Data Types (Primitives)

| Type | Examples |
|------|----------|
| `int` | `age = 30` |
| `float` | `pi = 3.14` |
| `str` | `name = "Python"` |
| `bool` | `is admin = True` |
| `list` | `colors = ["red", "blue"]` |
| `tuple` | `point = (3, 4)` |
| `dict` | `person = {"name": "Python"}` |
| `set` | `unique = {1, 2, 3,}` |

# Printing and Input

## Print Syntax

- `print("Hello, World!")`

## Input Syntax

- `name = input("Whati is your name? ")`

    - input() always returns a **string**

# Operators

## Math Operators

| Operator | Function | 
|----------|----------|
| `+` | Addition | 
| `-` | Substraction |
| `*` | Multiplication | 
| `/` | Division (float) | 
| `//` | Floor Division (Rounds down to the nearest whole number) |
| `%` | Modulus (REmainder) |
| `**` | Exponent |

### Addition `+`

### Use clear variable names like `subttotal`, `tax`, `total` 

```bash
a = 5         # Assignment Statement
b = 4         # Assignment Statement
total = a + b # Assignment Statement: total = Variable identifier, `=` = Assignment operator, `a + b` = Expression
print(total)  # Function call Statement - built-in function(print) gets an argument(total)
```
### Subtraction `-`

### Use `-=` for decrementing in loops or counters and it subtracts the second value from the first

```bash
a = 10              # Assignment Statement
b = 5               # Assignment Statement
difference = a - b  # Assignment Statement: difference = Variable identifier, `=` = Assignment operator, `a - b` = Expression
print(difference)   # Function call Statement - print is built-in function and difference is the argument
```
### Multiplication `*`

### When multiplying by constants (e.g 1000), consider defining the constant with a name

```bash
length = 2             # Assignment Statement
width = 2              # Assignment Statement
area = length * width  # Assignment Statement
print(area)            # Function call Statement - print is built-in function and area is the argument
```

### Float Division `/`

### Returns a float result, even if evenly divisible and Always expect a float when using /. If you need an integer use //

```bash
result = 10 / 2   # Assignment Statement
print(result)     Function call Statement - print is the built-in function and result is the argument
```

### Floor Division `//`

### Divides and rounds down to the nearest whole number and useful when you only want how many whole items fit

### Use Cases

| Use Cases |
|-----------|
| When you need an integer result from division |
| When splitting things evenly(like pagination, chunks, rows) |
| When calculating 'how many whole units fit into' something |

```bash
whole = 7 // 2    # Assignment Statement
print(whole)      # Function Call Statement - print is the built-in function and whole is the argement
```

### Modulus (Remainder) `%`

### Returns the remainder of division

### Use Cases

| Use Cases |
|-----------|
| Check if numbers are even or odd |
| Loop in cycles |
| Wrap values (like ring buffers, indexing) |

```bash
print(10 % 3)   # Function call Statement - print is the built-in function and `10 % 3` is the argument
print(7 % 2)    # Function call Statement - print is the built-in function and `7 % 2` is the argument

# Checking even/odd
if x % 2 == 0:     # Conditional Statement - checks if a condition is `true` or ` false`
   print("Even")  # Function call Statement - print is the built-in function and `Even` is the argument
```

### Exponent `**`

### Raises a number to the power of another (sam*e as `math.pow()`)

### Use Cases

| Use Cases |
|-----------|
| Powers of 2: `2 ** n` |
| Square roots: `x ** 0.5` |
| Anything math-heavy without importing extra libraries |

```bash
print(2 ** 3)    # Function call Statement - print is the built-in function and `2 ** 3` is the argument
print(9 ** 0.5)  # Function call Statement - print is the built-in function and `9 ** 0.5` is the argument (Tip- use `x ** 0.5` for square root)
```

### Bonus: In-place operators

### Combined Math operators Assignments - Use Sparingly and only when it makes the loop or counter more readable

```bash
x += 1
x -= 2
x *= 3
x /= 4
x //= 5
x %= 6
X **= 7
```
## Comparison

## `==` Equal to

## Description: Checks if teo values are the same

### Example

```bash
a = 5          # Assignment Statement
b = 5          # Assignment Statement
print(a == b)  # Print is the built-in function and (a == b) is the argument
```

## `!=` Not Equal to

## Description: Check to see if two values are different

### Example

```bash
a = 5         # Assignment Statement
b = 7         # Assignment Statement
print(a != b) # Print is the built-in function and (a != b) is the argument
```

## `>` Greater than

## Description: Checks if value on left is greater than value on right

### Example

```bash
a = 10        # Assignment Statement
b = 3         # Assignment Statement
print(a > b)  # Print is the built-in function and (a > b) is the argument
```

## `<` Less than

## Description: Checks if value on left is less than the value on the right

### Example 

```bash
a = 2         # Assignment Statement
b = 8         # Assignment Statement
print(a < b)  # print is the built-in function and (a < b) os the argument
```
## `>=` Greater than or equal to

## Deecription: True if left aide is bigger or equal to right side

### Example

```bash
a = 10         # Assignment Statement
b = 10         # Assignment Statement
print(a >= b)  # Print is a built-in function and (a >= b) is an argument
```

## `<=` Less than or equal to

## Description: True if left side is smaller or equal to right side

### Example

```bash
a = 4          # Assignment Statement
b = 4          # Assignment Statement
print(a <= b)  # Print is the buildt-in function and (a <= b) is the argument
```

## Logical

## `and` Logical and

## Description: Return true only if both conditions are true and false if either condition is false

### Example

```bash
age = 25                      # Assignment Statement
print(age > 18 and age < 30)  # Print is the built-in function and the logical operator is the argument
print(age > 18 and age > 40). # Print is the built-in function and the logical operator is the srgument
```

## `or` Logical or

```bash
age = 15                      # Assignment Statement
print(age > 18 or age == 15)  # Print is the built-in function and the logical operator is the argument
print(age > 18 or age > 20)   # Print is the built-in function and the logical operator is the argument
```

## `not` Logical not

## Description: Use when u want the opposite of a condition

```bash
is_logged_in = False
print(not is logged in)      # True, because NOT False = True

x = 10
print(not (x > 5))           # False, because x > 5 is true
```

# Control Flow

## Conditional Statements

## if

```bash
if age >= 18:        # Conditional Statement that states to Print 'Adult' if the age is greater than or equal to 18
    print("Adult")   # Function Call Statement - print is the built-in function and `Adult` is the argument
elif age > 12:       # Conditional Statement that states to print 'Teen' if and only if age is greater than 12
    print("Teen")    # Function Call Statement - print is the built - in function and 'Teen' is the argument
else:                # Conditional Statement that states to print 'Child' if the inputed 'age' does not meet the conditions for the 'if' or 'elif' statements
    print("Child")   # Function Call Statement - print is the built - function and 'Child' is the argument
```
# Loops

## `For` Loops

```bash
for i in range(5):   # Loop Header for = Loop keyword, i = variable, in membership keyword, range(5) = Iterable, : = starts the loop body 
    print(i)         # Function Call Statement - print is the built - in Function and 'i' is the argument
```
## `While` Loops

```bash
while x < 10:        # Loop Header while = Loop keyword, x < 10 Boolean expression, : = starts the indented block
    print(x)         # Function call Statement - print is the built-in function and 'x' is the argument
    x += 1           # Combined Math Operator Statement - it says to add 1 to 'x' everytime
```

# Functions

## Definitions

```bash
def greet(name):           # Function Definition header: def = python keyword, greet = Function name, name = Parameter(argument placeholder), : = start the indent
    return "Hello" + name  # Return Statement: return = tells function what value to send back to caller, '"Hello" + name` Combines Hello with name that was entered
```

## Call it

```bash
print(greet("Name"))
```

# Helpful Tips

| Helpful Tips |
|--------------|
| Think in blocks and logic |
| Test things in Python shell |
| Read and interpret **tracebacks(errors)** - they are friendly and helpful |
| Use short, clear functions |
| DRY: Don't Repeat Yourself |
| Spacing matters for readability |
| Use parentheses when mixing operators |
| Be explicit in formulas |
| Do not guess integer vs float |


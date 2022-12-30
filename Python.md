## Python Default and Non-Default Arguments

In Python, you can define a function with default arguments, which are values that will be used as the default for the corresponding parameters if no value is passed to the function when it is called. Default arguments are specified by giving a default value in the function definition.

Here is an example of a Python function with default arguments:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

# Call the function with a default argument
greet('John') # Outputs: "Hello, John!"

# Call the function with a non-default argument
greet('John', 'Hi') # Outputs: "Hi, John!"

```
In this example, the greet function has two parameters: name and greeting. The greeting parameter has a default value of 'Hello', so if the greet function is called without a value for this parameter, the default value will be used.

For example, when we call greet('John'), the name parameter is given the value 'John', and the greeting parameter is given the default value 'Hello', so the function prints "Hello, John!".

On the other hand, if we call greet('John', 'Hi'), the name parameter is still given the value 'John', but the greeting parameter is given the value 'Hi', so the function prints "Hi, John!".

### Interview questions on default and non-default arguments

Here are some interview questions related to default and non-default arguments in Python, along with sample answers:

### How do you define a default argument in a Python function?

To define a default argument in a Python function, you can give the parameter a default value in the function definition. For example:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')
In this example, the greet function has a default argument greeting with a default value of 'Hello'. If the greet function is called without a value for this parameter, the default value will be used.

### Can you provide an example of a function with default arguments?
Example of a function with default arguments:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet('John') # Outputs: "Hello, John!"
greet('John', 'Hi') # Outputs: "Hi, John!"
```
In this example, the greet function has a default argument greeting with a default value of 'Hello'. If the greet function is called without a value for this parameter, the default value will be used.

### How do you call a function with default arguments in Python?
To call a function with default arguments in Python, you can simply call the function and omit the arguments that have default values. For example:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet('John') # Outputs: "Hello, John!"
```

In this example, we call the greet function with a single argument 'John', and the greeting argument is given the default value 'Hello'.

### What happens if you call a function with default arguments and provide values for some of the parameters?
If you call a function with default arguments and provide values for some of the parameters, the default values will be overridden by the values you provide. For example:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet('John', 'Hi') # Outputs: "Hi, John!"
```
In this example, we call the greet function with two arguments: 'John' and 'Hi'. The default value of the greeting argument is overridden by the value 'Hi', so the function prints "Hi, John!".

### Can you provide an example of a function with both default and non-default arguments?
Example of a function with both default and non-default arguments:

```python
def greet(greeting='Hello', name):
  print(f'{greeting}, {name}!')
 
greet('John') # Outputs: "Hello, John!"
greet('Hi', 'John') # Outputs: "Hi, John!"
```

In this example, the greet function has two arguments: greeting and name. The greeting argument has a default value

### what are the positional and key word arguments
In Python, positional arguments are arguments that are passed to a function in a specific order, based on the position of the argument in the function definition. Positional arguments are required, and must be provided when the function is called.

Here is an example of a function with positional arguments in Python:

```python
def greet(greeting, name):
  print(f'{greeting}, {name}!')

greet('Hello', 'John') # Outputs: "Hello, John!"
```
In this example, the greet function has two positional arguments: greeting and name. When we call the greet function, we pass the values 'Hello' and 'John' as arguments, which are assigned to the greeting and name parameters, respectively.

Keyword arguments, on the other hand, are arguments that are passed to a function by specifying the parameter name and value in the function call. Keyword arguments are optional and can be provided in any order.

Here is an example of a function with keyword arguments in Python:

```python
def greet(greeting='Hello', name='John'):
  print(f'{greeting}, {name}!')

greet() # Outputs: "Hello, John!"
greet(name='Alice') # Outputs: "Hello, Alice!"
greet(greeting='Hi', name='Alice') # Outputs: "Hi, Alice!"
```
In this example, the greet function has two keyword arguments: greeting and name, both of which have default values. When we call the greet function with no arguments, the default values are used. When we call the greet function with one argument, the default value for the other argument is used. And when we call the greet function with both arguments, the default values are overridden by the values we provide.


## Different type of Arguments in Python

* Positional arguments: Positional arguments are arguments that are passed to a function in a specific order, based on the position of the argument in the function definition. Positional arguments are required, and must be provided when the function is called.

* Keyword arguments: Keyword arguments are arguments that are passed to a function by specifying the parameter name and value in the function call. Keyword arguments are optional and can be provided in any order.

* Default arguments: Default arguments are arguments that have a default value specified in the function definition. If a default argument is not provided when the function is called, the default value will be used.

* Variable-length arguments: Variable-length arguments are arguments that allow a function to accept a variable number of arguments. There are two types of variable-length arguments in Python: *args and **kwargs. *args is used to capture a variable number of positional arguments, and **kwargs is used to capture a variable number of keyword arguments.

* Optional arguments: Optional arguments are arguments that are not required when the function is called, but can be provided if needed. Optional arguments can be implemented using default arguments or variable-length arguments.


## How **kwargs are stored in python

In Python, the **kwargs syntax is used to define a function that can accept a variable number of keyword arguments. When a function with **kwargs is called, any extra keyword arguments are packed into a dictionary and stored in the variable kwargs.

Here is an example of a function with **kwargs in Python:

```python
def greet(**kwargs):
  print(f'Hello, {", ".join(f"{key}={value}" for key, value in kwargs.items())}!')

greet(name='John', age=30, city='New York') # Outputs: "Hello, name=John, age=30, city=New York!"
```
In this example, the greet function has a single parameter **kwargs, which is used to capture a variable number of keyword arguments. When we call the greet function with three keyword arguments: name='John', age=30, and city='New York', these arguments are packed into a dictionary and stored in the kwargs variable.

Inside the function, we use the items method of the kwargs dictionary to iterate over the key-value pairs, and then use the join method of the str class to join the key-value pairs into a single string, separated by commas.


## How *args are stored in python 
In Python, the *args syntax is used to define a function that can accept a variable number of positional arguments. When a function with *args is called, any extra positional arguments are packed into a tuple and stored in the variable args.

Here is an example of a function with *args in Python:
```python

def greet(*args):
  print(f'Hello, {", ".join(args)}!')

greet('John', 'Alice', 'Bob') # Outputs: "Hello, John, Alice, Bob!"
```

In this example, the greet function has a single parameter *args, which is used to capture a variable number of positional arguments. When we call the greet function with three arguments: 'John', 'Alice', and 'Bob', these arguments are packed into a tuple and stored in the args variable.

Inside the function, we use the join method of the str class to join the elements of the args tuple into a single string, separated by commas.


## Sample code to take user inputs and do maths calcuation 

In this program, we define a function perform_operation that takes three arguments: a, b, and choice. The function uses an if-elif-else statement to check the value of choice and perform the corresponding operation.

Then, we accept values for a and b from the user, as well as a choice for the operation. Finally, we call the perform_operation function with the values of a, b, and choice and print the result.

```python
def perform_operation(a, b, choice):
  if choice == 1:
    return a + b
  elif choice == 2:
    return a - b
  elif choice == 3:
    return a * b
  elif choice == 4:
    return a / b
  else:
    return "Invalid choice"

# Accept values and choice from the user
a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
choice = int(input("Enter your choice (1=Add, 2=Sub, 3=Mul, 4=Div): "))

# Perform the operation and print the result
result = perform_operation(a, b, choice)
print(result)

```

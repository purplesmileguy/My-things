import random
import pyfiglet

# Examples
def generate_examples(num_examples, operation, length1, length2, allow_remainder=False):
    examples = []
    for _ in range(num_examples):
        num1 = generate_number(length1)
        num2 = generate_number(length2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = max(num1, num2) - min(num1, num2)
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if allow_remainder:
                result = num1 / num2
            else:
                result = num1 // num2

        example = f"{num1} {operation} {num2}"
        examples.append((example, result))

    return examples

# Generating numbers
def generate_number(length):
    if length == 'tens':
        return random.randint(10, 99)
    elif length == 'hundreds':
        return random.randint(100, 999)
    elif length == 'thousands':
        return random.randint(1000, 9999)

# Code
result = pyfiglet.figlet_format("PurpleCode")
print(result)
num_examples = int(input("Enter the number of examples: "))
operation = input("Choose the operation (+, -, *, /): ")
length1 = input("Choose the length of the first number (tens, hundreds, thousands): ")
length2 = input("Choose the length of the second number (tens, hundreds, thousands): ")
allow_remainder = False

if operation == '/':
    remainder_choice = input("Do you want to include remainder (yes/no)? ")
    if remainder_choice.lower() == 'yes':
        allow_remainder = True

examples = generate_examples(num_examples, operation, length1, length2, allow_remainder)
for example, result in examples:
    print(example)

show_results = input("Show the results of examples (yes/no)? ")
if show_results.lower() == 'yes':
    print("Results:")
    for _, result in examples:
        print(result)

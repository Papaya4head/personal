""" 
import statistics
name=str(input('enter your name :'))
def greet(name):
    print(f'welcome to gdsc,', name + '!')
greet(name)
x=int(input('no 1 : '))
z=int(input('no 2 : '))
def add_numbers(x,z):
     t=x+z
t=add_numbers(x,z)
print(t)
def print_args(*args):
    for arg in args:
        print(arg) """

def calculate_average(*args):
    """Calculates the average of a list of numbers."""
    total = sum(args)/len(args)
    return total
average = calculate_average(1,2,3,4,5,6)
print("Average of the numbers:", average)
add_two_numbers = lambda a, b: a + b
print("Sum of 5 and 3:", add_two_numbers(5, 3))

square_number = lambda x: x * x
print("Square of 4:", square_number(4))

is_even = lambda x: x % 2 == 0
print("Is 11 even?", is_even(11))


print("Even numbers in the list:", list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

numbers = [1, 2, 3, 4, 5, 6]

doubled_numbers = map(lambda x: x*2 , numbers)

print("Doubled numbers:", list(doubled_numbers))

def get_numbers_and_sum():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1 + num2
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return None

sum_of_numbers = get_numbers_and_sum()
if sum_of_numbers is not None:
    print("Sum of the numbers:", sum_of_numbers)
def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Division by zero error")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
divide_numbers()



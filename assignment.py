# 1. Exceptional Weather Forecast

# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start
# Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

inp = int(input("Enter the temperature in Fahrenheit: "))


# Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.

# Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

def fahrenheit_to_celsius(fahrenheit):
    try:
        degrees_celsius = 5 / 9 * (fahrenheit - 32)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except OverflowError:
        print("There was an overflow error with your input. Please try a different input")
    else:
        print(f"{fahrenheit} degrees fahrenheit is equal to {degrees_celsius} degrees Celsius")
    finally:
        print("Thank you for using the calculator!")

fahrenheit_to_celsius(inp)

# 2. The Recipe Ratio Adjuster

# Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.

# Use a try block to catch any arithmetic errors that may occur during the calculation.

# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

while(True):
    try:
        inp = int(input("How many servings is the recipe originally asking for? "))
        inp1 = int(input("How many servings do you wish to make? "))
        total_servings = inp * inp1
    except ValueError:
        print("There was a Value Error! Please enter appropriate input")
    except ArithmeticError:
        print("There was an arithmetic error! Please try again.")
    else:
        print(f"The total servings amount to {total_servings}")
    finally:
        print("Enjoy your cooking!")
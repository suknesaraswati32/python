# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     result = a / b
#     print("Result:", result)

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")


# try:
#     num = int(input("Enter a number: "))
#     print("Number:", num)

# except ValueError:
#     print("Error: Please enter a valid integer.")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     result = a / b

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# else:
#     print("Division successful.")
#     print("Result:", result)


# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     print("Result:", a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# finally:
#     print("Program execution completed.")


# numbers = [10, 20, 30, 40, 50]

# try:
#     index = int(input("Enter index: "))
#     print("Element:", numbers[index])

# except IndexError:
#     print("Error: Index is out of range.")

# except ValueError:
#     print("Error: Enter a valid integer index.")


# student = {
#     "name": "Saraswati",
#     "age": 20,
#     "branch": "CSE"
# }

# try:
#     key = input("Enter key: ")
#     print("Value:", student[key])

# except KeyError:
#     print("Error: Key does not exist.")




# try:
#     file = open("dfs.py", "r")
#     content = file.read()
#     print(content)
#     file.close()

# except FileNotFoundError:
#     print("Error: File does not exist.")



# class AgeError(Exception):
#     pass


# try:
#     age = int(input("Enter your age: "))

#     if age < 18:
#         raise AgeError("Age must be 18 or above.")

#     print("You are eligible.")

# except AgeError as e:
#     print("Error:", e)



try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Division successful.")
    print("Result:", result)

finally:
    print("Thank you!")

def add(a, b):
    return a + b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2)
print("Addition =", result)



square = lambda x: x * x
num = int(input("Enter a number: "))
print("Square =", square(num))



import array
arr = array.array('i', [10, 20, 30, 40, 50])
print("Array elements:", arr)
arr.append(60)
print("After adding element:", arr)
arr.remove(30)
print("After removing element:", arr)



with open("demo.txt", "w") as file:
    file.write("Welcome to Python programming")
with open("demo.txt", "r") as file:
    data = file.read()
print(data)



import os
directory = "myfolder"
if not os.path.exists(directory):
    os.mkdir(directory)
print("Directory created successfully")
print("Current directory:", os.getcwd())
print("Directories and files:", os.listdir())

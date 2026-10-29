# n = int(input("enter a number"))
# if n == 0:
#     print("number is zero")
# else:
#     print("number is non-zero")



# a = int(input("enter first number"))
# b = int(input("enter second number"))
# if a > b:
#     print("largest number is", a)
# else:
#     print("largest number is", b)


# n = int(input("enter a number"))
# if n > 0:
#     print("number is positive")
# elif n < 0:
#     print("number is negative")
# else:
#     print("number is zero")


# ch = input("enter a character ")
# if ch in "aeiou":
#     print("vowel")
# else:
#     print("consonant")


# percentage = float(input("enter percentage"))
# if percentage >= 90:
#     print("excellent")
# elif percentage >= 80:
#     print("very Good")
# elif percentage >= 70:
#     print("good")
# elif percentage >= 60:
#     print("average")
# else:
#     print("poor performance")



# a = int(input("enter first number"))
# b = int(input("enter second number"))
# c = int(input("enter third number"))
# if a >= b and a >= c:
#     print("largest number", a)
# elif b >= a and b >= c:
#     print("largest number", b)
# else:
#     print("largest number", c)


# a = int(input("enter first number"))
# b = int(input("enter second number"))
# c = int(input("enter third number"))
# if a <= b and a <= c:
#     print("smallest number", a)
# elif b <= a and b <= c:
#     print("smallest number", b)
# else:
#     print("smallest number", c)



n = int(input("enter number"))
if n % 2 == 0:
    print("number is even")
else:
    print("number is odd")
    
    
year = int(input("enter year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("leap year")
else:
    print("not leap year")    
    
    
    
married = input("driver married ")
gender = input("enter gender ")
age = int(input("enter age"))
if married == "yes":
    print("driver is insured")
elif married == "no" and gender == "male" and age > 30:
    print("driver is insured")
elif married == "no" and gender == "female" and age > 25:
    print("driver is insured")
else:
    print("driver is not insured")  
    
      
    
    
n = int(input("enter n: "))
i = 1
while i <= n:
    print(i)
    i = i + 1    
  
  
    
n = int(input("enter n: "))
i = 2
while i <= n:
    print(i)
    i = i + 2  
      
    
    
n = int(input("enter n: "))
i = 1
while i <= n:
    print(i)
    i = i + 2    
    
    
n = int(input("enter n: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print("sum =", sum) 



n = int(input("enter n: "))
i = 1
sum = 0
while i <= n:
    if i % 2 != 0:
        sum = sum + i
    i = i + 1
print("sum =", sum)   




n = int(input("enter n"))
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print("sum =", sum)



n = int(input("enter n"))
i = n
while i >= 1:
    print(i)
    i = i - 1
    
    
    
n = int(input("enter terms"))
a = 0
b = 1
i = 1
while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1    
    
    
n = int(input("enter number"))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("factorial =", fact)    


n = int(input("enter number"))
i = 2
flag = 0
while i < n:
    if n % i == 0:
        flag = 1
        break
    i = i + 1
if n <= 1:
    print("not prime")
elif flag == 0:
    print("prime")
else:
    print("not prime")
    
    
    
n = int(input("enter number"))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("sum", sum)    



n = int(input("enter number"))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("palindrome")
else:
    print("not palindrome")
    
    
n = int(input("enter number"))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("reverse =", reverse)    


n = int(input("enter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1
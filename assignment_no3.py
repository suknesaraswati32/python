students = {
    "rahul": 78,
    "priya": 85
}
name = input("enter name")
marks = float(input("enter marks"))
students[name] = marks
name = input("enter to update")
if name in students:
    students[name] = float(input("enter marks: "))
name = input("enter student: ")
students.pop(name, None)
print("students:", students)
print("average:", sum(students.values()) / len(students))
print("highest:", max(students.values()))
print("lowest:", min(students.values()))



import math
points = []
n = int(input("enter number"))
for i in range(n):
    x = float(input("enter x"))
    y = float(input("enter y"))
    points.append((x, y))
p1 = points[0]
p2 = points[1]
distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
print("distance", distance)
farthest = max(points, key=lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2))
print("farthest point", farthest)




server_ip = ("192.168.1.10", 8080)
allowed_ips = ["192.168.1.2", "192.168.1.3"]
print("server ip:", server_ip)
print("allowed ips:", allowed_ips)
new_ip = input("enter new allowed ip: ")
allowed_ips.append(new_ip)
print("updated configuration:")
print("server ip:", server_ip)
print("allowed ips:", allowed_ips)



project1 = set(input("enter employees1 ").split())
project2 = set(input("enter employees2: ").split())
print("common employees:", project1 & project2)
print("only project 1:", project1 - project2)
print("only project 2:", project2 - project1)
print("all employees:", project1 | project2)



from collections import Counter
text = input("enter text")
words = text.lower().split()
frequency = Counter(words)
print("total words", len(words))
print("word frequency", dict(frequency))
print("top 3", frequency.most_common(3))

vowels = sum(1 for ch in text.lower() if ch in "aeiou")
print("vowel count", vowels)



book1 = set(input("enter words").lower().split())
book2 = set(input("enter words  ").lower().split())
print("unique words", book1)
print("unique words", book2)
print("common words", book1 & book2)
print("only first", book1 - book2)
print("only second", book2 - book1)
print("total unique words", len(book1 | book2))



inventory = {
    "pen": 20,
    "book": 15,
    "bag": 0
}
product = input("enter product")
stock = int(input("enter stock"))
inventory[product] = stock
product = input("enter to update")
if product in inventory:
    inventory[product] = int(input("enter stock"))
highest = max(inventory, key=inventory.get)
print("highest stock", highest, inventory[highest])
inventory = {k: v for k, v in inventory.items() if v != 0}
print("inventory", inventory)
print("unique products", len(inventory))



import string
s1 = input("enter string")
s2 = input("enter string")
a = sorted(ch.lower() for ch in s1 if ch not in string.punctuation and not ch.isspace())
b = sorted(ch.lower() for ch in s2 if ch not in string.punctuation and not ch.isspace())
if a == b:
    print("anagram")
else:
    print("not anagram")



attendance = {}
n = int(input("enter days"))
for i in range(n):
    day = input("enter day")
    students = set(input("enter student").split())
    attendance[day] = students
all_days = set(attendance.values())
days = list(attendance.values())
attended_all = set.intersection(*days) if days else set()
print("attended days", attended_all)
only_one = set()
for students in days:
    only_one.update(students)
count = {}
for students in days:
    for student in students:
        count[student] = count.get(student, 0) + 1
only_one = {student for student in only_one if count[student] == 1}
print("only one day", only_one)
print("unique students", set().union(*days) if days else set())



from collections import Counter
text = input("enter text")
choice = input("ignore case")
if choice.lower() == "yes":
    text = text.lower()
frequency = Counter(text)
for ch, count in frequency.most_common():
    print(repr(ch), count)



import re
email = input("enter email")
pattern = r"^[a-z0-9._-]+@[a-z0-9-]+(\.[a-z0-9-]+)+$"
if re.match(pattern, email.lower()):
    parts = email.split(".")
    if 2 <= len(parts[-1]) <= 6:
        print("valid email")
    else:
        print("invalid email")
else:
    print("invalid email")



import re
text = input("enter text")
pattern = r"\(?\d{3}\)?[-.\s]\d{3}[-.]\d{4}|\d{10}"
phones = re.findall(pattern, text)
print("phone numbers", phones)



import re
text = input("enter text")
pattern = r"(https?://[^\s]+|www\.[^\s]+)"
urls = re.findall(pattern, text)
print("urls", urls)



import re
password = input("enter password ")
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-]).{8,}$"
if re.match(pattern, password):
    print("strong password")
else:
    print("weak password")



import re
from datetime import datetime
text = input("enter dates")
patterns = [
    r"\b\d{2}/\d{2}/\d{4}\b",
    r"\b\d{2}-\d{2}-\d{4}\b",
    r"\b\d{4}\.\d{2}\.\d{2}\b",
    r"\b(?:january|february|march|april|may|june|july|august|september|october|november|december) \d{1,2}, \d{4}\b"
]
dates = []
for pattern in patterns:
    dates.extend(re.findall(pattern, text.lower()))
for date in dates:
    try:
        if "/" in date:
            d = datetime.strptime(date, "%d/%m/%Y")
        elif "-" in date:
            d = datetime.strptime(date, "%m-%d-%Y")
        elif "." in date:
            d = datetime.strptime(date, "%Y.%m.%d")
        else:
            d = datetime.strptime(date.title(), "%B %d, %Y")
        print(d.strftime("%Y-%m-%d"))
    except:
        print("invalid date", date)



import re
html = input("enter html")
clean = re.sub(r"<[^>]+>", "", html)
print(clean)



import re
text = input("enter text")
hashtags = re.findall(r"#\w+", text)
print("hashtags:", hashtags)



import re
from collections import Counter
filename = input("enter filename")
with open(filename, "r") as file:
    text = file.read()
extensions = re.findall(r"\.[a-zA-Z0-9]+", text)
counts = Counter(extensions)
print("extensions", extensions)
print("count", dict(counts))



import ipaddress
ip = input("enter ip address")
try:
    address = ipaddress.ip_address(ip)
    if address.version == 4:
        print("valid ipv4")
    else:
        print("valid ipv6")
except:
    print("invalid ip")



import string
from collections import Counter
filename = input("enter filename: ")
with open(filename, "r") as file:
    text = file.read()
text = text.lower()
for ch in string.punctuation:
    text = text.replace(ch, "")
words = text.split()
frequency = Counter(words)
print("top 10 words", frequency.most_common(10))



import re
filename = input("enter filename")
query = input("enter search query")
with open(filename, "r") as file:
    text = file.read()
matches = re.findall(re.escape(query), text, re.IGNORECASE)
highlighted = re.sub(
    re.escape(query),
    lambda m: "[" + m.group() + "]",
    text,
    flags=re.IGNORECASE
)
print(highlighted)
print("count", len(matches))



import re
stopwords = {"the", "is", "a", "an", "and", "of", "to", "in", "on", "for"}
text = input("enter text")
words = text.lower().split()
result = [word for word in words if word not in stopwords]
print("result", " ".join(result))



import re
filename = input("enter filename")
old_word = input("enter word to find")
new_word = input("enter replacement")
choice = input("case sensitive?")
with open(filename, "r") as file:
    text = file.read()
if choice.lower() == "yes":
    text = text.replace(old_word, new_word)
else:
    text = re.sub(re.escape(old_word), new_word, text, flags=re.IGNORECASE)
new_filename = input("enter new filename")
with open(new_filename, "w") as file:
    file.write(text)
print("file saved")



import re
text = input("enter text: ")
sentences = re.split(r"(?<=[.!?])\s+", text.strip())

for sentence in sentences:
    if sentence:
        print(sentence)



import re
from collections import Counter
text = input("enter text")
words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
frequency = Counter(words)
sentences = re.split(r"(?<=[.!?])\s+", text)
for sentence in sentences:
    score = sum(frequency[word.lower()] for word in re.findall(r"\b[a-zA-Z]+\b", sentence))
    print(score, sentence)



import re
text = input("enter text: ")
contractions = {
    "can't": "cannot",
    "won't": "will not",
    "don't": "do not",
    "doesn't": "does not",
    "isn't": "is not",
    "aren't": "are not",
    "i'm": "i am",
    "you're": "you are",
    "they're": "they are"
}
text = text.lower()
for old, new in contractions.items():
    text = text.replace(old, new)
text = re.sub(r"[^a-z\s]", "", text)
text = re.sub(r"\s+", " ", text).strip()
print(text)



import string
text = input("enter text: ")
clean = ""
for ch in text:
    if ch not in string.punctuation and not ch.isspace():
        clean += ch.lower()
if clean == clean[::-1]:
    print("palindrome")
else:
    print("not palindrome")



from collections import Counter
import re
stopwords = {"the", "is", "a", "an", "and", "of", "to", "in", "on", "for"}
text = input("enter text: ")
words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
words = [word for word in words if word not in stopwords]
frequency = Counter(words)
print("top 5 keywords:", frequency.most_common(5))



import re
dictionary = {
    "hello",
    "world",
    "python",
    "program",
    "computer",
    "student",
    "college",
    "software",
    "engineer"
}
text = input("enter text: ")
words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
for word in words:
    if word not in dictionary:
        print("misspelled:", word)



class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("book borrowed")
        else:
            print("book not available")

    def return_book(self):
        self.available = True
        print("book returned")

    def show_details(self):
        print("title:", self.title)
        print("author:", self.author)
        print("year:", self.year)
        print("available:", self.available)


title = input("enter title: ")
author = input("enter author: ")
year = int(input("enter year: "))

b = book(title, author, year)
b.show_details()
b.borrow()
b.show_details()
b.return_book()



class bankaccount:
    counter = 1000

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        bankaccount.counter += 1
        self.account_number = bankaccount.counter

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdraw successful")
        else:
            print("insufficient balance")

    def transfer(self, other, amount):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
            print("transfer successful")
        else:
            print("insufficient balance")

    def display(self):
        print("account number:", self.account_number)
        print("account holder:", self.account_holder)
        print("balance:", self.balance)


name1 = input("enter first account holder: ")
name2 = input("enter second account holder: ")

a1 = bankaccount(name1, 5000)
a2 = bankaccount(name2, 2000)

a1.deposit(1000)
a1.withdraw(500)
a1.transfer(a2, 1000)

a1.display()
a2.display()



class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("employee id:", self.employee_id)
        print("salary:", self.salary)


name = input("enter name: ")
age = int(input("enter age: "))
employee_id = input("enter employee id: ")
salary = float(input("enter salary: "))

e = employee(name, age, employee_id, salary)
e.display()



class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary


class manager(employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("employee id:", self.employee_id)
        print("salary:", self.salary)
        print("department:", self.department)
        print("team size:", self.team_size)


name = input("enter name: ")
age = int(input("enter age: "))
employee_id = input("enter employee id: ")
salary = float(input("enter salary: "))
department = input("enter department: ")
team_size = int(input("enter team size: "))

m = manager(name, age, employee_id, salary, department, team_size)
m.display()



class calculator:
    def add(self, a, b=0, c=0, d=0):
        return a + b + c + d


calc = calculator()

print("two numbers:", calc.add(10, 20))
print("three numbers:", calc.add(10, 20, 30))
print("four numbers:", calc.add(10, 20, 30, 40))
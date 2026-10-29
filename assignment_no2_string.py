s = input("enter a string: ")
count = 0
for ch in s:
    count += 1
print(count)



s = input("enter a string: ")
vowels = consonants = digits = spaces = special = 0
for ch in s:
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print(vowels, consonants, digits, spaces, special)



s = input("enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)



s = input("enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("palindrome")
else:
    print("not palindrome")



s = input("enter a string: ")
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("uppercase:", upper)
print("lowercase:", lower)



s = input("enter a string: ")
a = input("enter character: ")
b = input("enter new character: ")
result = ""
for ch in s:
    result += b if ch == a else ch
print(result)



s = input("enter a string: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print(result)



s = input("enter a string: ")
ch = input("enter character: ")
count = 0
for x in s:
    if x == ch:
        count += 1
print(count)



s = input("enter a string: ")
print("first:", s[0])
print("last:", s[-1])



s = input("enter a string: ")
for ch in s:
    print(ch, ord(ch))



s = input("enter a sentence: ")
words = s.split()
print(len(words))



s = input("enter a sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)



s = input("enter a sentence: ")
words = s.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print(shortest)



s = input("enter a sentence: ")
words = s.split()
result = ""
for word in words:
    result += word[0].upper() + word[1:] + " "
print(result)



s = input("enter a string: ")
result = ""
for ch in s:
    if s.count(ch) > 1 and ch not in result:
        result += ch
print(result)



s = input("enter a string: ")
done = ""
for ch in s:
    if ch not in done:
        print(ch, s.count(ch))
        done += ch



s1 = input("enter first string: ")
s2 = input("enter second string: ")
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not anagram")



s = input("enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)



s = input("enter main string: ")
sub = input("enter substring: ")
if sub in s:
    print("substring exists")
else:
    print("substring does not exist")



s = input("enter a sentence: ")
word = input("enter word: ")
count = 0
for x in s.split():
    if x == word:
        count += 1
print(count)



password = input("enter password: ")
upper = lower = digit = special = False
for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True
if len(password) >= 8 and upper and lower and digit and special:
    print("valid password")
else:
    print("invalid password")



s = input("enter a string: ")
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
result += s[-1] + str(count)
print(result)



s = input("enter a string: ")
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
result += s[-1] + str(count)
print(result if len(result) < len(s) else s)



s = input("enter a string: ")
max_count = 0
result = ""
for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        result = ch
print(result)



s = input("enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
values = sorted(set(freq.values()), reverse=True)
for ch in s:
    if freq[ch] == values[1]:
        print(ch)
        break



s = input("enter a message: ")
shift = int(input("enter shift: "))
result = ""
for ch in s:
    if ch.isalpha():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch
print(result)



email = input("enter email: ")
if "@" in email and "." in email and email.count("@") == 1:
    print("valid email")
else:
    print("invalid email")



s = input("enter a paragraph: ")
words = s.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
for word in freq:
    print(word, freq[word])



s = input("enter a sentence: ")
words = s.split()
result = ""
i = len(words) - 1
while i >= 0:
    result += words[i] + " "
    i -= 1
print(result.strip())



s1 = input("enter first string: ")
s2 = input("enter second string: ")
if len(s1) == len(s2) and s2 in s1 + s1:
    print("yes")
else:
    print("no")
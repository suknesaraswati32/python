# s=input("enter your string")
# count=0
# for i in s:
#   count=count+1
# print(count)  

# s=input("enter your string")
# voels=0
# digit=0
# for i in s:
#   if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
#     voels+=1
#   if i in range(1,10):  
#     digit+=1
# print(digit,voels)    

# s=input("enter your string")
# n=len(s)-1
# s2=""
# while n>=0:
#   s2 += s[n]
#   n=n-1
# print(s2)    


# s=input("enter your string")
# orignal=s
# n=len(s)-1
# revstring=""
# while n>=0:
#   revstring +=s[n]
#   n=n-1
# if revstring == orignal:
#   print("the string is palindrome")   
# else:
#   print("string is not palindrome")  


# s=input("enter a string")
# upper=0
# lower=0
# for i in s:
#   if(i==i.upper()):
#      upper+=1
#   else:
#     lower+=1
# print(upper)       
# print(lower)

# s=input("enter a string")
# ch=input("enter char")
# s2=s.replace(ch,"*")
# print(s2)   

# s=input("enter a string")
# s2=s.replace(" ","")
# print(s2)

    
# s=input("enter a string") 
# ch=input("enter the charcter")
# freq=0
# for i in s:
#   if(i==ch):
#     freq+=1
# print(freq)    

# s=input("enter a string") 
# n=len(s)
# first=s[0]
# last=s[n-1]
# print(first)
# print(last)

# dict={}
# s=input("enter a string") 
# asci=""
# for ch in s:
#   asci=ord(ch)
#   dict[ch]=asci
# print(dict)  

# s=input("enter a string") 
# s2=s.strip()
# word=1
# for i in s2:
#   if i==" ":
#     word+=1
# print(word)    

# s = input("Enter a string: ")
# words = s.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest word:", longest)
# print("Length:", len(longest))


# s = input("Enter a string: ")
# words = s.split()
# shortest = words[0]
# for word in words:
#     if len(word) < len(shortest):
#         shortest = word
# print("shortest word:", shortest)
# print("shortest:", len(shortest))

# s=input("enter a string")
# s2=s.title()
# print(s2)


# s2=set()
# s=input("enter a string")
# for i in s:
#   if i not in s2: 
#     s2.add(i)
#   else:
#     print(i)

dict={}
# s=input("enter a string")
# for i in s:
#   if i in dict:
#     dict[i]+=1
#   else:
#     dict[i]=1
# print(dict)      

# dict={}
# s1=input("enter a string")
# s2=input("enter a string")

# for i in s1:
#   if i in dict:
#       dict[i]+=1
#   else:
#       dict[i]=1
# for i in s2:
#   if i in dict:
#       dict[i]-=1
#       if dict[i] == 0:
#         del(dict[i])
# if(len(dict)==0):
#   print("given string is anagram")    
# else:
#   print("given string is not anagram")
  
    
# s2=set()  
# s=input("enter a string")
# for  i in s:
#   s2.add(i)
# print(s2)


s=input("enter a string")
substr=input("enter the substring")

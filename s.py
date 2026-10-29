with open('text.txt','r') as f:
  text=f.read()
list=text.split()
count=0
freq={}
for word in list:
  if word not in freq:
    freq[word]=1
  else:
    freq[word]+=1
  count=count+1
print(freq)  
print(count)
for key,val in freq.items():
  if(val>=1):
    print(key,":",val)
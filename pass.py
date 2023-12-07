words=input("Enter something: ")
i={}
for word in words:
    if word not in i:
        i[word]=1
    else:
        i[word]+=1
print(i)
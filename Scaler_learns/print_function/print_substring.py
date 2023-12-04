def worldslicing(A,B,C):
    return A[B:C+1]

word=input("Enter word to slice: ")
num1=int(input("Enter starting index: "))
num2=int(input("Enter ending index: "))

result=worldslicing(word,num1,num2)

print(result)
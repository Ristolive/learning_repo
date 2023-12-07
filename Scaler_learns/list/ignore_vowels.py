word =input("Enter a word: ")
vowels="aeoui"
letters=[i for i in word if i not in vowels]
for letter in letters:
    print(letter, end=" ")
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

word1 = sorted(word1.lower().replace(" ",""))
word2 = sorted(word2.lower().replace(" ",""))

if word1 == word2:
    print("Anagrams")
else:
    print("Not anagrams")


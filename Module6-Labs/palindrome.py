text = "Eleven animals I slam in a net"
t = []

text = text.lower()

for l in text:
    if l.isspace():
        continue
    t.append(l)

sorted = list(reversed(t))

if sorted == t:
    print("It's a palindrome.")
else:
    print("It's not a palindrome")

"""text = input("Enter text: ")

# remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome")
else:
	print("It's not a palindrome")"""

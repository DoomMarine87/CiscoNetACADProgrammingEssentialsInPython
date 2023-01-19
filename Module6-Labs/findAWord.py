"""Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any 
characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside 
the second string?

For example:

    if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
    if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this 
    order)"""

#My version - string1 and string2 have to have the exact same number of the same letters.  The for loop tests this and if the
#letter is found removes it from string2 so that it isn't checked against twice.
string1 = input("Please enter word 1: ").lower()
string2 = input("Please enter your string: ").lower()
newString = ""

for i in string1:
    if i in string2:
        string2 = string2.replace(i,"",1)
        newString += i

if newString == string1:
    print("Yes")
else:
    print("No")

#More generic version, which returns "Yes" if string1 has multiple occurences of a certain letter even if string2 has only one.
#uses the find method.
"""string1 = "donor"
string2 = "Nabucodonosor"
newString = ""

string1 = string1.lower()
string2 = string2.lower()

for i in string1:
    if string2.find(i,-1):
        newString += i

print(string1, newString)
if newString == string1:
    print("Yes")
else:
    print("No")"""




    


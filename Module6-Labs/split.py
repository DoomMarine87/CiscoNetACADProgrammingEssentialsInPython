"""You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

    it should accept exactly one argument - a string;
    it should return a list of words created from the string, divided in the places where the string contains whitespaces;
    if the string is empty, the function should return an empty list;
    its name should be mysplit()

Use the template in the editor. Test your code carefully.
Expected output
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]"""


def mysplit(strng):
    list(strng)
    newlist = []
    word = ""

    for ch in range(len(strng) -1):
        if strng[ch] != " " and strng[ch+1] != " ":
            word += strng[ch]
        elif strng[ch] != " " and strng[ch+1] == " ":
            word += strng[ch]
            newlist.append(word)
            word = ""
          
    if word != "":
        if strng[-1] != " ":
            word += strng[-1]
            newlist.append(word)
    
    return newlist


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
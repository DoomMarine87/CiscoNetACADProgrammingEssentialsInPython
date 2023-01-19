text = input("Please enter your text here: ")
interval = 0

while interval ==0:
    try:
        interval = int(input("Please enter input value here: "))
        if interval not in range(1,26):
            raise ValueError
    except ValueError:
        interval = 0
        if interval == 0:
            print("Bad interval value.  Please enter a number between 1 and 26.")

cipher = ""

for i in text:
    if not i.isalpha():
        char = i
        cipher += char
    elif ord(i) >= ord("A") and ord(i) <= ord("Z"):
        char = ord(i) + interval
        if char > ord("Z"):
            char = ord(i) - 26 + interval
        cipher += chr(char)
    elif i.isalpha():
        char = ord(i) + interval
        if char > ord("z"):
            char = ord(i) - 26 + interval
        cipher +=chr(char)
    
print(cipher)

"""input - abcxyzABCxyz 123
        2
output -cdezabCDEzab 123

input - The die is cast
        25
ouput - Sgd chd hr bzrs"""
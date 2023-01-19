"""Your task is to write a function able to input integer values and to check if they are within a specified range.

The function should:

    accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
    if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the 
    user to input the value again;
    if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is 
    not within permitted range (min..max) and ask the user to input the value again;
    if the input value is valid, return it as a result."""


def read_int(prompt, min, max):
    while True:
        try:  
            integer = int(input("Enter integer: "))
            if integer >= min and integer <= max:
                return integer
            else:
                raise
            
        except ValueError:
            print("Error: wrong input")
        
        except:
            print(f"Error: the value is not within permitted range ({min}..{max})")
        
        
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

"""Test data

Test your code carefully.

This is how the function should react to the user's input:
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1"""
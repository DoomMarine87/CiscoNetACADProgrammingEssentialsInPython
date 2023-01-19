"""We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's 
a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be 
using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

    objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the 
    following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10; the class should be equipped with 
    parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second 
    respectively.

Use the following hints:

    all object's properties should be private;
    consider writing a separate function (not method!) to format the time string.

Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.
"""

class Timer:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        if self.__hour < 10:
            self.__hour = str(self.__hour)
            self.__hour = list(self.__hour)
            self.__hour.insert(0, "0")
            self.__hour = "".join(self.__hour)
        if self.__minute < 10:
            self.__minute = str(self.__minute)
            self.__minute = list(self.__minute)
            self.__minute.insert(0, "0")
            self.__minute = "".join(self.__minute)
        if self.__second < 10:
            self.__second = str(self.__second)
            self.__second = list(self.__second)
            self.__second.insert(0, "0")
            self.__second = "".join(self.__second)
    
        self.__hour = str(self.__hour)
        self.__minute = str(self.__minute)
        self.__second = str(self.__second)

        newTime = self.__hour + ":" + self.__minute + ":" + self.__second

        self.__hour = int(self.__hour)
        self.__minute = int(self.__minute)
        self.__second = int(self.__second)
        
        return newTime     

    def next_second(self):
        self.__second = self.__second + 1
        if self.__second > 59:
            self.__second = 0
            self.__minute = self.__minute + 1
        if self.__minute > 59:
            self.__minute = 0
            self.__hour = self.__hour + 1
        if self.__hour > 23:
            self.__hour = 0

    def prev_second(self):
        self.__second = self.__second - 1
        if self.__second < 0:
            self.__second = 59
            self.__minute = self.__minute - 1
        if self.__minute < 0:
            self.__minute = 59
            self.__hour = self.__hour - 1
        if self.__hour < 0:
            self.__hour = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

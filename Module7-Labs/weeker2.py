def chooseDay(day):
    weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in range(len(weekDays)):
        if day in weekDays:
            day = weekDays[d]

def add_days (interval, day):
    weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    if day == "Mon":
        plusDay = 0
    elif day == "Tue":
        plusDay = 1
    elif day == "Wed":
        plusDay = 2
    elif day == "Thu":
        plusDay = 3
    elif day == "Fri":
        plusDay = 4
    elif day == "Sat":
        plusDay = 5
    elif day == "Sun":
        plusDay = 6
    
    day = interval % 7

    return weekDays[day + plusDay]

print(add_days(15, "Mon"))

#Mon + 15 = Tue

def subtract_days(interval):
    weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = interval % 7


    return weekDays[-day]

print(subtract_days(22))

#Mon - 23 = Sun






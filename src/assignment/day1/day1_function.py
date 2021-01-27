"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""


def is_on_list(days_arr, days):
    if days in days_arr:
        return True


def get_x(days_arr, position):
    if len(days_arr) < position:
        return "Empty"
    return days_arr[position]


def add_x(days_arr, days):
    return days_arr.append(days)


def remove_x(days_arr, days):
    if days not in days_arr:
        return
    return days_arr.remove(days)


# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "aa")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #

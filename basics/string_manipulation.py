# https://www.w3schools.com/python/python_ref_string.asp
lower_string = "my string is awesome"
upper_string = "MY STRING IS AWESOME"

# Converts the first character to upper case
lower_string_capitalize = lower_string.capitalize()

# Converts string into lower case
upper_string_casefold = upper_string.casefold()

# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
find_string = lower_string.find("m", 5, 15)

# Joins the elements of an iterable to the end of the string
join_string = "WOW".join(lower_string)

# Split the string, using comma, followed by a space, as a separator returns list
split_string = lower_string.split(" ")

# Make the lower case letters upper case and the upper case letters lower case:
swapcase_string = lower_string.swapcase()

# Make the first letter in each word upper case
title_string = lower_string.title()

startswith_string = lower_string.startswith("my",2,7)

arr = [lower_string, 
    upper_string, 
    lower_string_capitalize, 
    upper_string_casefold,
    find_string, 
    join_string, 
    split_string,
    swapcase_string, 
    title_string,
    startswith_string]

for x in arr:
    print(x)


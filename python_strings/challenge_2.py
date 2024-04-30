###################################################################

# challenge 1 := Consider the following string declaration which is part of the output of a Linux command.
# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3';
# sIndex = my_str.find("b4");
# print(my_str[sIndex:]);
# #  or
# my_str_list = my_str.split();
# print(my_str_list[-1])

###################################################################

# challenge 2 := Display the following strings literally:
# It displayed: "You've got an error!"
# \n means a new line.
# \ is known as the escape character.

# print("You've got an error! \n" + "\\n  means a new line. \n" + "\ is known as escape character");

###################################################################

# challenge 3 := Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
# The user will be prompted to enter the value in ft.
# Display the value in cm with 2 decimals, formatted using an f-string.

# ftValue = float(input("enter the value in foot"));
# print(f"the value is : {ftValue * 30.48:.2f} cm")

###################################################################

# challenge 4 :=
# inp_str = input("enter your string");
# rev_inp_str = inp_str[::-1];
# print(inp_str == rev_inp_str)

###################################################################

# challenge 5 := Write a Python script to get a string made of the first and the last 2 chars from a given string entered by the user.
# inp_str = input("enter string");
# print(inp_str[0:2] + inp_str[-2:])

###################################################################

# challenge 6 := Write a Python program to get a string from a given string where all occurrences of its first character have been changed to '$', except the first character itself.

# my_str = "mama";
# new_str = my_str[1:];
# print(my_str[0] + new_str.replace(my_str[0] , "$"))

###################################################################

# challenge 7 := Write a Python program to remove the nth index character from a nonempty string.
# my_str = "hello";
# index = 1;
# print(my_str[0:index] + my_str[index+1 : ])

###################################################################

# challenge 8 := Write a Python script that prompts the user for the radius of a circle and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
# Using an f-string display the area of the circle with 4 decimal places.

# radius = float(input("enter the radius of circle"));
# PI = 3.14;
# area = PI * radius * radius;
# print(f"area : {area:.4f}")

###################################################################

# challenge 9 := Write a Python script that finds all occurrences of a substring in a given string by ignoring the letter case.

# my_str = "hello this is my Is very iS charming";
# sub_str = "is";
# count = my_str.lower().count(sub_str.lower());
# print(f" no. of times {sub_str} occurs in whole string is : {count}");

###################################################################

# challenge 10 := Write a Python script that displays a number with a comma (,) as the thousands separator (US and UK format) and with a period(.) as the thousands separator (EU format).

# inp = 12384756982
# inp_comma = f'{inp:,}'
# print(inp_comma)
# print(inp_comma.replace(",","."))

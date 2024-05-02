###############################################################################
# Challenge  1 :  Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.

# num = int(input("enter a number :"));
# for i in range(1,num + 1):
#     if(num % i == 0):
#         print(i);

###############################################################################
# Challenge  2 : Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.
# x = int(input("enter x : "));
# y = int(input("enter y : "));
# for i in range(2 ,x ):
#     if(i*i == x):
#         print(i);


###############################################################################
# Challenge  3 : Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
# input_str = input("enter your string :");
# vowels = ['a','e','i','o','u'];
# vow_count = 0;
# for ch in input_str :
#     if (ch in vowels):
#         print(ch);
#         vow_count += 1;
# print(f"total vowel in string are : {vow_count}");


###############################################################################
# Challenge  4 : Write a Python script that checks if a triangle is equilateral, isosceles or scalene.
# a = int(input("enter side a"));
# b = int(input("enter side b"));
# c = int(input("enter side c"));
# if (a==b):
#     if(b==c):
#         print("equilateral");
#     else:
#         print("iso");
# elif(a==c):
#     print("iso");
# else:
#     print("sc");


###############################################################################
# Challenge  5 :  print this pattern

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# for i in range(5):
#     for j in range(i):
#         print("*" , end="");
#     print(" ");
#
# for i in range (5):
#     for j in range(5-i):
#         print("*" , end = "");
#     print(" ");


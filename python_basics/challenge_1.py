# challenge 1  :=  Declare variables for the following types: int, float, bool, string, list.    Print out the variables and their types at the terminal.
a = 10;
name = "parmo";
flag = True;
fruits = ["apple" , "mango" , "banana"];
city = {"paris" , "london" , "chicago"};
person1 = {"name":"john" , "age":"21" , "location" : "NY"};
print(type(a) , a);
print(type(name) , name);
print(type(fruits) , fruits);
print(type(city) , city);
print(type(person1) , person1);

# challenge 2 :=  Change this script so that it follows the Python naming and style conventions described in PEP8
my_name = 'Andrei'
value=100
# This is
# an example of a multiline
# comment in Python.
my_str = 'Hello'
print(my_str)


# challenge 3 := This script contains some syntax errors. Modify the script so that it runs without any errors.
best_friend = "Anne"
print('My best friend is ', best_friend)
age = 18
age = 10;
print(age )
a, b = '10', '20'
print(a + b)
print('To comment a line of code you # at the beginning of the line.')

# challenge 4 := Add parenthesis to change the order of operations so that a is 1.0
a = (16 / (2 + 6) / 2) ** 2
print(a)

# challenge 5 := Write a Python script that calculates how many IPv6 addresses are available. You can also include reserved IP addresses.
print(2**128);


# challenge 6 := A company's revenue is 45,897,513.  Calculate the company's profit if the profit represents 12.7% of the revenue.
revenue = 45897513;
profitPer = 12.7;
pr = revenue * 12.7 / 100;
profit = (revenue /100) * profitPer;
print( format(profit , ".2f"));


# ##########################################################################
# challenge 1 : Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.
# l  = [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5];
#
# def unique_list(l):
#      l1 = set(l);
#      return l1;
#
# print(unique_list(l));

# ##########################################################################
# challenge 2 : Write a Python function to check whether a number is perfect or not. The function should return True if the number is perfect and False otherwise.

# def check_perfect(num):
#     div_sum = 0;
#     for n in range(1,num):
#         if num%n == 0:
#             div_sum += n;
#
#     if div_sum == num:
#         return True;
#     else:
#         return False;
#
# num = int(input("enter your number :"));
# print(check_perfect(num));


# ##########################################################################
# challenge 3 : Write a function that returns the factorial of a number n which is the function's argument.

# def fact(num):
#     fac = 1;
#     for n in range(1,num+1):
#         fac *= n;
#     return fac;
#
# num = int(input("enter number for fact :"));
# print(fact(num));


# ##########################################################################
# challenge 4 : Create a function that takes an integer as an argument and returns True if its a prime number and False otherwise.

# def check_prime(num):
#     flag = True;
#     for n in range(2,num):
#         if(num%n==0):
#             flag = False;
#     return flag;
#
# num = int(input("enter number for checking prime"));
# print(check_prime(num));


# ##########################################################################
# challenge 5  : Write a function called fibo that takes an integer greater than 10 as an argument and returns the Fibonacci series between 0 and the function's argument.

# def fibo(num):
#     l1 = [0,1];
#     sum = 0 ;
#
#     while sum < num:
#         sum =  (l1[-1] + l1[-2]);
#         l1.append(sum);
#
#     return l1[0:-1];
#
# num = int(input("enter num"));
# print(fibo(num));


# ##########################################################################
# challenge 6  : Define a function that draws a Christmas tree using asterisks (*). The function takes a single argument, which is the height of the tree.

# def tree_print(num):
#     for i in range(num):
#         for j in range(i):
#             print("*", end="");
#         print(" ");
#
# num = int(input("enter height of tree : "));
# tree_print(num);
#




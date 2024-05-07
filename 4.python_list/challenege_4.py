##################################################################################


# Challenge #1 : Create a Python script that removes all the occurrences of a given element of a list.
# n = 1;
# l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]
#
# print(f"list before removing {n} : {l1}");
#
#
# while n in l1:
#     # if s == st:
#     l1.remove(n);
#
# print(f"list after removing {n} : {l1}");


##################################################################################


# Challenge #2 :  Create a Python script that removes all the elements of a list that are duplicates.
# l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]
# u_l1 = [];
# for i in l1:
#     if i not in u_l1:
#         u_l1.append(i);
#
# print(f"unique list : {u_l1}");


##################################################################################


# Challenge #3 :  Consider the following string: nums = '10,20,30,40,50' Create a Python script that creates a list of integers from the string.
# nums = '10,20,30,40,50';
# l1 = nums.split(",");
# for n in l1:
#     n = int(n);
# int_l1 = [int(n) for n in l1];
# print(f"type of l1 : {type(int_l1)}");
# print(f"list one : {int_l1}");


##################################################################################


# Challenge #4 : Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
# l1 = list();
# for n in range(1500,3201):
#     if (n % 7 == 0) and (n%5 != 0 ):
#         l1.append(str(n));
#
# print(",".join(l1));


##################################################################################


# Challenge #5
# Write a program that prompts the user for a long string containing multiple words separated by whitespaces and prints back the same string with the words in backward order.
# st = "My name is Andrei";
# l1 = st.split(" ");
# st = " ".join(reversed(l1));
# print(st);


##################################################################################


# Challenge #6 : Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# st = "green-red-yellow-black-white";
# l1_st = st.split("-");
# l1_st.sort();
# print("-".join(l1_st));


##################################################################################


# Challenge #7 : Write a Python program that accepts as input a sequence of words separated by one or more whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.
# st = "I love cat and dogs";
# l1_st = st.split(" ");
# ans_st = " ";
# for item in l1_st:
#     print(ans_st.join(reversed(item)) , end="  ");



##################################################################################


# Challenge #8 : Create an alternative solution for the previous challenge using list comprehension.
# st = "I love cat and dogs";
# l1 = st.split(" ");
# l1 = [w[::-1] for w in l1]
# new_str = ' '.join(l1)
# print(new_str)


##################################################################################


# Challenge #9 : # Consider a list of words(strings). Write a Python script that generates a list of tuples where the first element of the
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash'];
# words_and_length = [(w, len(w)) for w in words];
# print(words_and_length);
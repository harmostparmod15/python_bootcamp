#  ################################################

# Challenge #1 : Consider this text file that contains multiple duplicate MAC addresses.

# with open("./macs.txt" ) as f:
#     content = list(set(f.read().splitlines()));
#     print(content);
#
# with open("./unique_macs.txt" , "w" , newline="") as f:
#     for mac in content:
#         f.write(str(mac) + "\n");


#  ################################################

# Challenge #2 : Consider this text file that contains multiple duplicate MAC addresses.

# with open("./sample_file.txt") as f:
#     content = list(f.read().splitlines());
#     str_ans = "\n".join(content);
#     print(str_ans)


#  ################################################

#Challenge #4 :  Create a Python function called tail that reads the last n lines of a text file. The function has two arguments: the file name and n (the number of lines to read). This is similar to the Linux `tail` command.

# def tail(file_name , n):
#     """ similar to linux tail command"""
#     with open(file_name) as f:
#         content_list = f.read().splitlines();
#         len_str = len(content_list);
#         first = len_str - n;
#         tmp_list = content_list[first:len_str]
#         for line in tmp_list:
#             print("".join(line));
#
# tail("./sample_file.txt" , 2);


#  ################################################

# Challenge #6
#
# Write a Python program to count the number of lines, words, and characters in a text file. This is similar to the Linux `wc` command. Create a function, if possible.
# def wc(file):
#     with open(file, 'r') as f:
#         # reading the file into a list
#         content = f.read().splitlines()
#
#         lines = len(content)
#
#         words = 0
#         for line in content:
#             words += len(line.split())
#
#         chars = 0
#         for line in content:
#             chars += len(list(line))
#
#         return lines, words, chars
#
# print(wc('sample_file.txt'))


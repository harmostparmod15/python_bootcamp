# try:
#     a = 10;
#     b = 10;
#     print(f" sum of a and b is {a+b}");
# except :
#     print("an exception has occured ");
# else:
#     print("no errors");
# finally:
#     print("program ends here");



#  opening file and handling error

# f = open("./a.txt" , "w");
# try:
#     f.write("hello adding stuff");
# except:
#     print("cannot write to the file");
# else:
#     print("written succesfully");
# finally:
#     print("closing file ......");
#     if not f.closed:
#         f.close();
#
# print("other code lines .........")


# exception handling with proper built-in exceptions
# try:
#     a =10;
#     b = 10;
#     print(f" divide  a by b is {a/b}");
# except ZeroDivisionError as e:
#     print(f"cannot divide by 0 {e.args}");
# except TypeError as e:
#     print(f"type mismatch {e.args}");
# except Exception as e:
#     print("some error occured");
# else:
#     print("no errors");
# finally:
#     print("program ends here");

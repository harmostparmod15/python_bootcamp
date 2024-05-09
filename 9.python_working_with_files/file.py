f = open("./a.txt");

# print(f.tell());
# f.seek(2);
# print(f.tell());
# content = f.read(5);
# print(content);
# # f.close();
# # print(f.closed);

#
# print(f.read());
# print("#"*20);
# print(f.tell());
# f.seek(0);
# print(f.tell());
# print(f.read());
# f.close();


#  recommended way to work with files
# with open("./a.txt") as file :
#     content = file.read();
#     print(content);
#     print(f"is file closed ? {file.closed}");
# print(f"outside of block is file closed ? {file.closed}");


#  reading files into list
# with open("./a.txt") as file:
#     content = file.read().splitlines();
#     print(content);
#
# print("#"*50);
#
# with open("./a.txt") as file:
#     content = file.readlines();
#     print(content);
#
# print("#"*50);
#
# with open("./a.txt") as f :
#     content = list(f);
#     print(content);


#  writing to a file
# with open("./a.txt" , "w") as f:
#     f.write("hello u are welcome");
#
# with open("./a.txt") as f:
#     print(f.read());
#
# with open("./a.txt" , "a") as f:
#     f.write("world \n");
#
# with open("./a.txt") as f:
#     print(f.read());

with open("./a.txt" , "r+") as f:
    f.write("new text 2 ");
    f.seek(0)
    print(f.read());
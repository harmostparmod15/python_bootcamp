# # function
# def my_function():
#     print("my function");
#     x = 10;
#     print(f"10 multiply 8 is : {x * 8}");
#
# my_function();
#


#  function with docstring
# def my_func(name):
    # """ this function says hello to you """
#     print(f"hello {name}");
#
# my_func("john");


#  function with keyword arguments ( kwargs )
# def my_sum(a,b,c):
#     print(a);
#     print(b);
#     print(c);
#
# my_sum(c=5,a=3,b=8);

# def find_sum(a,b,c = 10):
#     return  a+b+c;
#
#
# sum = find_sum(5,4);
# print(f"sum is {sum}")

#  * args
# def avg_num(a , b , *args):
#     return (a+ b + sum(args))/a+b+ len(args);
#
# print(avg_num(3,34,1,3,4,43));

# ** kwargs
# def my_func(**kwargs):
#     print(kwargs);
#     for k ,v in kwargs.items():
#         print(f"key : {k} , value:{v}");
#
# my_func(name="john" , age = "21" , vf="then");

#  lambda expression
#  simple function
# def my_sum(a,b,c):
#     return a+b+c;

# print(my_sum(1,2,3));

# lambda function of upper function
# result = (lambda a,b:a+b)(5,6);
# print(result);
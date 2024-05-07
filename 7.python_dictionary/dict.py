# person = {"name" : "john" , "age":21 , "location" : "USA"};
# print(person);
#
# print(len(person));
#
# person["age"] = 44;
#
# print(person);
#
#
# p_age = person["age"];
# print(f"person age is {p_age}");
#
# person_key = person.keys();
#
# print(f" keys of person dict are : {person_key}");
#
# person_val = person.values();
#
# person_val = list(person_val);
#
# print(f"type of person val : {type(person_val)} , and values : {person_val}");
#
#
# person_items = person.items();
#
# print(f"items of person dic : {person_items}");
#
#
# print(44 in person_val);
#
#
# for key in person.keys():
#       print(f"person keys are {key}");
# for val in person.values():
#       print(f"person values are {val}");
# for k,v in person.items():
#       print(f"person items are {k} : {v}");




# names = {"gt" , "hey" , "bye" };
# names = { n.capitalize() for n in names};
# print(f"capitalzie names are  {names}")
#
# d1 = {'a':1 , 'b':2 , 'c':3};
# d1 = { k*2 : v*2 for k,v in d1.items()};
# print(f"doubled key and value of dictionary : {d1}")
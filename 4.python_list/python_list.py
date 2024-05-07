# list1 = [1,2,4,5.4,"hello" , ['a','b','c']];
#
# list1 += [4,5];
#
# print(list1);
#
# list1[0:2] = [5,4];
#
# print("hello" in list1);
#
# print(list1);


### add elements to list
    # l1 = [1.2,3,4];
    # l1.append(5);
    # l1.extend([6,7,8]);
    # l1.insert(len(l1) , 9);
    #
    # print(f"list after using all 3  methods of adding elements into list ", l1);


### remove elements from the list
# l2 = [1,2,3,2,2];
# print(f"list {l2}");
# l2.clear();
# print(f"list after clear {l2}");

# x =  l2.pop();
# print(f"after removing last element from the list {l2}");

# l2.remove(2);
# print(l2)

### get index of  elements from the list
# l = [1,2,3,4,42,3,4,5];
# x = l.index(42);
# print(f"index of 42 is : {x}");
# cnt  = l.count(3);
# print(f"number of times 3 appear in list is : {cnt}");
# print(f"5 is present in list or not ? : {5 in l}");
#
# l.reverse();

# print(f"reversed list is : {l}");

# maxL = max(l);
# minL = min(l);
# print(f"maximum element in list is : {maxL} , and minimum alement in list is : {minL}");

# l1 = [1,2,3,4,5];
# l1_copy = [ch for ch in l1];
# print(f"copy of list is : {l1_copy}");
# db_l1 = [ num*2 for num in l1];
# print(f"double li : {db_l1}");
# even_no = [n for n in l1 if n%2==0];
# print(f"even numbers list generate from l1 {even_no}");
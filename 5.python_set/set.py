# s1 = {1,2,3 , 'a', 'b', 'hy'};
# s1.add((10,20));
# print(s1);
#
#
# str1 = "hhhh";
# st2 = set(str1);
# print(st2);
#
# s1_copy = s1.copy();
# print(s1_copy);
# s1_copy.add(4);
# print(s1);
# print(s1_copy);
#
# print(f"intersection of 2 sets {s1.intersection(s1_copy)}");
#
# uncommon = s1.symmetric_difference(s1_copy);
#
# print(f"uncommon elements of both set {uncommon}");
#
# union_set = s1.union(s1_copy);
# union_set_v2 = s1 | s1_copy;
#
# print(f"union of both set is {union_set}");
# print(f"union of both set v2 {union_set_v2}");
#
# print(s1.isdisjoint(s1_copy));
#
#
# print(2 in s1);
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}


my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)  # Output: set()


original_set = {1, 2, 3}
copied_set = original_set.copy()


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}


my_set = {1, 2, 3, 4}
my_set.discard(3)
print(my_set)  # Output: {1, 2, 4}


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3, 4}


set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(is_subset)  # Output: True


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
is_superset = set1.issuperset(set2)
print(is_superset)  # Output: True


my_set = {1, 2, 3, 4, 5}
popped_item = my_set.pop()
print(popped_item)  # Output: 1 or 2 or 3 or 4 or 5 (یکی از عناصر تصادفی)


my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4}


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}


my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
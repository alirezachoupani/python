my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}


original_dict = {'a': 1, 'b': 2, 'c': 3}
copied_dict = original_dict.copy()


keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}


my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)  # Output: 2


my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])


my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])


my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_value = my_dict.pop('b')
print(popped_value)  # Output: 2


my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_item = my_dict.popitem()
print(popped_item)  # Output: ('c', 3) (ممکن است در پایتون 3.7 و بعدی، جفت خروجی متفاوت باشد)


my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.setdefault('d', 4)
print(value)  # Output: 4
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


my_dict = {'a': 1, 'b': 2}
new_items = {'c': 3, 'd': 4}
my_dict.update(new_items)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])
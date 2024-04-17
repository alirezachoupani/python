# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # خروجی: [1, 2, 3, 4]


# my_list = [1, 2, 3, 4, 5]
# print("Before clear:", my_list)

# my_list.clear()
# print("After clear:", my_list)



# original_list = [1, 2, 3, 4, 5]
# # کپی کردن لیست
# copied_list = original_list.copy()
# print(copied_list)    # Output: [1, 2, 3, 4, 5]


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)  # Output: [1, 2, 3, 4, 5, 6]


# my_list = [10, 20, 30, 20]
# count = my_list.count(20)
# print(count)  # خروجی: 2


# my_list = [10, 20, 30, 40, 50]
# index = my_list.index(30)
# print(index)  # Output: 2


# # ایجاد یک لیست
# my_list = [10, 20, 30, 40, 50]

# # حذف و بازگرداندن آخرین عنصر
# popped_element = my_list.pop()
# print("آخرین عنصر حذف شده:", popped_element)
# print("لیست بعد از حذف:", my_list)

# # حذف و بازگرداندن عنصر در شماره فهرستی 2
# popped_element = my_list.pop(2)
# print("عنصر با شماره فهرستی 2 حذف شده:", popped_element)
# print("لیست بعد از حذف:", my_list)



# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)
# print(my_list)  # Output: [1, 2, 4, 5]


# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)  # Output: [5, 4, 3, 2, 1]


# my_list = [3, 1, 4, 2, 5]
# my_list.sort()
# print(my_list)  # Output: [1, 2, 3, 4, 5]


my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)  # عدد 10 را در اندیس 2 قرار می‌دهیم
print(my_list)  # خروجی: [1, 2, 10, 3, 4, 5]

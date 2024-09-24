list_fruits = ['banana', 'orange', 'apple', 'lemon','lema']
first_item, second_item, third_item, *rest = list_fruits

print(third_item)
print(rest)


first_number, second_number, third_number, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first_number)
print(second_number)
print(third_number)
print(rest)
print(tenth)


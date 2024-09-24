data_person = ['Gustavo', 23, 'gusjoseloz0803@gmail.com', 'Ing. Sistemas e Informatica']

does_exist = 'gusjoseloz0803@gmail.com' in data_person
print(does_exist)

does_exist = 'gusjoselo@gmail.com' in data_person
print(does_exist)


## Adding Items to a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.append('apple')
print(fruits)

fruits.insert(3, 'ciruelo')
print(fruits)


fruits.remove('ciruelo')
print(fruits)


fruits.pop(2)
print(fruits)


del fruits[1]
## del fruits[1:2]
print(fruits)


fruits.clear()
print(fruits)

fruits.copy()


# syntax
# list3 = list1 + list2

# syntax
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2)


fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
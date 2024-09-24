my_name = 'gustavo'

print(my_name.capitalize())

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`
print(challenge.count('py')) # 1


challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False


challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'


full_name = 'Gustavo Ojeda Lozano'
print(full_name.find('o')) #6
print(full_name.rfind('o')) #19



radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314


print(full_name.index('ta'))
print(full_name.rindex('ta'))


name = 'Gustavo'
number4 = '3.14'
number5 = '3'
print(name.isdecimal())
print(number4.isdigit())
print(number5.isdigit())
print(number5.isnumeric())
print(name.islower())
print(name.isupper())


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'


challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'


challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
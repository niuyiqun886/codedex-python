#message = "hello world"
#print(message)
# message = '牛一群'
# print(message)
# name = "ada lovelace"
# print(name.title())                       ##title()方法将字符串的每个单词的首字母大写
# print(name.upper())                       ##upper()方法将字符串中的所有字母都转换为大写
# print(name.lower())                            ##lower()方法将字符串中的所有字母都转换为小写
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"    ##f-string格式化字符串，使用{}来引用变量
# print(full_name)
# first_name = "niu"
# last_name = "yiqun"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# print(f"hello {name.title()}")
# print("python")
# print("\tPython")                          ##\t表示制表符，输出时会在字符串前添加一个水平制表符，使文本向右缩进
# print("Languages:\nPython\nC\nJavaScript")   ##\n表示换行符，输出时会在字符串中插入一个换行符，使文本分成多行显示
# favorite_language = " python "
# favorite_language = favorite_language.strip()   ##strip()方法用于删除字符串两端的空白字符（包括空格、制表符等）
# favorite_language = favorite_language.lstrip()  ##lstrip()方法用于删除字符串开头的空白字符（包括空格、制表符等）   
# #favorite_language = favorite_language.rstrip() ##rstrip()方法用于删除字符串末尾的空白字符（包括空格、制表符等）
# print(f"{favorite_language}{first_name}")
# nostarch_url = "https://nostarch.com"
# simple_url = nostarch_url.removeprefix("https://") ##removeprefix()方法用于删除字符串开头的指定前缀，如果字符串以该前缀开头，则返回删除前缀后的字符串；否则返回原字符串
# print(simple_url)

# message = "one of Python's strengths is its diverse community."  ##字符串中包含单引号时，可以使用双引号来定义字符串，这样就不需要转义单引号了
# print(message)

#
# name = "Eric"
# message = f"Hello {name}, would you like to learn some Python today?"
# print(message)

# name = "niyiqun"
# print(name.title())
# print(name.upper())
# print(name.lower())
# message = "    Albert_Einstein once said,\n'A person who never made a mistake never tried anything new.'    "
# message = message.strip()
# print(message)
# filename = "python_note.txt"
# print(filename.removesuffix(".txt")) ##removesuffix()方法用于删除字符串末尾的指定后缀，如果字符串以该后缀结尾，则返回删除后缀后的字符串；否则返回原字符串   
# 2+2
# print(2+2)
# #2**3
# print(2**3)
# X = 0.2 + 0.1
# print(X)

# x,y,z = 0,0,0
# print(x,y,z)

#import this
#import time
#print(time.localtime())

#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles)
#print(bicycles[0])  ##列表索引从0开始，bicycles[0]表示列表中的第一个元素
#print(bicycles[0].title())  ##title()方法将字符串的每个
#print(bicycles[1].title())  ##title()方法将字符串的每个
#print(bicycles[2].title())  ##title()方法将字符串的每个
#print(bicycles[3].title())  ##title()方法将字符串的每个
#print(bicycles[0].upper()) ##upper()方法将字符串中的所有字母都转换为大写
#print(bicycles[1].upper()) ##upper()方法将字符串中的所有字母都转换为大写
#print(bicycles[2].upper()) ##upper()方法将字符串中的所有字母都转换为大写
#print(bicycles[3].upper()) ##upper()方法将字符串中的所有字母都转换为大写
#print(bicycles[1:4])
#print(bicycles[-1]) ##负数索引表示从列表末尾开始计数，-1表示列表中的最后一个元素
#message = f"My first bicycle was a {bicycles[0].title()}." ##f-string格式化字符串，使用{}来引用变量
#print(message)


#friend_names = ['niuyiqun','youbei','zhanghonhchao']
#print(friend_names[0],friend_names[1],friend_names[2])
#print(f"{friend_names[0].title()} \nNice to meet you.")
#print(f"{friend_names[2].title()} would like to own a {bicycles[0].title()}")


#修改列表中的元素
#motorcycles = ['honda','yamaha','suzuki']
#print(motorcycles)
#motorcycles[0] = 'ducati'     ##修改列表中的元素，motorcycles[0]表示列表中的第一个元素，将其修改为ducati



#添加元素，创建一个空列表，然后使用append()方法依次添加元素
#motorcycles.append('ducati')  ##append()方法用于在列表末尾添加一个元素，motorcycles.append('ducati')表示在motorcycles列表的末尾添加一个元素ducati
#print(motorcycles)
#motorcycles = []
#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')
#print(motorcycles)

#在列表中插入元素
#motorcycles.insert(0,'ducati') ##insert()方法用于在列表的指定位置插入一个元素，motorcycles.insert(0,'ducati')表示在motorcycles列表的第一个位置插入一个元素ducati
#print(motorcycles)

#从列表中删除元素，使用del语句
#del motorcycles[0]
#print(motorcycles)

#从列表中删除元素，使用pop()语句
#popped_motorcycles = motorcycles.pop() ##pop()方法用于从列表中删除一个元素，并返回该元素的值，motorcycles.pop()表示从motorcycles列表中删除最后一个元素，并将其值赋给变量popped_motorcycles
#print(motorcycles)
#print(popped_motorcycles)

#friend_names.insert(0,'popped_motorcycles')
#print(friend_names)

#last_owned = motorcycles.pop()
#print(f"The last motorcycle I owned was a {last_owned.title()}")


#使用pop()删除任意位置的元素
#first_owned = motorcycles.pop(1)
#print(f"The first motorcycle I owned was a {first_owned.title()}")


#有根据值删除元素，不知道位置，只知道要删除的元素的值，可以使用remove()方法
#too_expensive = 'honda'
#motorcycles.remove(too_expensive) ##remove()方法用于从列表中删除第一个匹配的元素，motorcycles.remove('honda')表示从motorcycles列表中删除第一个值为honda的元素
#print(motorcycles)
#print(f"\nA {too_expensive.title()} is too expensive for me.")


#invited_names = ['baba','mama','yeye','nainai','laolao','laoye']
#print(f"{invited_names[0].title()} is invited to have a dinner with me.")
#print(f"{invited_names[1].title()} is invited to have a dinner with me.")
#print(f"{invited_names[2].title()} is invited to have a dinner with me.")
#print(f"{invited_names[3].title()} is invited to have a dinner with me.")
#print(f"{invited_names[4].title()} is invited to have a dinner with me.")
#print(f"{invited_names[5].title()} is invited to have a dinner with me.")

#print(f"{invited_names[4].title()} cannot come to the dinner because of some reasons.")

#invited_names[4] = 'aunt'
#print(invited_names)

#print(f"{invited_names[0].title()} is invited to have a dinner with me.")
#print(f"{invited_names[1].title()} is invited to have a dinner with me.")
#print(f"{invited_names[2].title()} is invited to have a dinner with me.")
#print(f"{invited_names[3].title()} is invited to have a dinner with me.")
#print(f"{invited_names[4].title()} is invited to have a dinner with me.")
#print(f"{invited_names[5].title()} is invited to have a dinner with me.")

#invited_names.insert(0,'gege')
#invited_names.insert(3,'jiejie')
#invited_names.append('meimei')
#print(invited_names)

#print(f"{invited_names[0].title()} is invited to have a dinner with me.")
#print(f"{invited_names[1].title()} is invited to have a dinner with me.")
#print(f"{invited_names[2].title()} is invited to have a dinner with me.")
#print(f"{invited_names[3].title()} is invited to have a dinner with me.")
#print(f"{invited_names[4].title()} is invited to have a dinner with me.")
#print(f"{invited_names[5].title()} is invited to have a dinner with me.")
#print(f"{invited_names[6].title()} is invited to have a dinner with me.")
#print(f"{invited_names[7].title()} is invited to have a dinner with me.")
#print(f"{invited_names[8].title()} is invited to have a dinner with me.")
#print('I can only invite two people for dinner because of the table I have.')

#print(invited_names)
#name0 = invited_names.pop()
#print(f"Sorry {name0.title()}, I can't invite you to dinner.")
#name1 = invited_names.pop()
#print(f"Sorry {name1.title()}, I can't invite you to dinner.")
#name2 = invited_names.pop()
#print(f"Sorry {name2.title()}, I can't invite you to dinner.")
#name3 = invited_names.pop()
#print(f"Sorry {name3.title()}, I can't invite you to dinner.")
#name4 = invited_names.pop()
#print(f"Sorry {name4.title()}, I can't invite you to dinner.")
#name5 = invited_names.pop()
#print(f"Sorry {name5.title()}, I can't invite you to dinner.")
#name6 = invited_names.pop()
#print(f"Sorry {name6.title()}, I can't invite you to dinner.")
#print(invited_names)
#print(f"{invited_names[0].title()} is still invited to dinner.")
#print(f"{invited_names[1].title()} is still invited to dinner.")
#print(invited_names)
#del invited_names[0:2]
#print(invited_names)


#管理列表
#使用sort()方法对列表进行永久排序
#cars = ['bmw','audi','toyota','subaru']
#print(cars)
#cars.sort()
#print(cars)

#cars.sort(reverse=True)
#print(cars)




#使用sorted()函数对列表进行临时排序
#print("Here is the original list:")
#print(cars)
#print("Here is the sorted list:")
#s_cars = sorted(cars) ##sorted()函数用于返回一个新的列表，该列表是原列表的排序版本，原列表保持不变
#s_cars.sort(reverse=True)
#print(s_cars)
#print("Here is the original list again:")
#print(cars)

#反向打印列表
#cars.reverse() ##reverse()方法用于将列表中的元素反转，cars.reverse()表示将cars列表中的元素反转
#print(cars)


#确定列表长度
#print(len(cars))

#locations = []
#locations.append("japan")
#locations.append("america")
#locations.append("italy")
#locations.insert(0,"fenland")
#print(locations)
##print(sorted(locations))
#locations.sort()
#print(locations)
#locations.reverse()
#print(locations)
#locations.sort()
#print(locations)
#locations.sort(reverse=True)
#print(locations)

#print(f"I wannt to visit {len(locations)} countries.")

#del locations[1]
#print(locations)
#locations.remove("fenland")
#print(locations)

#locations[1] = "nanjing"
#print(locations)

#locations_china = locations.pop(1)
#print(f"I have been to {locations_china.title()}")
#print(locations)
#locations.pop()
#print(locations)

#索引错误
#print(cars[-1])
#print(cars[-2])
#print(cars[4]) #错误的索引，cars列表中没有索引为4的元素，因为索引从0开始，cars列表中只有索引为0、1、2、3的元素，所以会出现IndexError: list index out of range错误
#print(len(cars))
#print(cars[0:4])





#遍历整个列表
#使用for循环打印列表中的元素
#magicians = ['alice','david','carolina']
#for magician in magicians:  #这里选用单复数的形式
#    print(magician)

#for循环执行更多操作
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I can't wait to see your next trick,{magician.title()}.\n")
#print("Thank you, everyone. That was a great magic show! ")

# pizzas = []
# pizzas.append('pepperoni')
# pizzas.append('mushroom')
# pizzas.append('cheese')
# for pizza in pizzas:
#     print(pizza)
#     print("I like {pizza.title()} pizza")
# print("I really love pizza!")

# anaimals = []
# anaimals.append('lion')
# anaimals.insert(0,'tiger')
# anaimals.append('cat')
# for anamil in anaimals:
#     print(f"A {anamil.title()} would make a great pet.\n")
# print("Any of these animals would make a great pet!")

#创建数值列表
#for value in range(1,5):
#     print(value)
#
#numbers = list(range(1,6))
#print(numbers)
#numbers = list(range(1,6))
#numbers.reverse()
#print(numbers)
#
#even_numbers = list(range(2,11,2)) #range()函数的第三个参数表示步长，range(2,11,2)表示从2开始，到11结束，步长为2，即生成一个包含2、4、6、8、10的列表
#print(even_numbers)
#
#squares = []
#for value in range(1,11):
#    squares.append(value**2)
#print(squares)


#对数值列表进行简单的计算
#digits = [0,1,2,3,4,5,6,7,8,9]
#print(min(digits))
#print(max(digits))
#print(sum(digits))


#列表推导式
#squares = [value**2 for value in range(1,11)]
#print(squares)

#练习题
#numbers = list(range(1,21))
#print(numbers)

#numbers_a = [value for value in range(1,1_000_001)]
#print(numbers_a)
#print(min(numbers_a))
#print(max(numbers_a))
#print(sum(numbers_a))

# number_odd = [value for value in range(1,20,2)]
# print(number_odd)
#
# number_odd_1 = []
# for value in range(1,20,2):
#     number_odd_1.append(value)
# print(number_odd_1)
#
# number_odd_2 = list(range(1,20,2))
# for number in number_odd_2:
#     print(number)
#
#
# number_aa_3 = [value for value in range(3,30,3)]
# print(number_aa_3)
#
#
# numbers_x3 = []
# for value in range(1,10):
#     numbersx_3 = value**3
#     numbers_x3.append(numbersx_3)
# print(numbers_x3)

#numbers = [value**3 for value in range(1,11)]
#print(numbers)



#使用列表的一部分
#切片(包含开始不包含结束的点)
#players = ['charles','martina','michael','florence','eli']
#print(players[0:3]) ##切片表示从索引0开始，到索引3结束，但不包括索引3，即切片包含索引0、1、2的元素
#print(players[1:4]) ##切片表示从索引1开始，到索引4结束，但不包括索引4，即切片包含索引1、2、3的元素
#print(players[:4])  ##切片表示从索引0开始，到索引4结束，但不包括索引4，即切片包含索引0、1、2、3的元素
#print(players[2:])  ##切片表示从索引2开始，到列表末
#print(players[-3:]) ##切片表示从索引-3开始，到列表末，即切片包含索引-3、-2、-1的元素
#print(players[0:5:2]) ##切片表示从索引0开始，到索引4结束，但不包括索引4，步长为2，即切片包含索引0、2的元素

#name = players.pop(1)
#print(name)

#遍历切片
#print("Here are the first three players on my team:")
#for player in players[:3]:
#    print(player.title())



#幅值列表
# my_foods = ['pizza','falafel','carrot cake']
# #friend_foods = my_foods[0:2] #如果是[：]就是幅值整个列表 ##切片表示从索引0开始，到索引2结束，但不包括索引2，即切片包含索引0、1的元素
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)


#练习题
# digits = [0,1,2,3,4,5,6,7,8,9]
# print("The first three items in the list are:")
# print(digits[:3])
# print(len(digits))
# print("The last three items in the list are:")
# digit = digits[4:7]
# print(digit)
# print(digits[-3:])


#my_pizzas = []
#my_pizzas.append('pepperoni')
#my_pizzas.append('mushroom')
#my_pizzas.append('cheese')
#print(my_pizzas)

#friends_pizzas = my_pizzas[:]
#friends_pizzas.append('cannoli')
#print(friends_pizzas)


#print("My favorite pizzas are:")
#for my_pizza in my_pizzas:
#    print(my_pizza)

#print("\nMy friends's favorite pizzas are:")
#for friend_pizza in friends_pizzas:
#    print(friend_pizza)

#print(f"My friend's favorite pizza is {friends_pizzas[2].title()}")

#print(f"My friend's favorite pizza is {friends_pizzas.pop(1).title()}")
#print(friends_pizzas)



#元组，定义元组，定义好的元组将不能修改
dimensions = (200,50)
#print(dimensions[0])
#print(dimensions[1])

#遍历元组中所有值,修改元组变量
#print("original dimensions:")
#for dimension in dimensions:
#    print(dimension)

#dimensions = (400,100)
#print("\nModified dimensions")
#for dimension in dimensions:
#    print(dimension)


#print(dimensions)


#练习题
#foods = ("noddles","fish","pork","rice","lamb")
#for food in foods:
#    print(food)

#foods[0] = "liangcai"     #直接报错了

#foods = ("noddles","fish","pork","rice","lamb","liangcai","zhouzi")
#for food in foods:
#    print(food)



#第五章 if语句
#5.1例子
#cars = ["audi","bmw","subaru","toyota"]
#for car in cars:
#    if car == "bmw":
#        print(car.title())
#    else:
#        print("none")

#5.2条件测试
#5.2.1检查是否相等，使用“==”
#car = 'Bmw'
#print(car == 'bmw')
#print(car == "Bmw")
#5.2.2如何在检查时候相等时忽略大小写
#print(car.lower() == "bmw")

#检查是否不等，使用“!=”
#requested_topping = "mushrooms"
#if requested_topping != "anchovies":
#    print("Hold the anchovies")

#5.2.4数值比较
#age = 18
#print(age == 18)


#answers = list(range(1,100,2))
#print(answers)
#answer = 50
#for answer in answers:
#    if answer != 42:
#        print("That is not the correct answer. Please try again!")
#for answer in answers:
#    if 30 < answer < 60:
#        print("This number is smaller than the number of the answer.")
#    else:
#        print("false")

#5.2.5检查多个条件
#01.使用“and”检查多个条件
#age_0 = 22
#age_1 = 18
#print(age_0 >= 21 and age_1 >= 21)
#age_2 = 22
#print(age_0 >= 21 and age_2 >= 21)

#if age_0 >= 21 and age_2 >= 21:
#    print("We can go to the KTV")

#02.使用“or”检查多个条件
#print(age_0 >= 21 or age_1 >= 21)
#print(age_1 >= 21 or age_2 >= 21)

#5.2.6检查特定的值是否不在列表中,使用关键字“in”
#requested_toppings = ["mushroom","onions","pineapple"]
#print("mushroom"in requested_toppings)
#print("pepperoni" in requested_toppings)

#5.2.7检查特定的值是否不在列表中，使用关键字“not in”
#banned_users = ["andrew","carolina","david"]
#user = "marie"
#if user not in banned_users:
#    print(f"{user.title()}, you can post a response if you wish.")
#else:
#    print("I can run")

#练习题
#name = 'yiqun'     
#print("Is name == 'yiqun'? I predict True")
#print(name == "yiqun")

#print("Is name == 'Rick'? I predict False")
#print(name == "Rick")

#yiqun_age = 18
#print(yiqun_age >= 20)
#print(yiqun_age <= 30)
#print(yiqun_age == 18)
#print(yiqun_age != 18)

#color = ["red","green","blue"]
#print("red" in color)
#print("yellow" not in color)
#print(yiqun_age == 18 and "orange" in color )
#print(name == "Rick" or "grape" in color)

#animal = "dog"
#print(animal == "cat")
#print(animal != "cat")

#flower = "Rose"
#print(flower == "rose" )
#print(flower.lower() == "rose")

#age = 18
#print(age == 18)
#print(age != 18)
#print(age>17 and age < 19)
#print(age >= 18 and age <= 20)
#print(age >17 or age < 17)

#number = list(range(1,10))
#print(15 in number)
#print(15 not in number)

#5.3if语句
#5.3.1简单的if语句

#age = 17
#if age >= 18:
#    print("You are old enough to vote!")
#    print("Have you registered to vote yet?")
#else:
#    print("Sorry you are too young to vote.")
#    print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else语句
#age = 12
#ages = list(range(1,20))
#for age in ages:
#if age < 4:
#    print("Your admission cost is 0$.")
#elif age < 18:
#  print("Your admission cost is $25.")
#else:
#    print("Your admission cost $40.")

#age = 12
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 25
#else:
#    price = 40
#print(f"Your admission cost ${price}.")

#使用多个elif代码块
#age = 66
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 25
#elif age < 65:
#    price = 40
#else:
#    price = 20
#print(f"Your admission cost ${price}.")

#省略else代码块
#age = 12
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 25
#elif age < 65:
#    price = 40
#elif age >= 65:
#    price = 20
#print(f"Your admission cost ${price}.")

#5.3.6测试多个条件
#requested_toppings = ['mushrooms','extra cheese']
#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms")
#if 'pepperoni' in requested_toppings:
#    print('Adding pepperoni')
#if 'extra cheese' in requested_toppings:
#    print('Adding extra cheese')
#print("\nFinish making your pizza!")

#练习题
#alien_color = 'green'
#if alien_color == 'green':
#   print('Player gains 5 points.')
#if alien_color == 'red':
#   print('Player gain 10 points.')

#if alien_color == 'green':
#   print("Player kills the green alien, so he gains 5 points.")
#else:
#  print('Player gains 10 points')

#alien = ['green','yellow','red']
#for alien_color in alien:
#    if alien_color == 'green':
#       print('Player gains 5 points.')
#    elif alien_color == 'red':
#       print('Player gains 10 points')
#    elif alien_color == 'yellow':
#       print('Player gains 15 points')

#age = 20
#age = list(range(1,100,5))
#for age in age:
#    print(age)
#    if age < 2:
#        print('这个人是婴儿')
#    elif 2 <= age < 4:
#        print('这个人是幼儿')
#    elif 4 <= age < 13:
#        print('这人是儿童')
#    elif 13 <= age < 18:
#        print('这人是少年')
#    elif 18 <= age < 65:
#        print('这人是中青年人')
#    else:
#        print('这人是老年人')

#fruit_list = ['apple','banana','orange','watermelon']
#avorite_list = fruit_list[:]
#rint(favorite_list)
#if 'apple' in favorite_list:
#    print("I really like apple.")
#if 'banana' in favorite_list:
#    print("I really like banana.")

#5.4使用if语句处理列表
#5.4.1检查特殊元素
#requested_toppings = ['mushrooms','green peppers','extra cheese']
#for requested_topping in requested_toppings:
#    print(f"Adding {requested_topping}.")
#print("\nFinished making your pizza!")

#for requested_topping in requested_toppings:
#    if requested_topping =='green peppers':
#        print("Sorry, we are out of green peppers in right now.")
#    else:
#        print(f"Adding {requested_topping}.")
#print("\nFinished making your pizza!")

#5.4.2确定列表非空
#requested_toppings = []
#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print(f"Adding {requested_topping}.")
#    print("\nFinished making your pizza!")
#else:
#    print("Are you sure you want a plain pizza?")

#5.4.3使用多个列表
#available_toppings = ['mushrooms','olives','green peppers',
#                      'peppperoni','pineapple','extra cheese']
#requested_toppings = ['mushrooms','green peppers','extra cheese','apples']

#for requested_topping in requested_toppings:
#   if requested_topping in available_toppings:
#        print(f"Adding {requested_topping}.")
#    else:
#       print(f"Sorry, we don't have {requested_topping}.")
#print("\nFinshed making your pizza!")

#练习
#admin_names = ['yiqun','liwei','hongchao','xiaoxin','youbei','shichang','xingjia']
#for admin_name in admin_names:
#    if admin_name == 'yiqun':
#        print(f"Hello {admin_name.title()}, would you like to see a status report?")
#    elif admin_name == 'liwei':
#        print(f"Hello {admin_name.title()}, would you like to party?")
#    elif admin_name == 'hongchao':
#        print(f"Hello {admin_name.title()}, would you like to have a dinner with me?")
#    elif admin_name == 'xiaoxin':
#        print(f"Hello {admin_name.title()}, can you help me with this project?") 
#    elif admin_name == 'youbei':
#        print(f"Hello {admin_name.title()}, would you like to go for a walk?")
#    elif admin_name == 'shichang':
#        print(f"Hello {admin_name.title()}, would you like to go for a run?")
#    else:
#        print(f"Hello {admin_name.title()}, thank you for logging in again.")

#if admin_names:
#    for admin_name in admin_names:      #不用for也可以直接用 if admin_names:检查是否为空。用for就会循环了。
#    print(f"There are {len(admin_names)} users in the admin_names list")
#else:
#    print("We need to find some users!")

#检查用户名
#current_users = ['Yiqun','liwei','hongchao','xiaoxin','youbei']
#current_users_lower = [current_users.lower() for current_users in current_users]
#print(current_users_lower)
#new_users = ['shichang','XINGJIA','yiqun','LIWEI','Hongchao']
#new_users_lower = [new_users.lower() for new_users in new_users]
#for new_user_lower in new_users_lower:
#    if new_user_lower in current_users_lower:
#        print(f"The {new_user_lower} is available.")
#    else:
#       print(f"{new_user_lower}, you need to enter a new username.")

#序数
#numbers = list(range(1,10))
#print(numbers)
#for number in numbers:
#    if number == 1:
#        print(f"{number}st")
#    elif number == 2:
#        print(f"{number}nd")
#    elif number == 3:
#        print(f"{number}rd")
#    else:
#        print(f"{number}th")



























































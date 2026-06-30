#字典
#6.1一个简单的字典
#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0['color'])
#print(alien_0['points'])

#6.2使用字典
#6.2.1访问字典中的值
#alien_0 = {'color': 'green'}
#print(alien_0['color'])

#new_point = alien_0['points']
#print(f"You just earned {new_point} points!")
#print(f"You just earned {alien_0['points']} points!")

#添加键值对,相当于是向字典里添加了一个新的键值对
#print(alien_0)

#alien_0['x_positon'] = 0
#alien_0['y_positon'] = 25
#print(alien_0)

#6.2.3从创建一个新的字典开始,可以用来存储用户的数据
#alien_0 = {}
#alien_0['color'] = 'green'
#alien_0['points'] = 5
#print(alien_0)

#6.2.4修改字典中的值,(和修改那个list差不多)
#alien_0 = {"color": "green"}
#print(f"The alien is {alien_0['color']}.")

#alien_0['color'] = 'yellow'
#print(alien_0)
#print(f"The alien is {alien_0['color']}.")


#alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
#alien_0['speed'] = 'fast'
#向右移动外星人
#根据当前速度确定外星人向右移动多远
#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    x_increment = 3

#新位置为旧位置加上移动距离
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print(f"New position: {alien_0['x_position']}")

#删除键值对, 使用del语句,删除后就无法再访问这个键值对了(注意删除后就永久消失了)
#del alien_0['speed']
#print(alien_0)

#6.2.6由类似的对象组成的字典
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#   'edward': 'ruby',
#   'phil': 'python',
#}
#language = favorite_languages['sarah'].title()
#print(f"Sarach's favorite language is {language}.")
#print(favorite_languages['sarah'])
#print(language)

#6.2.7使用get()来访问值
#alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])
#point_value = alien_0.get('points','No point value assigned.')
#print(point_value)

#color_value = alien_0.get('color')
#print(color_value)

#练习
#information = {
#    'first_name': 'Niu',
#    'last_name': 'Yiqun',
#    'age': 18,
#    'city': 'Shenyang'
#}
#print(information['first_name'])
#print(information['last_name'])
#print(information['age'])
#rint(information['city'])

#print(f"{information['first_name']} {information['last_name'].lower()}")

#names = {}
#numbers = list(range(1,6))
#print(numbers)
#names['niuyiqun'] = number[0]
#print(names)
#name = ['niuyiqun','zhangsan','lisi','wangwu','zhaoliu']
#for i in range(0,5):
#    names[name[i]] = numbers[i]
#print(names)


#6.3遍历字典
#6.3.1遍历所有键值对,使用items()方法
#user_0 = {
#    'username': 'efermi',
#    'first': 'enrico',
#    'last': 'fermi',
#}

#for key, value in user_0.items():
#    print(f"key: {key}")
#    print(f"value: {value}")

#for name,age in names.items():
#    print(f"{name.title()} is {age} years old.")

#6.3.2遍历字典中所有的键,使用keys()方法
#for name in names.keys():
#    print(name.title())

#for age in names.values():
#    print(age)

#friend = ['phil','sarah']
#for name in favorite_languages.keys():
#    print(f"Hi {name.title()}.")
#    if name in friend:
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()}, I see you love {language}!")

#if 'erin' not in favorite_languages.keys():
#    print("erin, please take our poll!")

#6.3.3按特定顺序遍历字典中的所有键,使用sorted()函数
#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()}, thank you for taking the poll.")

#favorite_language = sorted(favorite_languages.keys())
#print(favorite_language)

#for values, keys in favorite_languages.items():
#    print(values,keys)

#6.3.4遍历字典中的所有值,使用values()方法，为剔除重复项可以使用set()函数
#print("The following languages have been mentioned:")
#for language in favorite_languages.values():
#    print(language.title())

#输出的相同的python没有了
#for language in set(favorite_languages.values()):
#    print(language.title())

#集合可以使用一对花括号来创建，集合是没有顺序的，所以无法按顺序访问，要先变成list才能访问
#language_set = {'python','ruby','python','c'}
#print(language_set)

#languages = {}
#language = ['python','ruby','python','c']
#print(language)
#ge = [18,19,20,21]

#for i in range(0,4):
#    languages[language[i]] = age[i]
#print(languages)

#练习
#python_zidian = {"if": "如果", "else": "否则", "elif": "否则如果", "while": "当", "for": "对于"}
#for key, value in python_zidian.items():
#    print(f"\n{key}:{value}.")

#river_country = {
#    'nile': 'egypt',
#    'amazon': 'brazil',
#    'yangtze': 'china',}
#for key,value in river_country.items():
#    print(f"The {key.title()} runs through {value.title()}.")
#    print(f"{key.title()}")
#    print(f"{value.title()}")


#print(favorite_languages)
#language_jiancha = {'jen','niyiuqn','sarah'}
#for name in language_jiancha:
#    if name in favorite_languages.keys():
#        print(f"Thank you, {name.title()} for takeing the jiancha.")
#    else:
#        print(f"Please take our jiancha, {name.title()}.")

#6.4嵌套
#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#    print(alien)

#aliens = []
#for alien_number in range(0,30):
#    new_alien = {'color': 'green', 'points':5 ,'speed': 'slow'}
#    aliens.append(new_alien)
#print(aliens)

#for alien in aliens[:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['points'] = 10
#       alien['speed'] = 'medium'
#    elif alien['color'] == 'yellow':
#        alien['color'] = 'red'
#        alien['points'] = 15
#        alien['speed'] = 'fast'

#for alien in aliens[:5]:
#    print(alien)
#print(f"Total number of aliens:{len(aliens)}")

#6.4.2在字典中存储列表
#pizza = {
#    'crust': 'thick',
#    'toppings': ['mushrooms', 'extra cheese'],
#}
#print(f"You ordered a {pizza['crust']}-crust pizza"
#      "with the following toppings:")

#for topping in pizza['toppings']:
#    print(f"\t{topping}")

#favorite_languages = {
#    'jen': ['python', 'ruby'],
#   'sarah': ['c'],
#   'edward': ['ruby', 'go'],
#   'phil': ['python', 'haskell'],
#}
#for name, languages in favorite_languages.items():
#    print(len(languages))
#    if len(languages) == 1:
#        print(f"\n{name.title()}'s favorite languages is:")
#    else:
#        print(f"\n{name.title()}'s favorite languages are:")
#    for languages in languages:
#        print(f"\t{languages.title()}")

#6.4.3在字典中存储字典
#users = {
#    'aeinstein':{
#        'first': 'albert',
#        'last': 'einstein',
#        'location': 'princeton',
#    },
#    'mcurie':{
#        'first': 'marie',
#        'last': 'curie',
#        'location': 'paris',
#    },
#}
#for username, user_info in users.items():
#    print(f"\nUsername: {username}")
#    full_name = f"{user_info['first']} {user_info['last']}"
#    location = user_info['location']
#    print(f"\tFull name: {full_name.title()}")
#    print(f"\tLocation: {location.title()}")


#练习
#information = {
#    'niuyiqun': {
#    'first_name': 'niu',
#    'last_name': 'yiqun',
#   'age': 18,
#   'city': 'Shenyang'},
#   'liuyujun': {
#   'first_name': 'Liu',
#   'last_name': 'yujun',
#   'age': 30,
#   'city': 'harbin'}
#   }
#for name, info in information.items():
#    print(name,info)


#pets = {
#    'dog':{
#        'owner':'niuyiqun',
#       'age':3,
#       'breed':'siberian husky'
#   },
#    'cat':{
#        'owner':'liuyujun',
#       'age':2,
#        'breed':'persian cat'
#    }
#}
#for pet, info in pets.items():
#    print(f"\n{info['owner'].title()}'s pet is a {pet}.")
#    print(f"{pet.title()}'s age is {info['age']}.")
#    print(f"{pet.title()}'s breed is {info['breed'].title()}.")

#favorite_places = {
#    'niuyiqun': ['shanghai','beijing','guangzhou'],
#   'liuyujun': ['shenyang','harbin','dalian'],
#}
#for name, places in favorite_places.items():
#    print(f"\n{name.title()}'s places are:")
#    for place in places:
#       print(f"\t{place.title()}")


cities = {
    'shenyang':{
        'country': 'china',
        'population': 10000000,
        'fact':'shenyang is the capital of liaoning province.'},
    'paris':{
        'country': 'france',
        'population': 2000000,
        'fact':'paris is the capital of france.'},
    'london':{
        'country': 'england',
        'population': 8000000,
        'fact':'london is the capital of england.'
    }
}
for country,info in cities.items():
    print(f"\n{country.title()}:")
    for info in info.values():
        print(f"\t{info}")



























































































































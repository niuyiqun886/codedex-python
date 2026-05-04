#第八章 函数
#将函数存储为模块的独立文件中。
#8.1 定义函数,使用def开头定义一个函数
#def greet_user():
#    """显示简单的问候语"""
#    print("Hello!")

#greet_user()           #调用函数只需要使用这个函数的定义的名字就可以。

#向函数传递信息
#def greet_user(username):
#    """显示简单的问候语"""
#    print(f"Hello, {username.title()}!")

#greet_user('niuyiuqun')

#8.1.2 实参和形参 如上面的例子，其中 username就是一个形参，而'niuyiqun'就是一个实参
#就是将实参赋值给了形参

#练习8.1 消息
#def display_message():
#    print("The theme in this chapter is the function.")

#display_message()

#练习 8.2 喜欢的书
#def favorite_book(book):
#    print(f"One of my favorite books is {book.title()} in Wonderland.")

#favorite_book('alice')

#8.2 传递实参
#8.2.1 位置实参。可以同时输入两个形参
#def describe_pet(animal_type, pet_name):
#    """显示宠物的信息"""
#   print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}")

#describe_pet('dog', '旺财')

#01 调用函数多次
#describe_pet('hamster', 'harry')

#02 位置实参的顺序很重要
#describe_pet('旺财', 'dog')

#8.2.2 关键字实参，在函数调用的过程中使用关键字，这时就不需要关注顺序了
#describe_pet(animal_type = 'dog', pet_name = '旺财')
#describe_pet(pet_name = '旺财', animal_type = 'dog')

#8.2.3 默认值，给了形参的默认值，调用函数就不同在给指定值了。，当然再次赋值也没问题。
#def describe_pet(pet_name, animal_type = 'dog'):
#    """显示宠物的信息"""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet(pet_name = 'willie')
#describe_pet(pet_name = '富贵', animal_type = 'cat')

# 8.2.4 等效的函数调用
#def describe_pet(pet_name, animal_type = 'dog'):  #这里的pet_name的形参必须提供实参。
#    print(f"\nI have a {animal_type}.")
#   print(f"My {animal_type}'s name is {pet_name}.")
#一只名为willie的小狗
#describe_pet('willie')
#describe_pet(pet_name = 'willie')

#一只名为Harry的仓鼠
#describe_pet('Harry', 'hamster')
#describe_pet(pet_name = 'harry', animal_type = 'hamster')
#describe_pet(animal_type = 'hamster', pet_name = 'harry')

#8.2.5 避免实参错误(没有添加实参，或者定义形参)
#def describe_pet(pet_name, animal_type):
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title}.")

#describe_pet()

#练习8.3 ：T恤
#def make_shirt(size, word):
#    print(f"This shirt'size is {size} with the word : {word}.")
#make_shirt('XL', '18')
#ake_shirt(size = 'XXL', word = '10')

#练习8.4： 大号T恤
#def make_shirt(size = 'large', word = 'I love Python'):
#    print(f"This shirt'size is {size} with the word : {word}.")
#make_shirt()
#ake_shirt(word = 'China')

#练习8.5：城市
#def describe_city(city = 'beijing', country = 'china'):
#    print(f"{city.title()} is in {country.title()}.")
#describe_city()
#describe_city('london', 'england')

#8.3 返回值，可以使用return语句将值返回到调用函数的那行代码
#def get_formatted_name(first_name, last_name):
#    """返回标准格式的姓名"""
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

#8.3.3 让实参变成可选的
#def get_formatted_name(first_name, middle_name, last_name):
#    """返回标准格式的姓名"""
#    full_name = f"{first_name} {middle_name} {last_name}"
#    return full_name.title()

#musician = get_formatted_name('jimi', 'lee', 'hendrix')
#print(musician)

#def get_formatted_name(first_name, last_name, middle_name = ''):
#   """返回标准格式的姓名"""
#   if middle_name:
#        full_name = f"{first_name} {middle_name} {last_name}"
#    else:
#        full_name = f"{first_name} {last_name}"
#    return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

#musician = get_formatted_name('john', 'hooker', 'lee')
#print(musician)

#8.3.3 返回字典
#def build_person(first_name, last_name):
#    """返回一个字典，其中包含有关一个人的信息"""
#    person = {'first': first_name, 'last': last_name}
#    return person
#musician = build_person('jimi', 'hendrix')
#print(musician)

#def build_person(first_name, last_name, age = None):
#    """返回一个字典，其中包含有关一个人的信息"""
#    person = {'first': first_name, 'last': last_name}
#   if age:
#        person['age'] = age #这是字典的定义方式
#    return person
#musician = build_person('jimi', 'hendrix', 27)
#print(musician)

#8.3.4 结合使用函数和while循环
def get_fomatted_name(first_name, last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatte_name  = get_fomatted_name(f_name, l_name)
    print(f"\nHello, {formatte_name}!")
#加入了退出和不退出循环的命令    
    exit = input("Do you want to quit?(yes/no)")
    if exit == 'yes':
        break
    elif exit == 'no':
        continue







































































































































































































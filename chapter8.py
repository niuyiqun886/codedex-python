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
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog', '旺财')

#01 调用函数多次
describe_pet('hamster', 'harry')

#02 位置实参的顺序很重要
describe_pet('旺财', 'dog')

#8.2.2 关键字实参，在函数调用的过程中使用关键字，这时就不需要关注顺序了
describe_pet(animal_type = 'dog', pet_name = '旺财')
describe_pet(pet_name = '旺财', animal_type = 'dog')
# 测试 VSCode 同步到 GitHub











































































































































































































































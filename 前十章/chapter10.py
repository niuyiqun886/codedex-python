#第十章 文件和异常
#10.1读取文件
#101.1读取文件的全部内容，使用python读取txt文档中的内容
#from pathlib import Path
#path = Path('PY_test/pi_digits.txt')  #这里需要看下运行的目录，目录不对无法运行
#contents = path.read_text().rstrip()  #这里的.rstrip()是可以去掉多余行可以删除字符串末尾的空白
##contents = path.read_text()
#print(contents)
#这种方法为：方法链式调用

#10.1.2相对文件路径和绝度文件路径
#相对路径：就是让Python到相对于当前运行的程序所在路目录中去找文件
#绝对路径：就是让python去读取这个文件的完整路径


#使用绝对路径
#from pathlib import Path
#path = Path('D:/代码/PY_test/pi_digits.txt')  #书上说的是使用斜杠‘/’，不能用windows中的反斜杠‘\’
#contents = path.read_text().rstrip()
#print(contents)

#-------------------------------------------------------------------------------
#10.1.3访问文件中的各行
#from pathlib import Path
#path = Path('D:/代码/PY_test/pi_digits.txt')
#contents = path.read_text()
#lines = contents.splitlines()
#for line in lines:
#    print(line)
#print(len(lines))

#-------------------------------------------------------------------------------
#10.1.4 使用文件的内容
#from pathlib import Path
#path = Path('D:/代码/PY_test/pi_digits.txt')
#contents = path.read_text()
#lines = contents.splitlines()

#pi_string = ''
#for line in lines:
#    pi_string += line.lstrip()

#print(pi_string)
#print(len(pi_string))

#-------------------------------------------------------------------------------
#10.1.5包含100万位的大型文件
#from pathlib import Path
#path = Path('D:/代码/PY_test/pi_million_digits.txt')
#contents = path.read_text()

#lines = contents.splitlines()
#pi_string = ''
#for line in lines:
#    pi_string += line.lstrip()

#print(f"{pi_string[:52]}...")
#print(len(pi_string))

#-------------------------------------------------------------------------------
#10.1.6圆周率值包含你的生日吗
#from pathlib import Path
#path = Path('D:/代码/PY_test/pi_million_digits.txt')
#contents = path.read_text()

#lines = contents.splitlines()
#pi_string = ''
#for line in lines:
#    pi_string += line.lstrip()

#print(f"{pi_string[:52]}...")
#print(len(pi_string))

#birthday = input("Enter your birthday, in the form mmddyy: ")

#if birthday in pi_string:
#    print("Your birthday appears in the first million digits of pi.")
#else:
#    print("Your birthday does not appears in the first million digits of pi.")

#-------------------------------------------------------------------------------
#练习10.1Python学习笔记
#from pathlib import Path
#path = Path('D:/代码/PY_test/learning_python.txt')
#contents = path.read_text()
#print(contents)

#learns = []
#learn_lines = contents.splitlines()
#for learn_line in learn_lines: 
#    print(learn_line)
#    learns.append(learn_line)
#print(learns)

#for learn in learns:
#    print(learn)

#-------------------------------------------------------------------------------
#练习10.2C语言学习笔记
#for learn in learns:
#    learn = learn.replace('python', 'C')
#    print(learn)

#-------------------------------------------------------------------------------
#10.2写入文件
##10.2.1 写入一行
#from pathlib import Path
#path = Path('programming.txt')          #定义了一个相对路径下的文件夹
#path.write_text("I love programming.""\nI like dogs")  #这样就可以直接在这个文件中写入内容了

#-------------------------------------------------------------------------------
##10.2.2写入多行
#from pathlib import Path

#contents = "I love programming.\n"
#contents += "I love creating new games.\n"
#contents += "I also love working with data.\n"

#path = Path('programming.txt')
#path.write_text(contents)

##注意这里，在对path对象调用write_text（）方法时，如果指定的文件已经存在，那么write_text（）
##将删除其内容，并将指定的内容写入其中。

#-------------------------------------------------------------------------------
##练习10.4 访客
#from pathlib import Path
#name = input("Please input you name:")
#path = Path('name.txt')
#path.write_text(name)

#-------------------------------------------------------------------------------
##练习10.5 访客薄
#from pathlib import Path
#contents = ''
#while True:
#    name = input("Please input you name:")
#    if name == 'q':
#        break
#    else:
#        contents += name + '\n'
#path = Path('guest_book.txt')
#path.write_text(contents)

#-------------------------------------------------------------------------------
##10.3异常
#10.3.1处理ZeroDivisionError异常
#print(5/0)
#10.3.2使用try-except代码块,这个错误影响了代码的正常运行，是用try-except可以略过这个异常的模块
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")


#------------------------------------------------------------------------------------
#10.3.3使用异常避免崩溃(如果分母出现0了，那么就会直接报错的）
#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")

#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Sceond number: ")
#    if second_number == 'q':
#        break
#    answer = int(first_number) / int(second_number)
#    print(answer)


#------------------------------------------------------------------------------------
#10.3.4  else代码块(在中间插入了try-except模块可以直接解决因ZeroDivisionError导致的程序停止)
#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Sceond number: ")
#    if second_number == 'q':
#        break
#    try:
#        answer = int(first_number) / int(second_number)
#    except ZeroDivisionError:
#        print("You can't divide by 0.")
#    else:
#        print(answer)


#-----------------------------------------------------------------------------------
#10.3.5 处理FileNoteFoundError（这个是找不到文件了）
#问题
#from pathlib import Path

#path = Path('alice.txt')
#contents = path.read_text(encoding = 'utf-8')

#解决这个问题
#from pathlib import Path

#path = Path('alice.txt')
#try:
#    contents = path.read_text(encoding = 'utf-8')
#except FileNotFoundError:
#    print(f"Sorry, the file {path} does not exit.")


#-----------------------------------------------------------------------------------
#10.3.6分析文本
#from pathlib import Path

#path = Path('alice.txt')
#try:
#    contents = path.read_text(encoding = 'utf-8')
#except FileNotFoundError:
#    print(f"Sorry, the file {path} does not exit.")
#else:
    #计算文件大致包含多少个单词
#    words = contents.split()
#    num_words = len(words)
#   print(f"The file {path} has about {num_words} words.")


#-----------------------------------------------------------------------------------
#10.3.7使用多个文件,将计算的过程定义为一个函数
#from pathlib import Path

#def count_words(path):
#    try:
#        contents = path.read_text(encoding = 'utf-8')
#    except FileNotFoundError:
#        print(f"Sorry, the file {path} does not exit.")
#    else:
#    #计算文件大致包含多少个单词
#        words = contents.split()
#        num_words = len(words)
#        print(f"The file {path} has about {num_words} words.")

#path = Path('alice.txt')
#count_words(path)



#from pathlib import Path

#def count_words(filenames):
#    try:
#        contents = path.read_text(encoding = 'utf-8')
#    except FileNotFoundError:
#        print(f"Sorry, the file {path} does not exit.")
#    else:
#    #计算文件大致包含多少个单词
#        words = contents.split()
#        num_words = len(words)
#        print(f"The file {path} has about {num_words} words.")


#filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
#for filename in filenames:
#    path = Path(filename)
#    count_words(path)


#-------------------------------------------------------------------------------
#10.3.8静默失败,使用pass跳过失败
#from pathlib import Path
#def count_words(filenames):
#    try:
#        contents = path.read_text(encoding = 'utf-8')
#    except FileNotFoundError:
#        pass
#   else:
#    #计算文件大致包含多少个单词
#        words = contents.split()
#        num_words = len(words)
#        print(f"The file {path} has about {num_words} words.")


#filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
#for filename in filenames:
#    path = Path(filename)
#    count_words(path)

#-------------------------------------------------------------------------------
#练习10.6 加法运算
#print("Give me two numbers, and I'll add them.")

#first_number = input("\nFirst number: ")
#second_number = input("Sceond number: ")      
#try:
#    answer = int(first_number) + int(second_number)
#except ValueError:
#    print("You can't input word.")
#else:
#    print(answer)

#-------------------------------------------------------------------------------
#练习10.7 加法计算器
#print("Give me two numbers, and I'll add them.")
#print("Enter 'q' to quit.")
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Sceond number: ")      
#    if second_number == 'q':
#        break
#    try:
#        answer = int(first_number) + int(second_number)
#    except ValueError:
#       print("You can't input word.")
#    else:
#        print(answer)

#-------------------------------------------------------------------------------
#10.8猫和狗
#from pathlib import Path

#files = ['cats.txt','dogs.txt','pigs.txt'] 
#for file in files:
#    path = Path(file)
#    try:
#        contents = path.read_text()
#    except FileNotFoundError:
#        print(f"The {file} does not exit.")
#    else:
#        print(contents)

#-------------------------------------------------------------------------------
#10.8猫和狗
#from pathlib import Path

#files = ['cats.txt','dogs.txt','pigs.txt'] 
#for file in files:
#    path = Path(file)
#    try:
#        contents = path.read_text()
#    except FileNotFoundError:
#        pass
#    else:
#        print(contents)

#-------------------------------------------------------------------------------
#练习10.10 常见单词,查找文件中的单词的数量
#from pathlib import Path

#path = Path('little_women.txt')
#contents = path.read_text()
#word = input("Please input your word: ")
#number = contents.lower().count(word)
#print(number)


#-------------------------------------------------------------------------------
#10.4 存储数据，使用json可以存储字典、列表这些复杂的结构
#10.4.1使用json.dump()和json.loads()

####存数据
#from pathlib import Path
#import json
#numbers = [2, 3, 5, 7, 11, 13]

#path = Path('numbers.json')
#contents = json.dumps(numbers)    ##使用json.dumps()存储
#path.write_text(contents)         ##使用json.dunps()后还是要使用write_text()来写入

####取数据，取出来就是原来的结构
#from pathlib import Path
#import json

#path = Path('numbers.json')
#contents = path.read_text()         ##使用json.load()之前还是要使用read_text()来读文档
#numbers = json.loads(contents)      ##使用json.loads()来读取

#print(numbers)

#-------------------------------------------------------------------------------
#10.4.2 保存和读取用户生成的数据
####保存生成的数据
#from pathlib import Path
#import json

#username = input("What is your name? ")

#path = Path('username.json')
#contents = json.dumps(username)
#path.write_text(contents)

#print(f"We'll remember you when you come back, {username}!")


####读取用户的数据
#from pathlib import Path
#import json

#path = Path('username.json')
#contents = path.read_text()
#username = json.loads(contents)

#print(f"Wellcome back, {username}!")

###将上面的合并到一个程序中
#from pathlib import Path
#import json

#path = Path('username.json')
#if path.exists():
#    contents = path.read_text()
#    username = json.loads(contents)
#    print(f"Welcome back,{username}!")
#else:
#    username = input("What is your name? ")
#    contents = json.dumps(username)
#    path.write_text(contents)
#    print(f"I will remember you when you come back,{username}")


#-------------------------------------------------------------------------------
#10.4.3 重构，即划分为一系列完成具体工作的函数进行改进
#from remember_me import *

#path = Path('username.json')
#username1 = get_stored_username(path)
#print(username1)

#greet_user()


#-------------------------------------------------------------------------------
#练习10.11：喜欢的数
#from pathlib import Path
#import json

#path = Path('word.json')
#word = input("Plase input you favorite word: ")
#contents = json.dumps(word)
#path.write_text(contents)

#from pathlib import Path
#import json

#path = Path('word.json')
#contents = path.read_text()
#word = json.loads(contents)
#print(f"I know your favorite number! It's {word}.")


#-------------------------------------------------------------------------------
#练习10.12记住喜欢的数
#from pathlib import Path
#import json
#path = Path('word.json')

#if path.exists():
#    contents = path.read_text()
#    word = json.loads(contents)
#    print(word)
#else:
#    word = input("Please input your favorite word: ")
#    contents = json.dumps(word)
#    path.write_text(contents)


#-------------------------------------------------------------------------------
#练习10.13用户字典，将用户的信息写入字典中
#from pathlib import Path
#mport json
#path = Path('information.json')
#infor = {}

#if path.exists():
#    contents = path.read_text()
#    information = json.loads(contents)
#    print(f"I know your name is {information['name']} and you are {information['age']} years old.")
#    print(information)
#else:
#    username = input("Please add your username:")
#    infor['username'] = username
#    age = input("Please input your age: ")
#    infor['age'] = age
#    name = input("Please input your name: ")
#    infor['name'] = name
#    contents = json.dumps(infor)
#    path.write_text(contents)


#-------------------------------------------------------------------------------
#练习10.14 验证用户
from remember_me import *
import json

greet_user()
































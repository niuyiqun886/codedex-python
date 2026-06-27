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

#10.1.3访问文件中的各行
#from pathlib import Path
#path = Path('D:/代码/PY_test/pi_digits.txt')
#contents = path.read_text()
#lines = contents.splitlines()
#for line in lines:
#    print(line)
#print(len(lines))

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

#irthday = input("Enter your birthday, in the form mmddyy: ")

#if birthday in pi_string:
#    print("Your birthday appears in the first million digits of pi.")
#else:
#    print("Your birthday does not appears in the first million digits of pi.")

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

#练习10.2C语言学习笔记
#for learn in learns:
#    learn = learn.replace('python', 'C')
#    print(learn)


#10.2写入文件
##10.2.1 写入一行
#from pathlib import Path
#path = Path('programming.txt')          #定义了一个相对路径下的文件夹
#path.write_text("I love programming.""\nI like dogs")  #这样就可以直接在这个文件中写入内容了

##10.2.2写入多行
#from pathlib import Path

#contents = "I love programming.\n"
#contents += "I love creating new games.\n"
#contents += "I also love working with data.\n"

#path = Path('programming.txt')
#path.write_text(contents)

##注意这里，在对path对象调用write_text（）方法时，如果指定的文件已经存在，那么write_text（）
##将删除其内容，并将指定的内容写入其中。


##练习10.4 访客
#from pathlib import Path
#name = input("Please input you name:")
#path = Path('name.txt')
#path.write_text(name)

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
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding = 'utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exit.")
else:
    #计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")


#-----------------------------------------------------------------------------------
#使用多个文件






















































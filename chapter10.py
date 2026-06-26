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
from pathlib import Path
path = Path('D:/代码/PY_test/learning_python.txt')
contents = path.read_text()
#print(contents)

learns = []
learn_lines = contents.splitlines()
for learn_line in learn_lines: 
    print(learn_line)
    learns.append(learn_line)
print(learns)

#for learn in learns:
#    print(learn)

#练习10.2C语言学习笔记
for learn in learns:
    learn = learn.replace('python', 'C')
    print(learn)














#第十章 文件和异常
#10.1读取文件
#101.1读取文件的全部内容
from pathlib import Path
path = Path('PY_test/pi_digits.txt')  #这里需要看下运行的目录
contents = path.read_text()
print(contents)
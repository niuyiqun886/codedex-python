#from pathlib import Path
#import json

#def greet_user():
#    path = Path('username.json')
#    if path.exists():
#        contents = path.read_text()
#        username = json.loads(contents)
#        print(f"Welcome back,{username}!")
#    else:
#        username = input("What is your name? ")
#        contents = json.dumps(username)
#        path.write_text(contents)
#        print(f"I will remember you when you come back,{username}")


#from pathlib import Path
#import json

#def get_stored_username(path):
#    """如果存储了用户名，就获取它"""
#    if path.exists():
#        contents = path.read_text()
#        username = json.loads(contents)
#        return username
#    else:
#        return None


#def greet_user():
#    path = Path('username.json')
#    if path.exists():
#        contents = path.read_text()
#        username = json.loads(contents)
#        print(f"Welcome back,{username}!")
#    else:
#        username = input("What is your name? ")
#        contents = json.dumps(username)
#        path.write_text(contents)
#        print(f"I will remember you when you come back,{username}")

##最终版-------------------------------------------------------------------------
#from pathlib import Path
#import json

#def get_stored_username(path):
#    """如果存储了用户名，就获取它"""
#    if path.exists():
#        contents = path.read_text()
#        username = json.loads(contents)
#        return username
#    else:
#        return None

#def get_new_username(path):
#    username = input("What is your name? ")
#    contents = json.dumps(username)
#    path.write_text(contents)
#    return username

#def greet_user():
#    path = Path('username.json')
#    username = get_stored_username(path)
#   if username:
#        print(f"Welcome back,{username}!")
#   else:
#        username = get_new_username(path)
#        print(f"I will remember you when you come back,{username}")


##练习题版-------------------------------------------------------------------------
from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        confirm = input(f"Is this your name : {username}\n")
        if confirm == 'yes':
            print(f"Welcome back {username}")
        else:
            username = get_new_username(path)
            print(f"I will remember you when you come back,{username}")
    else:
        username = get_new_username(path)
        print(f"I will remember you when you come back,{username}")

#用户输入和while循环
#7.1 input()函数的工作原理
#message = input("Tell me something, and I will repeat it back to you: ")#:后面加了一个空格
#print(message)

#7.1.1编写清晰的提示
#name = input("Please enter your name: ") #name后面加了一个空格
#print(f"\nHello, {name}!")


#prompt = "If you share your name, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "# += 表示把右边内容追加到 prompt 里

#name = input(prompt)
#print(f"\nHello, {name}!")

#7.1.2使用int()来获取数值输入
#age = input("How old are you? ")
#age = int(age)    #把输入的字符串转换为整数
#print(age>=18)

#height = input("How tall are you, in inches? ")
#height = int(height)

#if height >= 48:
#    print("\nYou are tall enough to ride!")
#lse:
#    print("\nYou'll be able to ride when you're a little older.")

#7.1.3 求模运算符,它是一个百分号（%），它返回除法的余数,不会指出一个数是另一个的多少倍，
#只指出余数是多少。
#print(4 % 3)
#print(5 % 3)
#print(6 % 3)
#print(7 % 3)

#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#if number % 2 == 0:
#    print(f"\nThe number {number} is even.")
#else:
#    print(f"\nThe number {number} is odd.")

#练习7.1汽车租赁
#cars = input("What kind of car do you want to rent? ")
#print(f"Let me see if I can find you a {cars}")

#练习7.2餐馆订位
#people = input("How many people are in your dinner group? ")
#people = int(people)
#f people > 8:
#   print("You'll have to wait for a table.")
#lse:
#   print("Your table is ready.")

#练习7.3 10的整数倍
#number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
#number = int(number)
#f number % 10 == 0:
#    print(f"\nThe number {number} is a multiple of 10.")
#else:
#    print(f"\nThe number {number} is not a multiple of 10.")

#7.2 while循环,for循环用于遍历列表或其他集合的元素，而while循环则不断地执行一段代码，直到指定的条件不再满足为止。
#7.2.1 使用while循环
#Current_number = 1
#while Current_number <=5:
#   print(Current_number)
#   Current_number += 1

#7.2.2 让用户选择何时退出，即message = quit 时退出循环。
#prompt = "\n Tell me something, and I will repeat it back to you: "
#prompt += "\n Enter 'quit' to end the program. "

#message = ""
#hile message != 'quit':
#    message = input(prompt)
#   print(message)

#prompt = "\n Tell me something, and I will repeat it back to you: "
#prompt += "\n Enter 'quit' to end the program. "

#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

#7.2.3 使用标志,有时候需要一个变量来告诉程序何时停止运行，这个变量被称为标志（flag）。
# 在这个例子中，我们使用一个名为active的布尔变量来控制循环的运行。
#prompt = "\n Tell me something, and I will repeat it back to you: "
#prompt += "\n Enter 'quit' to end the program. "

#active = True
#while active:
#   message = input(prompt)

#    if message == 'quit':
#        active = False
#    else:
#        print(message)

#7.2.4 使用break退出循环
#prompt = "\nPlease enter the name of a city you have visited:: "
#prompt += "\n Enter 'quit' when you are finished."

#while True:
#    city = input(prompt)

#    if city == 'quit':
#        break
#    else:
#        print(f"\nI'd love to go to {city.title()}")

#7.2.5 在循环中使用continue
#current_number = 0
#while current_number < 10:
#    current_number += 1
#   if current_number % 2 == 0:
#       continue
#   print(current_number)

#7.2.6 避免无限循环，需要在写好后对while循环测试，看是否符合预期那样结束。
#x = 1
#while x <= 5:
#   print(x)
#   x += 1       #没有这一行将进入无限循环

#练习7.4：比萨配料
#pizza_fruit = "Please enter something to the topping of the pizza."
#pizza_fruit += "\nAdding your favorite fruite:"

#while True:
#    fruit = input(pizza_fruit)
#   if fruit == 'quit':
#       break
#   else:
#       print(f"\tI'd love to add the {fruit} on the topping.")

#练习7.5 电影票
#people_age = "Please tell me: How old are you?"

#while True:
#    age = input(people_age)
#    if age == 'quit':
#       break
#    age = int(age)
#    print(age)
#    if age < 3:
#        print(f"You can be free.")
#    elif 3 <=age < 12:
#        print("You need to pay $10.")
#    else:
#        print("You need $15.") 
    
        
#练习 7.7 无限循环
#number = 1
#while number <= 20:
#    print(number)

#7.3使用while循环处理列表和字典

#7.3.1 在列表之间移动元素
#首先，创建一个待验证用户列表
#和一个用于存储已验证用户的空列表
#unconfirmed_users = ['alice', 'brain', 'candace']
#confirmed_users = []
#print(unconfirmed_users)
#验证每个用户，直到没有为验证用户为止
#将每个经过验证的用户都移到已验证用户列表中
#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()

#    print(f"Verifying user:{current_user.title()}")
#    confirmed_users.append(current_user)
#print(confirmed_users)
#显示所有已经验证的用户
#print(f"\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#    print(confirmed_user.title())
#print(confirmed_users)


#7.3.2 删除为特定值的所有列表元素，使用remove()
#pets = ['dog', 'cat','dog', 'goldfish', 'cat', 'rabbbit', 'cat']
#print(pets)
#while 'cat' in pets:
#    pets.remove('cat')
#print(pets)

#7.3.3 使用用户输入填充字典
#responses = {}
#polling_active = True
#while polling_active:
    #提示输入被调查者的名字和回答
#    name = input("\nWhat is your name? ")
#    response = input("Which mountain would you like to climb someday?")

    #将回答存储到字典中,字典的存储格式就是 responses[name] = response
#    responses[name] = response

    #看看是否还有人参与调查
#    repeat = input("Would you like to let another person respond?(yes/no)")
#    if repeat == 'no':
#        polling_active = False

#调查结束，显示结果
#print("\n--- Poll Results ---")
#for name, response in responses.items():
#    print(f"{name} would you like to climb {response}.")

#print(responses)

#练习7.8 熟食店
#sandwich_orders = ['apple', 'banana', 'grape']
#finish_sandwiches = []
#while sandwich_orders:
#    sandwich = sandwich_orders.pop()
#    print(f"I made your {sandwich.title()} sandwich.")
#    print(len(sandwich_orders))
#    if len(sandwich_orders) == 0:
#        print(f"\n\tAll sandwiches have finished.")
#    finish_sandwiches.append(sandwich)

#print(f"\n{finish_sandwiches}")

#练习7.9 五香牛肉卖完了
#sandwich_orders = ['apple', 'pastrami', 'banana', 'grape', 'pastrami']
#finish_sandwiches = []
#print(f"The pastrami sandwich have been sold out.")
#while 'pastrami' in sandwich_orders:
#    sandwich_orders.remove('pastrami')
#print(sandwich_orders)
#while sandwich_orders:
#    sandwich = sandwich_orders.pop()
#    print(f"I made your {sandwich.title()} sandwich.")
#    if len(sandwich_orders) == 0:
#        print(f"\n\tAll sandwiches have finished.")
#    finish_sandwiches.append(sandwich)

#rint(f"\n{finish_sandwiches}")

#练习7.10 梦想中的度假胜地
place_visit = []
while True:
    place = input("If you could visit one place in the world, where would you go?")

    place_visit.append(place)

    repeat = input("These are the places I want to visit.(yes/no)")
    if repeat == 'yes':
        break
    else:
        continue
print(place_visit)














































































































































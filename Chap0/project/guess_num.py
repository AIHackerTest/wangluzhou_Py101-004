# encoding: utf-8
import random
from sys import exit


print("欢迎来到猜数字游戏!")
target = random.randint(0, 20)
max_guess_count = 10
print("你将有 %d 次机会." % max_guess_count)
for i in range(max_guess_count):
    while True: # while不会限制局部变量访问
        try:  # try中定义的变量并不局限在try模块内，但是一旦except以后,guess并没有被赋值，所以后面会报错
            guess = int(input("请输入数字: ")) # 对于字符型的"4.1"同样会转换失败
            break
        except ValueError:
            print("请确保你输入的是数字!")
            continue
    if guess == target:
        print("恭喜你答对了，正确答案就是 %d !" % target)
        exit()
    elif guess > target:
            print("比正确答案大了")
    else:
        print("比正确答案小了")
    print("你还有 %d 次机会可以输入" % (max_guess_count - i - 1))
print("你已经花掉所有有的 %d 次机会了, 游戏结束，gg!" % max_guess_count)

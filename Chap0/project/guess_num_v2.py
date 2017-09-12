# encoding: utf-8
import random
import math

def dd(x, y):
    return x - y

def count_rep(list_):
    return len(list_) - len(set(list_))

# 生成4个互不相等的四位数
samples = list(range(0,10))
first = random.randint(1,9)
samples.remove(first)
digit_list = [first] + random.sample(samples, 3)
# print(digit_list)
# 将list转换成四位整数
target = "".join(str(x) for x in digit_list)
max_guess_count = 10
print("欢迎来到猜数字游戏!")
print("你将有 %d 次机会." % max_guess_count)
for i in range(max_guess_count):
    ## 输入四位整数
    while True: # while不会限制局部变量访问
        try:
            guess_str = input("请输入数字: ")
            guess = int(guess_str)
            log_val = math.log10(guess)
            if 4 <= log_val or log_val <= 2:
                # 判断这个数字是否在101到9999范围
                raise ValueError
            guess_digit_list = [int(x) for x in guess_str]
            if len(guess_digit_list) != 4:
                raise ValueError
            break
        except ValueError:
            print("请确保你输入的是四个数字！")
            continue

    ## 判断数字正确且位置正确的个数
    a_count = list(map(dd, guess_digit_list, digit_list)).count(0)
    ## 判断数字正确但位置错误的个数
    tmp = guess_digit_list + digit_list
    ## 要注意输入的四位数本身就是可能含有重复项，需要排除
    b_count = count_rep(tmp) - a_count - count_rep(guess_digit_list)
    if a_count == 4:
        print("恭喜你答对了，正确答案就是 %s !" % target)
        exit()
    else:
        print ("您本次猜测的结果是 %d A %d B" % (a_count, b_count))
        print("你还有 %d 次机会可以输入" % (max_guess_count - i - 1))

print("你已经花掉所有有的 %d 次机会了, 游戏结束，gg!" % max_guess_count)

# coding: utf-8
# In[3]:
import random
def random_num():  #生成随机的四位各不相同的 list 函数
    a=[1,2,3,4,5,6,7,8,9]
    b=[0,1,2,3,4,5,6,7,8,9]

    a1=random.sample(a,1)    #产生千位数字
    b.remove(a1[0])     #保证后个位，十位，百位的数字和千位数字不同
    b1=random.sample(b,3)  #随机取三个元素最为一个片段返回，比如 [6,4,3]
    a1.extend(b1) #将千位和个十百位的元素，拼合为一个新list
    #print (a1)    #[9, 7, 1, 4]
    return (a1)

def num_to_list(num):  # 将“输入的数字“转为 list的函数

    num2 = str(num)
    c = []
    # print ("num_to_list num2: %r" % num2)

    for digit in num2:
        c.append (int(digit))
    # print ("num_to_list c: %r" % c)
    return c

def dd(x, y):
    return x-y

a = random_num()
random_number = a  #调用 随机函数的list

print ("You have 10 times to guess the given random number, good luck")

for i in range(10):

    guess_num = int(input("please input 4-digit number ->"))    #输入4位数字
    # print("guess_num %r" % guess_num)
    guess_list = num_to_list(guess_num) # 将“输入的guess数字“转为 list
    # print("guess=%r" %(guess_list))


    random_list = random_num()   # 产生 一个包含四位随机数字的list
    # print ("random_list: %r" % random_list)

    c = list(map(dd, guess_list, random_list))
    # print ("c = %r" % c)

    a_count = len(c)

    guess_list.extend(random_list)

    b_count = len(guess_list)-len(set(guess_list))-a_count

    print ("%dA%dB" %(a_count,b_count))

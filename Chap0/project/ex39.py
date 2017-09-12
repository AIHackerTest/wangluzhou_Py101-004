# encoding: utf-8
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Firsbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # 提取并移除的操作感觉未来很有用
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))


print ("There we go:", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1]) # whoa!fancy 取最后一位
print (stuff.pop()) # 默认移除最后一位，然后返回移除的那一个元素
print (' '.join(stuff)) # what? cool!
print ('#'.join(stuff[3:5])) # super stellar!

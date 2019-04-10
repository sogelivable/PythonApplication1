# 注释
import this
msg="hello world "
print(msg)
print(msg.title())
print(msg.lstrip())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)print(bicycles[0])print(bicycles[0].title())bicycles.append('ducati')bicycles.sort()#使用函数sorted() 对列表进行临时排序 返回新的别表sorted(bicycles)bicycles.reverse()len(bicycles)#别忘了，每当需要访问最后一个列表元素时，都可使用索引-1 。这在任何情况下都行之有效，即便你最后一次访问列表后，其长度发生了变化：bicycles[-1]motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]#你要将元素从列表中删除，并接着使用它的值。popped_motorcycle = motorcycles.pop(0)print(motorcycles)print(popped_motorcycle)#根据值删除元素motorcycles.remove('suzuki')magicians = ['alice', 'david', 'carolina'] for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show! "+magician)for value in range(1,5):
    print(value)    

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)for v in range(1,21):    if(v%2!=0):        print(v)players = ['charles', 'martina', 'michael', 'florence', 'eli'] print(players[0:3])#如果你要输出名单上的最后三名队员print(players[-3:])'yong' in playersplayers=[]if players:    print('test')        else:    print('empty')age = 12
if age < 4:
    print("Your admission cost is $0.") 
elif age < 18:
    print("Your admission cost is $5.") 
else:
    print("Your admission cost is $10.")#字典 类似jsonalien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['speed']=3
print(alien_0)
del alien_0['points']for key,value in alien_0.items:    print(key+''+value)        for key,value in sorted(alien_0.keys):    print(key+''+value)     for key,value in sorted(alien_0.values):    print(key+''+value)   agestring = '21'ageInt = int(agestring)current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1import TestClassuser_profile = TestClass.TestClass.build_profile('albert', 'einstein',location='princeton',field='physics')TestClass.TestClass.make_pizza('pepperoni')
TestClass.TestClass.make_pizza('mushrooms', 'green peppers', 'extra cheese')

#from TestClass import TestClass as t

import Dog as D

my_dog=  D.Dog('willie', 6)print("My dog's name is " + my_dog.name.title() + ".") print("My dog is " + str(my_dog.age) + " years old.")import collectionsorderedDic = collections.OrderedDict();try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
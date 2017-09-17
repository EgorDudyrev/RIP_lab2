from lab_classes import *
from matplotlib import pylab

#user_id = VK_User('56337756').execute()
name = input('Type username or id: ')
print()
user_id = None
try:
    user_id = VK_User(name).execute()
except Exception as e:
    print(e)
    quit(1)

ages= None
try:
    ages = VK_Friends(user_id).execute()
except Exception as e:
    print(e)
    quit(1)

hist = [(x,ages.count(x)) for x in set(ages)]
hist.sort(key=lambda x: x[0])
for age, number in hist:
    print(age,'#'*number)

pylab.hist(ages,bins=((max(ages)-min(ages))))
pylab.xlabel('age')
pylab.xticks(range(0,max(ages),5),rotation=45)
pylab.title('Distrubution of {}\'s friends ages'.format(name))
pylab.show()

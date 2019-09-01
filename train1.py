import os

param1 = ['test1', 'test2']


def testfunc(param1, param2=0):
    if len(param1) > 1 and param1[0]!='test' :
        for i in param1:
            param2 += len(i)
    else:
        param2=-1
    return param2


testans = testfunc(param1)

print(testans)

nums = [2,435,5,67,3,1,9]

print(nums[1:3])
print(nums[-1])
print(nums[:4])
print(nums[-4:])


#files
items = ['cat', 'mat']
with open('file.txt', 'w') as fout:
    for e in items:
        fout.write(e + '\n')

#tuples

m = (2,453.88,223,5,'str')
temp = m[0]
quality = m[3]
t,la,lo,q,f = m
print(t)
print(m[1])


                              #clasees

class Creature:
    def __init__(self, name,level):
        self.name = name
        self.level = level

    def walk(self):
        print('{} walks around with level {}'.format(self.name, self.level))

    def attack(self, creature):
        if self.level - creature.level >0:
            print('you defeated {}!'.format(creature.name))
        else:
            print('you died')


#classes vs obj

squirrel =  Creature('Suzy',7)

#classes are blueprints for creating objects
#objects are instance of class

                         #----Inheritance

class Dragon(Creature):
    def __init__(self,name, level, scale):
        super().__init__(name, level)
        self.scale = scale

    def breath_fire(self):
        print('ARR'*self.scale)

class Wizard(Creature):
    def __init__(self,name, level, typeOf):
        super().__init__(name, level)
        self.typeOf = typeOf

    def magic(self):
        if self.typeOf == 'evil':
            print('MWAHAAH')
        else:
            print('I Greet you')


Drogon = Dragon('Drogon', 100, 5)
Drogon.breath_fire()
Gandalf = Wizard('Gandalf', 100, 'good')
Gandalf.magic()
                        #POLYMORPHISM

creatures = [Dragon('Drogon1', 105, 5), Creature('worm',1), Wizard('Voldemort',1000, 'evil')]

wizard = Wizard('Dumbledore', 10000, 'good')

for c in creatures:
    wizard.attack(c)

#Dictionaries

info = dict()
info['age'] - 42

#OR

info = dict(age =42, loc ='Italy')
info = {'age': 42, 'loc' : 'Italy'}

if 'age' in info:
    info['age'] +=1
    print(info['age'])

                      #Error handling

#try-except

try:
    method1()
    method2()

except ConnectionError as ce:
#^Specific

except Exception as x:

#^general

                   #Lambdas
#functions are firs-class instances and objects

def find_nums(nums, predicate):
    for n in nums:
        if predicate(n):
            yield n
numbers = [1,1,2,3,5,8,13]
sig = find_nums(numbers, lambda x:x % 2 ==1 )

print(list(sig))

#List comprehentson

paying_usernames = [
 #projection (result) ->   u.name
 #source ->                for u in get_active()
 #filter ->                if u.last_puchase() == today
]

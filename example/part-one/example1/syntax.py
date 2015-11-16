#!/usr/bin/python
# -*- coding: UTF-8 -*-


print '-------------------------------'

for item in [1, 2, 3, 4, 5]:
    print item,
print

count = 0
while count < 5:
    print count, " is less than 5"
    count = count + 1
else:
    print count, "is not less than 5"

for letter in 'abcdef':
    print '当前字母 :', letter

for fruit in ['apple', 'orange', 'mango']:
    print '当前字母 :', fruit

print 'GoodBye!'

array = ["a", "s", "d", "e"]
for index in range(len(array)):
    print '当前水果 :', array[index]
print

if count != 0:
    pass
    print 'this is pass region!'

print eval('1==1')

print "My name is %s, age: %d" % ('nolan', 22)

hi = '''hi
there'''

print hi



x, y = 1, 2
print 'before: ', (x, y)
x, y = y, x
print 'after: ', (x, y)

# this is new common. 

dict = {'name': 'Zara', 1: 'platform', 2: 'webchat', 3: 'ios'}
print dict

print dict['name']
print dict[1]
del dict['name']

print dict
print dict['name']

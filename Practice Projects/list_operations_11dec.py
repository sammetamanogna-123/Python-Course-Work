Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Declaring the lists
l=[]
l=list()
l=[1,2,3,4]
l=[[1,2,3,4],[1,2,3]]
#combining the lists
l=[1,2,3]
m=[1,2,3]
l+m
[1, 2, 3, 1, 2, 3]
l*4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l*7
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
3 in l
True
4 not in l
True
names=['Manu','Usha','Akhila','Rohan','Tanmai','Tarani','Harini']
names
['Manu', 'Usha', 'Akhila', 'Rohan', 'Tanmai', 'Tarani', 'Harini']
names[5]
'Tarani'
names[-2]
'Tarani'
names[0]
'Manu'
names[1]
'Usha'
names[4]
'Tanmai'
names[2]
'Akhila'
names[-4]
'Rohan'
#Slicing
names[:3]
['Manu', 'Usha', 'Akhila']
names[-1:-4:-1]
['Harini', 'Tarani', 'Tanmai']
names[1::2]
['Usha', 'Rohan', 'Tarani']
names[-2::-2]
['Tarani', 'Rohan', 'Usha']
names[::-1]
['Harini', 'Tarani', 'Tanmai', 'Rohan', 'Akhila', 'Usha', 'Manu']
names
['Manu', 'Usha', 'Akhila', 'Rohan', 'Tanmai', 'Tarani', 'Harini']
names[4]
'Tanmai'
names[4] ='Kuttuu'
names
['Manu', 'Usha', 'Akhila', 'Rohan', 'Kuttuu', 'Tarani', 'Harini']
names[-2]='Gayatri'
names
['Manu', 'Usha', 'Akhila', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini']
names[2]='Usha Sri'
names
['Manu', 'Usha', 'Usha Sri', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini']
names[1]='Akhila'
names
['Manu', 'Akhila', 'Usha Sri', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini']
id(names)
2941375789120
names[1] = 'Akhii'
names
['Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini']
id(names)
2941375789120
names
['Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini']
#Adding the elements into the list
names.append("Tejuu")
names
['Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini', 'Tejuu']
names.append("Siddu")
names
['Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini', 'Tejuu', 'Siddu']
names.append("Thanmai")
#append is used for adding the elment in the end of list
#insert is used for adding the element at the particular position
names.insert(0,"Ammu")
names
['Ammu', 'Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Kuttuu', 'Gayatri', 'Harini', 'Tejuu', 'Siddu', 'Thanmai']
names.inset(5,"Babluu")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    names.inset(5,"Babluu")
AttributeError: 'list' object has no attribute 'inset'. Did you mean: 'insert'?
names.insert(5,"Bablu")
names
['Ammu', 'Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Harini', 'Tejuu', 'Siddu', 'Thanmai']
names.extend(['Pranav','Priya','Nithya'])
names
['Ammu', 'Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Harini', 'Tejuu', 'Siddu', 'Thanmai', 'Pranav', 'Priya', 'Nithya']
#Extend is used for adding the group of elements in the end of the list
id(names)
2941375789120
#Deleting the elements
names.remove('Priya')
names
['Ammu', 'Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Harini', 'Tejuu', 'Siddu', 'Thanmai', 'Pranav', 'Nithya']
names.remove('Harini')
names
['Ammu', 'Manu', 'Akhii', 'Usha Sri', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Tejuu', 'Siddu', 'Thanmai', 'Pranav', 'Nithya']
names.pop(3)
'Usha Sri'
names
['Ammu', 'Manu', 'Akhii', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Tejuu', 'Siddu', 'Thanmai', 'Pranav', 'Nithya']
names.pop(7)
'Tejuu'
names
['Ammu', 'Manu', 'Akhii', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Siddu', 'Thanmai', 'Pranav', 'Nithya']
#pop is used to remove the element by using index
#remove is used to remove the element by using names
#if we wont give any index value it will remove last element of the list
names.pop()
'Nithya'
names
['Ammu', 'Manu', 'Akhii', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Siddu', 'Thanmai', 'Pranav']
del names[2]
names
['Ammu', 'Manu', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Siddu', 'Thanmai', 'Pranav']
#del is also used to delete the element
del names[-2]
names
['Ammu', 'Manu', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Siddu', 'Pranav']
names.clear()
names
[]
id(names)
2941375789120
#clear is used to delete all the elements but we have a reference
#del is used to remove but it delete with the reference
#pop is used to remove but it wont delete the rederence

names=['Ammu', 'Manu', 'Akhii', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Siddu', 'Thanmai', 'Pranav']
names
['Ammu', 'Manu', 'Akhii', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Siddu', 'Thanmai', 'Pranav']
names.index('Manu')
1
#index is used for the finding the element at which position
names.index('kuttuu')
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    names.index('kuttuu')
ValueError: 'kuttuu' is not in list
names.index('Pranav')
9
names.count('Pranav')
1
#count is used for the frequency of an element or how many times the element is repeating

sorted(names)
['Akhii', 'Ammu', 'Bablu', 'Gayatri', 'Kuttuu', 'Manu', 'Pranav', 'Rohan', 'Siddu', 'Thanmai']
names
['Ammu', 'Manu', 'Akhii', 'Rohan', 'Bablu', 'Kuttuu', 'Gayatri', 'Siddu', 'Thanmai', 'Pranav']
names.sort()
names
['Akhii', 'Ammu', 'Bablu', 'Gayatri', 'Kuttuu', 'Manu', 'Pranav', 'Rohan', 'Siddu', 'Thanmai']
#Sorted will not effect the original list
#Sort will effect the original list

names.reverse()
names
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Gayatri', 'Bablu', 'Ammu', 'Akhii']
m=names
names
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Gayatri', 'Bablu', 'Ammu', 'Akhii']
m
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Gayatri', 'Bablu', 'Ammu', 'Akhii']
m.append('Ahalya')
m
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Gayatri', 'Bablu', 'Ammu', 'Akhii', 'Ahalya']
names
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Gayatri', 'Bablu', 'Ammu', 'Akhii', 'Ahalya']
#m=names it is like deep copy if we change the values or modify in the new list it will also changes in the original list
m.removes('Gayatri')
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    m.removes('Gayatri')
AttributeError: 'list' object has no attribute 'removes'. Did you mean: 'remove'?
m.remove('Gayatri')
m
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Bablu', 'Ammu', 'Akhii', 'Ahalya']
names
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Bablu', 'Ammu', 'Akhii', 'Ahalya']
l.copy(names)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    l.copy(names)
TypeError: list.copy() takes no arguments (1 given)
max(m)
'Thanmai'
min(m)
'Ahalya'
len(m)
10
l=[1,2,3,4,5]
sum(l)
15
l=[2,3.4,5.6]
sum(l)
11.0
l=['manu',8,9.5]
sum(l)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    sum(l)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
#sum is used to add only numbers

l=[0,0.0,'',[],set (), (),{}, False]
l
[0, 0.0, '', [], set(), (), {}, False]
any()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    any()
TypeError: any() takes exactly one argument (0 given)
any(l)
False
>>> all(1)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    all(1)
TypeError: 'int' object is not iterable
>>> all(l)
False
>>> l.append(1)
>>> l
[0, 0.0, '', [], set(), (), {}, False, 1]
>>> any(l)
True
>>> all(l)
False
>>> m
['Thanmai', 'Siddu', 'Rohan', 'Pranav', 'Manu', 'Kuttuu', 'Bablu', 'Ammu', 'Akhii', 'Ahalya']
>>> all(m)
True
>>> any(m)
True
>>> # any is used to check the list that any one is true or false
>>> # all is used to check the list that all the elemets are true or false
>>> # copy is used to return shallow copy of the original list
>>> #if we use copy it wont change the original list when we do any modifications in the new list

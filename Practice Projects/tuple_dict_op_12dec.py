Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Tuple : Collection of data and it allows the duplicates and it is orderd.
#It is heterogenous and we cannot modify.

#Tuple is immutable so that these are faster than lists.
#creating a tuple

t=()
t=tuple()
t=(1,2,3,4)
t
(1, 2, 3, 4)
t = (1,1,2,3,4,4,4,5)
t
(1, 1, 2, 3, 4, 4, 4, 5)
t=(1,1.1,"string",[],{},(),{1,22})
t
(1, 1.1, 'string', [], {}, (), {1, 22})
t=((1,1),(2,2),(3,3))
t
((1, 1), (2, 2), (3, 3))
#Operations of tuple
t
((1, 1), (2, 2), (3, 3))
t(1,2,3)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t(1,2,3)
TypeError: 'tuple' object is not callable
t=(1,2,3)
s=(2,3,4)
t+s
(1, 2, 3, 2, 3, 4)
t*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
4 in t
False
1 in t
True
1 not in
SyntaxError: invalid syntax
1 not in t
False
#indexing and slicing
lang=('java','python','c','c++','js','html')
lang[2]
'c'
lang[-1]
'html'
lang[-3]
'c++'
lang[1]
'python'
lang[0]
'java'
lang[-2]
'js'
lang[:3]
('java', 'python', 'c')
lang[-3:]
('c++', 'js', 'html')
lang[3:5]
('c++', 'js')
lang[::2]
('java', 'c', 'js')
a=1,2,3,4
a
(1, 2, 3, 4)
t=(1,2,3)
a,b,c=t
a
1
b
2
3
3
4
4
c
3
d
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d
NameError: name 'd' is not defined
e
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    e
NameError: name 'e' is not defined
res=("manu","manu@gmail.com","mn@123")
res.count("manu")
1
res.index("mn@123)
          
SyntaxError: unterminated string literal (detected at line 1)
res.index("mn@123")
          
2
len(res)
          
3
min(res)
          
'manu'
max(res)
          
'mn@123'
sorted(res)
          
['manu', 'manu@gmail.com', 'mn@123']
t=
          
SyntaxError: invalid syntax
t=(1,2,3,4,5)
          
sum(t)
          
15
t=(1,2,3,[4,5],6,7)
          
t[0]=1
          
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    t[0]=1
TypeError: 'tuple' object does not support item assignment
t[3].append(9)
          
t
          
(1, 2, 3, [4, 5, 9], 6, 7)
t[4].append(8)
          
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t[4].append(8)
AttributeError: 'int' object has no attribute 'append'
t[3].append(8)
          
t
          
(1, 2, 3, [4, 5, 9, 8], 6, 7)
t=({1,2},{3,4})
          
t[0].add(30)
          
t
          
({1, 2, 30}, {3, 4})


#Dictionary is ordered ,mutable and stores key-value pairs.
          
#These are indexed by position, dictionaries are indexed by unique keys.
          
d={}
          
d{1:2,2:3,3:4}
          
SyntaxError: invalid syntax
d={1:2,2:3,3:4}
          
d
          
{1: 2, 2: 3, 3: 4}
s={6:7}
          
d
          
{1: 2, 2: 3, 3: 4}
d+s
          
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    d+s
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
s[0]
          
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s[0]
KeyError: 0
d[0]
          
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    d[0]
KeyError: 0
s*2
          
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s*2
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
2 in d
          
True
5 in d
          
False
#membership operations only works for the keys
          
d[4]
          
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    d[4]
KeyError: 4
d
          
{1: 2, 2: 3, 3: 4}
d[3]
          
4
data={'name':'manu','batchno':44,'course':'pfs'}
          
data
          
{'name': 'manu', 'batchno': 44, 'course': 'pfs'}
data['name']
          
'manu'
data['course']
          
'pfs'
data['age']
          
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age')
          
data.get('name')
          
'manu'
#in normal extraction of elements if it is not there it shows errors but where as in get method it executed but nothing will print
          
data.get('age','key is not there')
          
'key is not there'
data.get('name','key is not there')
          
'manu'
data
          
{'name': 'manu', 'batchno': 44, 'course': 'pfs'}
data.setdefault('age',21)
          
21
d
          
{1: 2, 2: 3, 3: 4}
data
          
{'name': 'manu', 'batchno': 44, 'course': 'pfs', 'age': 21}
data.setdefault('name','usha')
          
'manu'
#setdefault is used to add the key and value to the tuple when there is no value in the dictionary
          
data.get('dob')
          
data.setdefault('dob','01-09-2004')
          
'01-09-2004'
data
          
{'name': 'manu', 'batchno': 44, 'course': 'pfs', 'age': 21, 'dob': '01-09-2004'}
d={1:1,2:4,3:9,4:16}
          
d
          
{1: 1, 2: 4, 3: 9, 4: 16}
d.setdefault(5,20)
          
20
d
          
{1: 1, 2: 4, 3: 9, 4: 16, 5: 20}
d={1:'int'}
          
d[1.1]='float'
          
d['str']='string'
          
d[[1,2,3]]='list'
          
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
d[{1:2}]='dict'
          
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    d[{1:2}]='dict'
TypeError: unhashable type: 'dict'
>>> d[(1,2)]='tuple'
...           
>>> d
...           
{1: 'int', 1.1: 'float', 'str': 'string', (1, 2): 'tuple'}
>>> d[1]=23
...           
>>> d
...           
{1: 23, 1.1: 'float', 'str': 'string', (1, 2): 'tuple'}
>>> d[{1,2}]='set'
...           
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    d[{1,2}]='set'
TypeError: unhashable type: 'set'
>>> d
...           
{1: 23, 1.1: 'float', 'str': 'string', (1, 2): 'tuple'}
>>> d['str']='string datatype'
...           
>>> d
...           
{1: 23, 1.1: 'float', 'str': 'string datatype', (1, 2): 'tuple'}

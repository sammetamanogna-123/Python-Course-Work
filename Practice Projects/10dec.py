Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python programming'
len(s)
18
len('p t')
3
ord
<built-in function ord>
ord('a')
97
ord('z')
122
ord('A')
65
ord('Z')
90
ord('0')
48
ord(' ')
32
max(s)
'y'
min(s)
' '
chr(' ')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    chr(' ')
TypeError: 'str' object cannot be interpreted as an integer
chr(1)
'\x01'
ord('@')
64
chr(128578)
'🙂'
chr(128579)
'🙃'
chr(128573)
'😽'
chr(s)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    chr(s)
TypeError: 'str' object cannot be interpreted as an integer
chr(s)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    chr(s)
TypeError: 'str' object cannot be interpreted as an integer
chr(50)
'2'
ord('@')
64
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
sorted(s, reverse=True)
['y', 't', 'r', 'r', 'p', 'p', 'o', 'o', 'n', 'n', 'm', 'm', 'i', 'h', 'g', 'g', 'a', ' ']
chr(128560)
'😰'
chr(87650)
'\U00015662'
chr(1285698)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    chr(1285698)
ValueError: chr() arg not in range(0x110000)
chr(110000)
'\U0001adb0'
sorted(s.reverse)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sorted(s.reverse)
AttributeError: 'str' object has no attribute 'reverse'
s
'python programming'
s.split()
['python', 'programming']
s.split('o')
['pyth', 'n pr', 'gramming']
s.split('r')
['python p', 'og', 'amming']
s.split('a')
['python progr', 'mming']
s.split('m')
['python progra', '', 'ing']
s='jaba,python,html,css,javascript,flask'
s.split(',')
['jaba', 'python', 'html', 'css', 'javascript', 'flask']
s='manognais')
SyntaxError: unmatched ')'
s='manognais'
s.split()
['manognais']
s='manu is a good girl'
s.rsplit()
['manu', 'is', 'a', 'good', 'girl']
s.rsplit(' ',2)
['manu is a', 'good', 'girl']
s.split(' ',2)        #from right side it is starts splitting
['manu', 'is', 'a good girl']
s.rsplit(' ',2)       #from left side it is starts splitting
['manu is a', 'good', 'girl']
s='''
manu
is
good'''
s
'\nmanu\nis\ngood'
s.splitlines()        #when we use multi lines and when we want to do the line by line spliting
['', 'manu', 'is', 'good']
s='teju is good boy'
s.partition(' ')        #it splits from the right side but upto the first coming space
('teju', ' ', 'is good boy')
s.rpartition(' ')      #it splits from the left side but upto the first coming space
('teju is good', ' ', 'boy')
#rsplit = from right side , rpartition = from right side , partition = left side, split = left side
l='python,java,css,html,js,django,flask'
l
'python,java,css,html,js,django,flask'
' '.join(l)
'p y t h o n , j a v a , c s s , h t m l , j s , d j a n g o , f l a s k'
'@'.join(l)
'p@y@t@h@o@n@,@j@a@v@a@,@c@s@s@,@h@t@m@l@,@j@s@,@d@j@a@n@g@o@,@f@l@a@s@k'
'@'.join()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    '@'.join()
TypeError: str.join() takes exactly one argument (0 given)
','.join(l)
'p,y,t,h,o,n,,,j,a,v,a,,,c,s,s,,,h,t,m,l,,,j,s,,,d,j,a,n,g,o,,,f,l,a,s,k'
''.join(l)
'python,java,css,html,js,django,flask'
'@' .join(l)
'p@y@t@h@o@n@,@j@a@v@a@,@c@s@s@,@h@t@m@l@,@j@s@,@d@j@a@n@g@o@,@f@l@a@s@k'
''.join(l)
'python,java,css,html,js,django,flask'
l=['python', 'java', 'flask']
l
['python', 'java', 'flask']
''.join(l)
'pythonjavaflask'
'the'.join(l)
'pythonthejavatheflask'
'  ===  '.join(l)
'python  ===  java  ===  flask'
'@'.join(l)
'python@java@flask'
' '.join(l)
'python java flask'
'is'.join(l)
'pythonisjavaisflask'
'and'.join(l)
'pythonandjavaandflask'
'and '.join(l)
'pythonand javaand flask'
' and '.join(l)
'python and java and flask'


#whitespaces and trimming methods
#strip(chars)
#lstrip(chars) = it removes spaces from left side
#rstrip(chars) = it removes spaces from right side

s='     python      java      '
s
'     python      java      '
s.strip()
'python      java'
s.lstrip()
'python      java      '
s.rstrip()
'     python      java'
# encode is used to convert the data into bytes
# decode is used to convert the bytes into data
text = 'hello '
text.encode()
b'hello '
text.decode()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
b'hello '.decode()
'hello '
#string testing methods
s='python programming'
s
'python programming'
s='usha is crazy girl'
s
'usha is crazy girl'
s.stratswith('usha')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    s.stratswith('usha')
AttributeError: 'str' object has no attribute 'stratswith'. Did you mean: 'startswith'?
s.startswith('usha')
True
s.endswith('girl')
True
s.endswith('boys')
False
s.startswith('manu')
False
#isalpha = checks that all the things in the alphabets or noy
'usha'.isalpha()
True
'123usha'.isalpha()
False
#isalnum = checks that all are numbers or not
'123'.isalnum()
True
'a1234'.isalnum()
True
#islower = checks that all are lowercase or not
'usha'.islower()
True
'ushA'.islower()
False
>>> #isupper = checks that all are uppercase or not
>>> 'usha'.isupper()
False
>>> 'ushA'.isupper()
False
>>> 'USAD'.isupper()
True
>>> ''.isspace()
False
>>> '  '.isspace()
True
>>> #istitle = every words have first letter should be capital
>>> s='Manu Usha'
>>> s
'Manu Usha'
>>> s.istitle()
True
>>> s='manu Usha'
>>> s.istitle()
False
>>> #isidentifier = checks whether it is identifier or not
>>> 'myvar'.isidentifier()
True
>>> '12var'.isidentifier()
False

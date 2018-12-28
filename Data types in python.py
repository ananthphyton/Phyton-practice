Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5.8
>>> b = int(a)
>>> ab
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ab
NameError: name 'ab' is not defined
>>> a,b
(5.8, 5)
>>> a >ArithmeticError b
SyntaxError: invalid syntax
>>> bool
<class 'bool'>
>>> k = 7
>>> b > k
False
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> int(False)
0
>>> range(10)
range(0, 10)
>>> lst(range(10))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    lst(range(10))
NameError: name 'lst' is not defined
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,11,2))
[2, 4, 6, 8, 10]
>>> #none,numeric,list,set,string,dictinory data types exists in python

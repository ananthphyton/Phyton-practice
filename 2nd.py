Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> id(num)
1771886832
>>> name = 'ananth'
>>> id(name)
89483296
>>> a = 10
>>> b = a
>>> id(a)
1771886912
>>> id(b)
1771886912
>>> a
10
>>> b
10
>>> id(10)
1771886912
>>> k =10
>>> id(k)
1771886912
>>> a = 9
>>> id(a)
1771886896
>>> b
10
>>> #all equal values will have same address in python
>>> PI = 3.14
>>> type
<class 'type'>
>>> type(PI)
<class 'float'>
>>> 

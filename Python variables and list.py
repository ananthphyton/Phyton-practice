Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> _+5
10
>>> name = 'anantha kumar'
>>> name[10]
'm'
>>> len(name)
13
>>> min(name)
' '
>>> max(name)
'u'
>>> nums = [1,5,9,11]
>>> nums
[1, 5, 9, 11]
>>> nums[2]
9
>>> nums[2:]
[9, 11]
>>> nums[-1]
11
>>> nums[-4]
1
>>> names['ananth','kumar','kiran','rajendra']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    names['ananth','kumar','kiran','rajendra']
NameError: name 'names' is not defined
>>> names = ['ananth','kumar','kiran','rajendra']
>>> names
['ananth', 'kumar', 'kiran', 'rajendra']
>>> numnames =[nums,names]
>>> numnames
[[1, 5, 9, 11], ['ananth', 'kumar', 'kiran', 'rajendra']]
>>> nums.append(30)
>>> nums
[1, 5, 9, 11, 30]
>>> nums.insert(1,15)
>>> nums
[1, 15, 5, 9, 11, 30]
>>> nums.pop()
30
>>> nums
[1, 15, 5, 9, 11]
>>> min
<built-in function min>
>>> min(nums)
1
>>> sum(nums)
41
>>> nums.sort()
>>> nums
[1, 5, 9, 11, 15]
>>> nums.
SyntaxError: invalid syntax
>>> nums.reverse()
>>> nums
[15, 11, 9, 5, 1]
>>> # Lists are immutable
>>> count(nums)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    count(nums)
NameError: name 'count' is not defined
>>> nums.count()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    nums.count()
TypeError: count() takes exactly one argument (0 given)
>>> nums.count
<built-in method count of list object at 0x05E9C198>
>>> nums.count[]
SyntaxError: invalid syntax
>>> nums.count[2:]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    nums.count[2:]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.count(1)
1
>>> nums.append(1)
>>> nums
[15, 11, 9, 5, 1, 1]
>>> nums.count(1)
2
>>> #tuple are immutable and lists are mutable
>>> # we have another one called sets. These are coded in { braket. we use sets to receive the data quickly and it does not contain duplicates.
>>> 

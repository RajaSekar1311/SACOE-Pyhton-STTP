Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1=[1,2,3,4,5]
>>> list1
[1, 2, 3, 4, 5]
>>> list1.append(6)
>>> list1
[1, 2, 3, 4, 5, 6]
>>> l=[1,3,2,6,5,8,4]
>>> min(l)
1
>>> max(l)
8
>>> sum(l)
29
>>> sorted(l)
[1, 2, 3, 4, 5, 6, 8]
>>> reversed(l)
<list_reverseiterator object at 0x02968570>
>>> list(reversed(l))
[4, 8, 5, 6, 2, 3, 1]
>>> 8 in l
True
>>> 7 in l
False
>>> 8 not in l
False
>>> t=['a','b','c','d']
>>> t.pop()
'd'
>>> s=t.pop()
>>> t
['a', 'b']
>>> l1=[25,10]
>>> l2=l1
>>> print(l1)
[25, 10]
>>> print(l2)
[25, 10]
>>> l1[0]=20
>>> l1
[20, 10]
>>> l2
[20, 10]
>>> l2[1]=50
>>> l1
[20, 50]
>>> l2
[20, 50]
>>> a=[5,10]
>>> b=list(a)
>>> a
[5, 10]
>>> b
[5, 10]
>>> a[0]=20
>>> a
[20, 10]
>>> b
[5, 10]
>>> [i**3 for i in [1,2,3,4] if i>2]
[27, 64]
>>> n1=list(range(1,10))
>>> sq=[n*n for n in n1]
>>> osr=[n*n for n in n1 if n%2==1]
>>> n1
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sq
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> osr
[1, 9, 25, 49, 81]
>>> mt=(",ouse", [1,12,2],(1,2,3))
>>> mt[0]
',ouse'
>>> mt[0][1]
'o'
>>> mt[1][0]
1
>>> mt[1]
[1, 12, 2]
>>> mt[2]
(1, 2, 3)
>>> a,b,c=1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> a,b=1,2,3
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a,b=1,2,3
ValueError: too many values to unpack (expected 2)
>>> m=()
>>> m=(1,2,3)
>>> m
(1, 2, 3)
>>> tup=1,
>>> tup
(1,)
>>> l11=[1,2,3]
>>> tuple(l11)
(1, 2, 3)
>>> 

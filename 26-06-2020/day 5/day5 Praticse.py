Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> da={}
>>> da
{}
>>> type(da)
<class 'dict'>
>>> da={'name':'raja',}
>>> da
{'name': 'raja'}
>>> len(da)
1
>>> da['year']=1989
>>> da
{'name': 'raja', 'year': 1989}
>>> len(da)
2
>>> 1
1
>>> print("length:", len(da))
length: 2
>>> print("length: %d", %len(da))
SyntaxError: invalid syntax
>>> 
>>> print("length: %d" %len(da))
length: 2
>>> da['name']='ravi'
>>> da
{'name': 'ravi', 'year': 1989}
>>> da.pop(year)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    da.pop(year)
NameError: name 'year' is not defined
>>> da.pop('year')
1989
>>> da
{'name': 'ravi'}
>>> 
>>> len(da)
1
>>> da['YEAR']=1989
>>> DA
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    DA
NameError: name 'DA' is not defined
>>> da
{'name': 'ravi', 'YEAR': 1989}
>>> sorted(da..keys())
SyntaxError: invalid syntax
>>> sorted(da.keys())
['YEAR', 'name']
>>> d={x:x**3 for x in range(10) if x%2==1}
>>> d
{1: 1, 3: 27, 5: 125, 7: 343, 9: 729}
>>> f1=open("sample.txt","w")
>>> f1.write("welcome to cse")
14
>>> f1.close()
>>> 
================= RESTART: C:/Users/SYS/Desktop/day 5/wrt.py =================
ok
>>> 
================ RESTART: C:/Users/SYS/Desktop/day 5/grade.py ================
Enter the name of input file to read the grades from: letterstxt
Enter the name of the output file to record the GPA's to: GPA
Traceback (most recent call last):
  File "C:/Users/SYS/Desktop/day 5/grade.py", line 4, in <module>
    inputFile = open(inputFileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: 'letterstxt'
>>> 
================ RESTART: C:/Users/SYS/Desktop/day 5/grade.py ================
Enter the name of input file to read the grades from: letterstxt
Enter the name of the output file to record the GPA's to: GPA.txt
Traceback (most recent call last):
  File "C:/Users/SYS/Desktop/day 5/grade.py", line 4, in <module>
    inputFile = open(inputFileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: 'letterstxt'
>>> 
================ RESTART: C:/Users/SYS/Desktop/day 5/grade.py ================
Enter the name of input file to read the grades from: letters
Enter the name of the output file to record the GPA's to: gpa
Traceback (most recent call last):
  File "C:/Users/SYS/Desktop/day 5/grade.py", line 4, in <module>
    inputFile = open(inputFileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: 'letters'
>>> 

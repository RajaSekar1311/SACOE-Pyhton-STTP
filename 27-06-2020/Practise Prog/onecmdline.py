import sys
count=len(sys.argv)
print ("The number of arguments is:",count)
for i in range(count):
	print ("The argument is",sys.argv[i],"lengt is:",len(sys.argv[i]))

inputFileName = input("Enter the name of input file to read the grades from: ")
outputFileName = input("Enter the name of the output file to record the GPA's to: ")

inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")
   
print("Opening file", inputFileName, " for reading.")
print("Opening file", outputFileName, " for writing.")
gpa = 0
for line in inputFile:
    if (line[0] == "A"):
        gpa = 4
    elif (line[0] == "B"):
        gpa = 3
    elif (line[0] == "C"):
        gpa = 2
    elif (line[0] == "D"):
        gpa = 1
    elif (line[0] == "F"):
        gpa = 0
    else:
        gpa = -1
    temp = str (gpa)
    temp = temp + '\n'
    print (line[0], '\t', gpa)
    outputFile.write (temp)
inputFile.close ()
outputFile.close () 
print ("Completed reading of file", inputFileName)
print ("Completed writing to file", outputFileName)

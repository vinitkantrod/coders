import sys

file_name = raw_input("Enter file name : ")
if len(file_name) == 0:
    print "Next time please enter correct file name to read it"
    sys.exit()
try:
    file = open(file_name,"r")
except IOError:
    print "There was an error reading file"
    sys.exit()
file_text = file.read()
file.close()
print file_text 

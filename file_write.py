import sys

try:
    file = open('write.txt',"w")
except IOError:
    print "There was an error while writing to a file",write.txt
    sys.exit()

file_finished = "$$"
print "Enter '", file_finished,"' when finished"
file_txt = 'a'
while file_txt != file_finished:
    file_txt = raw_input("Enter text : ")
    if file_txt == file_finished:
        file.close()
        break
    file.write(file_txt)
    file.write("\n")
file.close()

import sys

print "\n\n*********************************************************"
print "\n\t\t\tFile Operations\t\t\t\n"
print "*********************************************************"

print "\nThe operations you can perform here are :"
print "\n\ta) Create"
print "\n\tb) Write"
print "\n\t\tb_1) Write Completely "
print "\n\t\tb_2) Append It"
print "\n\tc) Read"
print "\n\td) Read and Write"
print "\n\te) Delete"
print "\n\tf) Rename"
print "\n\tg) Change Permission\n"
print "\n\th) File Objects Attributes"

input = raw_input("Enter the operation you want to perform(mention only alphabets) : ")

if input == 'a':
    try:
        file_name = raw_input("Enter file name to create : ")
        file = open(file_name,"a+")
        print "File",file_name,"created successfully !!" 
        #sys.exit()
       
    except IOError:
        print "Error while opening file"
        #sys.exit()
    #file.close()
    exit = raw_input("Do you want to continue(press y to continue and enter to exit) :")
    if exit == y:
        
 

elif input == 'h':
    print "\n\t1) File Name"
    print "\n\t2) File Mode"
    print "\n\t3) File Closed ?"
    h_inp = raw_input("Select which attributes you want to see : ")

    if h_inp == 1:
        print "Name of the File : ", file.name
    elif h_inp == 2:
        print "Mode of a File : ",file.mode
    elif h_inp == 3:
        print "Wheather file is closed ? : ", file.closed
    sys.exit()    
            

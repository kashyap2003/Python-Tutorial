# Functions r(read), W(Write), a(Append), r+(Read and Write)

employe_files = open("employees.txt", "r") # From this we are opening file employees.txt with read(r) function.

print(employe_files.readlines()) #this .readlines will take all the lines inside over files and put in a liat.

employe_files.close() # It will close the file that we have oppened.
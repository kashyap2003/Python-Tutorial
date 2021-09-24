# Functions r(read), W(Write), a(Append), r+(Read and Write)

employe_files = open("employees.txt", "r") # From this we are opening file employees.txt with read(r) function.

print(employe_files.read()) #this .read will split the thing which is in file.

employe_files.close() # It will close the file that we have oppened.
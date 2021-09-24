# Functions r(read), W(Write), a(Append), r+(Read and Write)

employe_files = open("employees.txt", "r") # From this we are opening file employees.txt with read(r) function.

print(employe_files.readline()) #this .readline will read an individual line. So, if you want next line print again.
print(employe_files.readline()) #this .readline will read an individual line. So, if you want next line print again.

employe_files.close() # It will close the file that we have oppened.
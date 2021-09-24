# Functions r(read), W(Write), a(Append), r+(Read and Write)

employe_files = open("employees.txt", "r") # From this we are opening file employees.txt with read(r) function.

print(employe_files.readlines()[2]) #this .readlines()[2] will tell what is in index position 2 in our list.

employe_files.close() # It will close the file that we have oppened.
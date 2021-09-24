# Functions r(read), W(Write), a(Append), r+(Read and Write)

employe_files = open("employees.txt", "r") # From this we are opening file employees.txt with read(r) function.

print(employe_files.readable()) #this .readable will tell us if this file is readeble or not in bolean value(T,F).

employe_files.close() # It will close the file that we have oppened.
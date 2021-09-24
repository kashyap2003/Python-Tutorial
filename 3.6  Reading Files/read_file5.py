# Functions r(read), W(Write), a(Append), r+(Read and Write)

employe_files = open("employees.txt", "r") # From this we are opening file employees.txt with read(r) function.

for employee in employe_files.readlines(): # This will print out all the employee inside it one by one.
    print(employee)

employe_files.close() # It will close the file that we have oppened.
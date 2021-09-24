# Functions r(read), W(Write), a(Append), r+(Read and Write)

employe_files = open("employees1.txt", "w") # From this we can overwrite file and this will creat a fileif it doen't exist.

employe_files.write("\nKelly - Customer Service") #It will over write everything in file.

employe_files.close() # It will close the file that we have oppened.
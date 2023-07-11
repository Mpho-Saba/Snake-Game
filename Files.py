#open file
#file = open("my_file.txt")
#contents = file.read()
#print(contents)

#file.open() #this is essential because it ensures resources are unallocated after file use

#instead, use a different method
#with open("my_file.txt") as file: #this is read mode
#    contents = file.read()
#    print(contents)

#if file does not exist, python creates a new file for you, but need to be in write mode 'w'

#write to file
with open("my_file.txt", 'a') as file:
    file.write('\nI am a coder3')
    # w makes sure the file is rewritten from scratch
    #if you want to add and not delete everything, use a for append
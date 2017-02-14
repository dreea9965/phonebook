myfile = open(raw_input("what is the name of the file?"), "w")

myfile.write(raw_input("Add something to the file..."))

myfile.close()

file_contents = open(raw_input("What is the name of the file again?"), 'r')

print file_contents.read()


def printmenu():
    print " "
    print "Electronic Phone Book"
    print " ====================="
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"
    print " "

    exist = int(raw_input("What do you want to do (1-5)?"))


    phonebook = {'Andy': '404-478-4568', 'Lisa': '435-234-5434', 'Maggie': '706-755-7643'}


    while exist > 0:
        if exist == 1:
            name = raw_input("What entry do you want to look up?")
            phonebook[name] = phonebook.get(name)
            print phonebook[name]

        elif exist == 2:
            name = raw_input("Set new entry name and phone number: ")
            phonebook[name] = name
            print name + " has just been added to phonebook."


        elif exist == 3:
            name = raw_input("What entry do you want to delete?")
            del phonebook[name]
            print "Your entry has been deleted"
            print "Remaining contacts:"
            print phonebook.keys()


        elif exist == 4:
            print phonebook


        elif exist == 5:
            print "good bye!"


        else:
            printmenu()

        break

while True:
    printmenu()

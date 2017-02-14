import pickle

phonebook = {'Andy': '404-478-4568', 'Lisa': '435-234-5434', 'Maggie': '706-755-7643'}

myfile = open('phonebook.pickle', 'w')
pickle.dump(phonebook, myfile)
myfile.close

myfile = open('phonebook.pickle', 'r')
phonebook = pickle.load(myfile)

phonebook = {'Andy': '404-478-4568', 'Lisa': '435-234-5434', 'Maggie': '706-755-7643'}
runner = True


def printmenu():
    global phonebook
    global runner

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



    while exist > 0:
        if exist == 1:
            name = raw_input("What entry do you want to look up?")
            phonebook[name] = phonebook.get(name)
            print phonebook[name]

        elif exist == 2:
            name = raw_input("Set new entry name: ")
            number = raw_input("Set new entry number: ")
            phonebook[name] = number
            print name  + number + " has just been added to phonebook."
            print phonebook


        elif exist == 3:
            name = raw_input("What entry do you want to delete?")
            del phonebook[name]
            print "Your entry has been deleted"
            print "Remaining contacts:"
            print phonebook.keys()


        elif exist == 4:
            print phonebook

        while exist >= 5:
            if exist == 5:
                print "good bye!"
                runner = False
            else:
                print "Not a valid entry!"
                printmenu()
            break

        break

while runner == True:
    printmenu()

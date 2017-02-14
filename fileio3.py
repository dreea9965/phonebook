myfile = open(raw_input("what is the name of the file?"))

file_contents = myfile.read()

print file_contents

counts = {}


def word_histogram(text):
    words = text.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    for word, count in counts.items():
        print "[%d : %s]" % (count, word)

word_histogram(file_contents)

def letter_histogram(word):
    for char in word:
        counts[char] = counts.get(char, 0) + 1

    for char, count in counts.items():
        print "[%d: %s]" % (count, char)


letter_histogram(file_contents)

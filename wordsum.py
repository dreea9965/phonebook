counts = {}


def word_histogram(text):
    words = text.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    for word, count in counts.items():
        print "[%d : %s]" % (count, word)

word_histogram('to be or not to be')



# example answer below

def word_histogram(sentence):
    word_list = sentence.split()
    word_lib = {}
    for word in word_list:
        if word not in word_lib:
            word_lib[word] = 1
        else:
            word_lib += 1

    print word_lib
word_histogram('to be or not to be')

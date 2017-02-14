counts = {}

def letter_histogram(word):
    for char in word:
        counts[char] = counts.get(char, 0) + 1

    for char, count in counts.items():
        print "[%d: %s]" % (count, char)


letter_histogram('hello')

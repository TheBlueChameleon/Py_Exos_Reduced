# ============================================================================ #
# problem 1

print("### Characters in a file")

with open("praktische_Physik.txt", "r") as handle :
    content = handle.read()

# manual approach:
total = len(content)
chars = 0
words = 1
lines = 1

for char in content :
    if char == " " :
        words += 1

    if char == "\n" :
        words += 1
        lines += 1
    else :
        chars += 1

print("COUNT MANUALLY:")
print("characters total   :", total)
print("without line breaks:", chars)
print("words              :", words)
print("lines              :", lines)
print()


# better approach: let Python do the tedious work:
with open("praktische_Physik.txt", "r") as handle :
    content = handle.readlines()

lines = len(content)
total = sum(len(line)       for line in content)
chars = sum(len(line) - 1   for line in content) + 1          # - 1: line breaks are part of the variable line. + 1: there's no line break in the last line.
words = sum(line.count(" ") for line in content) + lines      # + lines: each line begins with a word in front of which there is no whitespace.

print("ZWEITE AUSZÄHLUNG:")
print("characters total   :", total)
print("without line breaks:", chars)
print("words              :", words)
print("lines              :", lines)

print("=" * 80)

# ============================================================================ #
# problem 2

print("### File size with tell and seek")

with open("praktische_Physik.txt", "r") as handle :
    handle.seek(0, 2)     # jump to end of file
    lof  = handle.tell()

print("Counting via tell:")
print("Length in characters:", lof)
print()

print("Alternative counting via len():")
with open("praktische_Physik.txt", "rb") as handle :
    data = handle.read()                                                        # reads the content as a bytes object
    text = data.decode(encoding='utf-8')                                        # converts it into a regular UTF-8 string (see below)

print("Length in bytes     :", len(data))                                       # length of the text in characters
print("Length in characters:", len(text))                                       # length of the text in bytes
print()

# Character Encodings (UTF-8, ASCII, ANSI, ...):
# For the computer, letters are just numbers, as we know.
# However, there's different ways of putting numbers on a disk.
# One could use one byte per character, to the effect of having at most 256
# different characters. That is how they used to do up until the mid 2000s.
# Problem: Special characters (e.g. umlaut, asian scripts, ...) do not fit in
# this limited set of characters.
# Another way of putting information on disk would be using multiple bytes per
# character. UTF-16 is a standard that uses 2 Bytes per character and can thus
# use up to 65 536 different characters. While it mitigates one problem, this
# method creates a new one: it wastes a lot of space (most western text only
# uses the first 128 code points).
# Finally, there's UTF-8, which has *variable length encoding*, i.e. the number
# of bytes used per character depends on the character itself. It's a nifty bit
# of technology and I recommend you read into it yourself.
#
# Anyway, in the context of the problem statement:
# The file 'praktische_Physik.txt' uses UTF-8 and umlaut characters. These
# characters take up more space on disk than regular letters, hence the
# difference. A bytes object (as returned from read(binary mode) always counts
# Bytes. The same holds for tell().
# The function len() on the other hand can treat multi-byte characters, if it is
# told so. To that end, we have to explicitly tell Python that the binary data
# read from file are a UTF-8 string. This is done in line 66.
#
# Another way of doing so is by specifying the encoding in the open() command:

print("Alternative counting via len(), encoding in the open command:")
with open("praktische_Physik.txt", "r", encoding='utf-8') as handle :
    text = handle.read()

print("Length in characters:", len(text))

print("=" * 80)

# ============================================================================ #
# problem 3

print("### Total Score")

import csv

# purely with the means shown in the lecture:
with open("gameScores.txt") as handle :
    reader = csv.reader(handle)

    lines = []                        # read the file into a buffer
    for line in reader :
        lines.append(line)

scores = {}                           # create an empty dict
for i, name in enumerate(lines[0]) :  # first line holds 'headlines' which we use as keys for our dict
    scores[name] = sum( int(score[i]) for score in lines[1:] )

for name, score in scores.items() :
    print(f"{name:5}: {score} points")
print()

# another way:
with open("gameScores.txt") as handle :
    reader = csv.reader(handle)

    names = next(reader)
        # the function next hasn't been covered yet.
        # next takes an iterable (i.e. an object that can be iterated over with
        # for), and returns the next element in the container.
        # Not every iterable can be accessed with indices, e.g.
        #   names = reader[0]
        # won't work. Hence, we need this workaround to fetch the headlines
        # outside of a loop.
        #
        # The subsequent for loop catches up where next has left the iterable,
        # i.e. the head line has been skipped.

    scores = {name : 0 for name in names}

    for line in reader :
        for i, points in enumerate(line) :
            scores[names[i]] += int(points)

    # of course you could do all of that without knowing the function next.
    # one way of doing so would be

    # for i, line in enumerate(reader) :
    #    if i == 0 :
    #        scores = {name : 0 for name in line}
    #    else :
    #        for j, points in enumerate(line) :
    #            scores[names[j]] += int(points)

for name, score in scores.items() :
    print(f"{name:5}: {score} Punkte")

print("=" * 80)

# ============================================================================ #
# problem 4

print("### Bookmarks")

import json

def show_structure(data, indent = 0) :
    prefix = "    " *  indent

    for node in data :
        print( prefix + node['name'] )

        if   node['type'] == 'bookmark' :
            print(prefix + "->", node['url'])

        elif node['type'] == 'folder' :
            show_structure(node['content'], indent + 1)

with open("./bookmarks.json", "r") as hFile :
    data = json.load(hFile)

show_structure(data)

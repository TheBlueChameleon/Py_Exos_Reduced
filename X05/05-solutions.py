# ============================================================================ #
# problem 1

print("CROSS SUM")

x      = 543
result = 0

if type(x) != int :
    print("Only defined for integers")

else :
    if (x < 0) :
        print("Only defined for positive integers")
    else :
        while x :
            result  += x % 10
            x      //=     10

print(result)
print()

# take a look at line 9:
# we may pass *any* object as input x. However, in the function we assume
# that x is an integer, i.e. that we can divide it by 10 and that, after a
# number of repetitions, this will give 0.
# That means we manually test whether x is really an integer and deny service
# if not.


# ============================================================================ #
# problem 2

print("FIZZBUZZ")

substitutions = {
    3 : "fizz",
    5 : "buzz",
    7 : "tezz"
}

N = 35

for i in range(1, N+1) :
    special = False
    for divisor, substitute in substitutions.items() :
        if i % divisor == 0 :
            print(substitute, end="")
            special = True

    if not special :
        print(i, end="")

    print(", ", end="")

print("...")
print()


# ============================================================================ #
# problem 3

print("TEXT TO LIST")

dataStr = "1,2, 3,     4.5   , 7777"
# or:
#dataStr = input("Bitte eine Komma-getrennte Liste eingeben: ")

dataNum = [float(datapoint.strip()) for datapoint in dataStr.split(",")]

print(dataNum)
print()


# ============================================================================ #
# problem 4

print("LINE BREAKS")

text = "'E's not pinin'! 'E's passed on! This parrot is no more! He has ceased to be! 'E's expired and gone to meet 'is maker! 'E's a stiff! Bereft of life, 'e rests in peace! If you hadn't nailed 'im to the perch 'e'd be pushing up the daisies! 'Is metabolic processes are now 'istory! 'E's off the twig! 'E's kicked the bucket, 'e's shuffled off 'is mortal coil, run down the curtain and joined the bleedin' choir invisible!! THIS IS AN EX-PARROT!!"

width = 80

currentLine    = ""
currentWidth   = 0
lastWhitespace = 0

print("INPUT:")
print(text)

# ............................................................................ #
# version 1: character steps

print("OUTPUT:")
print("." * width)
for i, char in enumerate(text) :
    if char == ' ' :
        lastWhitespace = i

    currentWidth += 1
    currentLine  += char

    if currentWidth == width :
        lastWord = i - lastWhitespace

        print(currentLine[:-lastWord])

        currentLine  = currentLine[-lastWord:]
        currentWidth = 0

print(currentLine)

# ............................................................................ #
# version 2: word steps

words = text.split()
currentWidth = 0
newLine = False                 # flag: line break directly after the last printed word

print("." * width)
for word in words :
    nextWord = len(word)

    # print the word itself
    if currentWidth + nextWord > width :
        print()
        currentWidth = 0
        newLine = True

    print(word, end="")
    currentWidth += nextWord

    # print the separating whitespace:
    if currentWidth + 1 <= width :
        if newLine :
            newLine = False
        else :
            print(" ", end="")
            currentWidth += 1
    else :
        print()
print()
print("." * width)

#asdf asdfas
# asdfuoin

# ============================================================================ #
# problem 5

print("ERATOSTHENES PRIME SIEVE")

N = 10000

data = [i for i in range(2, N+1)]

for i in data :
    if i == 0 : continue

    for j in range(i+i, N+1, i) :
        data[j-2] = 0

data = [n for n in data if n != 0]

for i in data :
    print(i, end=", ")

print("...")

print()

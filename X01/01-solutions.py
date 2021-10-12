# ============================================================================ #
# Problem 1

# free point for you. If you get your interpreter and some code editor to work
# you've made it ;)

# ============================================================================ #
# Problem 2

# i is int, 
# f is float,
# s is String.
# i + i is still int
# i + f is float (Python tries to preserve as much information as possible)
# i * s is string ("22" -- definition of multiplication of strings)
# f * s triggers an error message, since Python does not know what to do whith 
#   fractions of strings.

# ============================================================================ #
# Problem 3

complexNumber = 1j

# alternatively:
complexNumber = complex(0, 1)

print(complexNumber**2, complexNumber.real, complexNumber.imag)
# Output:
# (-1, 0) 0 -1

# the latter two extract -- surprise -- the real and imaginary part of the
# complex number, as a float

# ============================================================================ #
# Problem 4

text = '"That' + "'s a pity" + '", she said.'

# alternatively:
text = '"That\'s a pity", she said'

print(text)

# ============================================================================ #
# Problem 5

b = 3
h = 4
i = 5

z = (i // b) + 1
s = (i %  b) + 1

print("Row", z, ", Column", s)

# ============================================================================ #
# problem 1

# Locally, i.e. within the scope of swap, this actually does perform a triangle
# exchange. That means, the local variables x_swap and y_swap now reference 
# memory cells such that they have the other variables initial value.
# However, this is disconnected from the state of the module level: neither 
# x_main nor y_main "see" any of the effects done to x_swap and y_swap.
# 
# memory model:
#
# --------+--------+--------+--------+--------+--------+--------+--------+------
#    100  |   101  |   103  |   104  |   105  |   106  |   107  |   108  |  ...
#  x_main | y_main | x_swap | y_swap |        |        |        |        |
#  -> 105 | -> 106 | -> 107 | -> 108 |    2   |    3   |    3   |    2   |
#
# (rows in this picture signify: memory address, variable name, content of the
# memory cell)


# ============================================================================ #
# problem 2

print("PI MONTE CARLO APPROXIMATION")

import random

def getPi(accuracy) :
    N = 0

    for run in range(accuracy) :
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x*x + y*y < 1 : N += 1

    return 4 * N/accuracy

for p in range(10, 15) :
    accuracy = 2**p
    print(f"accuracy: {accuracy:7}, pi ~ {getPi(accuracy)}")

print()


# ============================================================================ #
# problem 3

print("### INTEGRAL (I)")

import math

def integrate(func, start, stop, N) :
  result = 0
  width  = (stop - start) / N

  for i in range(N) :
    x = start + i * width
    result += func(x) * width

  return result

print( integrate(math.exp, 0, 1, 10000) )


# ============================================================================ #
# problem 4

print("RANDOM WALK")

import random           # already imported from task 2, but importing it a second time does precisely nothing

# obligatory part with optional extension 1:
# Basic Simulation with finite width of the road
def simulateDrunkard(N, bias, W) :
    drift = 0
    for step in range(N) :
        r = random.uniform(0, 1)

        if r < bias :
            if drift != -W : drift -= 1
        else :
            if drift != +W : drift += 1

    return drift


# optional extension 2: generation of the histogram list
def getHistogram(K, N, bias, W) :
    outcomes = [simulateDrunkard(N, bias, W) for i in range(K)]
    return {d : outcomes.count(d) for d in range(-W, W+1)}


# optional extension 3: display histogram as chart
def showHistogram(histogram) :
    for d, v in histogram.items() :
        print(f"{d:+3}", "#" * v)


# driver code
runs   = 500            # how often to send the drunkard down the road
N      = 20             # how many steps to take
B      = 10             # width of the road
pLeft  = 0.5            # bias to the left (go left 100% of the time --> 1)

print("three random outcomes:")
print( simulateDrunkard(N, pLeft, B) )
print( simulateDrunkard(N, pLeft, B) )
print( simulateDrunkard(N, pLeft, B) )
print()

print("histogram data:")
histogram = getHistogram(runs, N, pLeft, B)
print( histogram )

print("histogram plot:")
showHistogram( histogram )

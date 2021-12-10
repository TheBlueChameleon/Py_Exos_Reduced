import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import csv
import math
import random

# ============================================================================ #
# problem 2

Xmin = -math.pi
Xmax = +math.pi
Ymin = -5
Ymax = +5
resolution = 100

ticker = lambda x, i : f"{x / math.pi:4.2f}$\pi$"
formatter = FuncFormatter(ticker)

X = [x / resolution for x in range(int(Xmin * resolution), int(Xmax * resolution))]
Y = [math.tan(x) for x in X]

xTicks = [i / 4 * math.pi for i in range(-4, 5)]

fig = plt.figure( figsize=(12,4) )
lft = fig.add_subplot(121)

# find spots where the sign of the plot changes (poles):
splitPoints = [0]
lastSign = Y[0] > 0
for i, y in enumerate(Y) :
    if (y > 0) != lastSign :
        lastSign = (y > 0)
        splitPoints.append(i)
splitPoints.append(len(Y))

# and plot section by section:
for i in range(len(splitPoints) - 1) :
    start = splitPoints[  i  ]
    stop  = splitPoints[i + 1]

    lft.plot(X[start : stop], Y[start : stop], color="steelblue")

# coordinate cross -- your search engine of choice will find them easily
lft.hlines(0, Xmin, Xmax, colors="black")
lft.vlines(0, Ymin, Ymax, colors="black")

lft.set_title ("Heart Beat")
lft.set_xlabel("Angle")
lft.set_ylabel("Slope")

lft.set_ylim(Ymin, Ymax)
lft.set_xticks(xTicks)
lft.xaxis.set_major_formatter(formatter)

# ............................................................................ #
# the heart

rgt = fig.add_subplot(122, projection="polar")

#https://pavpanchekha.com/blog/heart-polar-coordinates.html
heart = lambda t : (math.sin(t) * math.sqrt( abs(math.cos(t)) )) / (math.sin(t) + 7/5) - 2 * math.sin(t) + 2

# another form for the heart can be found here: https://www.pinterest.de/pin/863987509751007911/
#heart = lambda theta : 3.5 - 1.5 * abs(math.cos(theta)) * math.sqrt(1.3 + abs(math.sin(theta))) + math.cos(2 * theta) - 3 * math.sin(theta) + 0.7 * math.cos(12.2 * theta)

resolution = 100
Theta = [t / resolution for t in range(int(2 * resolution * math.pi))]
R = [heart(theta) for theta in Theta]

rgt.plot(Theta, R, "r")

plt.show()

# ============================================================================ #
# problem 3

def bezier (start, end, via2, via1) :
    """
    implements cubic Bézier curves between 'start' and 'end' and smoothly
    approaches via1 and via2 in between.

    see https://youtu.be/aVwxzDHniEw for a beautiful explanation on how they
    work

    start : tuple of two floats, start point of the curve
    end   : tuple of two floats, end   point of the curve
    via1  : tuple of two floats, first deviation point
    via2  : tuple of two floats, second deviation point
    returns : a function f(t) that computes the curve between t in [0...1]

    """

    if not (len(start) == len(end) == len(via1) == len(via2) == 2) :
        raise ValueError("Not a 2D point")

    def inner (t) :
        x = (1-t)**3 * start[0] + 3 *(1-t)**2 * t * via1[0] + 3 * (1-t) * t**2 * via2[0] + t**3 * end[0]
        y = (1-t)**3 * start[1] + 3 *(1-t)**2 * t * via1[1] + 3 * (1-t) * t**2 * via2[1] + t**3 * end[1]
        return (x, y)

    return inner

# ............................................................................ #

def get_smooth_curve (pts_through, pts_via) :
    """
    constructs a smooth curve through all poitns pts_through that goes near the
    points pts_via

    pts_through: list of tuples of two floats
    pts_via    : list of tuples of two floats
    returns: a function f(t) that computes the curve between t in [0...1]

    """

    if len(pts_through) != len(pts_via) :
        raise ValueError("Length of point lists must be equal")

    for through, via in zip(pts_through, pts_via) :
        if not (len(through) == len(via) == 2) :
            raise ValueError("Not a list of 2D points")

    def inner (t) :
        N = len(pts_through) - 1        # number of sections on the curve
        section_id = int(t * N)
        section_t = t * N - int(t * N)


        A = pts_through[section_id    ]
        B = pts_through[section_id + 1]

        if section_id :
            S = pts_via[section_id - 1]
            x = 2 * A[0] - S[0]
            y = 2 * A[1] - S[1]

        else :
            # use the subsequent via point
            x, y = pts_via[section_id + 1]

        C = pts_via    [section_id    ]
        D = (x, y)

        func = bezier(A, B, C, D)

        return func(section_t)



    return inner

# ............................................................................ #
# the problem

N_points = 500
T = [t / N_points for t in range(N_points)]

dotted_through = [(3000,  1), (5000,  0)]
dotted_via     = [(5000, -1), (3000, -1)]

solid_through = [(5000,  0.0), (3000, 2.5), (7500, 2.0), (3000, 4.0), (25000, 4.0), (20000, -2)]
solid_via     = [*solid_through]

dotted_func = get_smooth_curve(dotted_through, dotted_via)
solid_func  = get_smooth_curve( solid_through,  solid_via)

dotted_X, dotted_Y = list(zip(*[dotted_func(t) for t in T]))
solid_X,   solid_Y = list(zip(*[ solid_func(t) for t in T]))

fig = plt.figure( figsize=(8, 6) )
fig.suptitle("Solar Evolution")

plot = fig.add_subplot(111)
plot.set_xlim(25000, 0)
plot.set_ylim(-2, 6)

plot.set_xlabel("Surface Temperature in K")
plot.set_ylabel(r"Luminosity in log($\frac{L}{L_0}$)")

plot.plot(dotted_X, dotted_Y, "b:")
plot.plot( solid_X,  solid_Y, "b")

plot.annotate("T-Tauri phase", xy = (3000, 0.5), xytext= (4500, -1.5), arrowprops={'arrowstyle':'->'})
plot.annotate("now (Main sequence)\nH-burning", xy = (5000, 0.0), xytext= (12500, -1.5), arrowprops={'arrowstyle':'->'})
plot.annotate("He flash\nin 9 bn years", xy = (2200, 3.6), xytext= (2500, 2.0), arrowprops={'arrowstyle':'->'})
plot.annotate("He core burning\nin 9.1 bn years", xy = (9500, 1.8), xytext= (15000, 0.0), arrowprops={'arrowstyle':'->'})
plot.annotate("Asymptotic Giant Branch\nEjection of outer layers", xy = (2500, 5.0), xytext= (15000, 5.0), arrowprops={'arrowstyle':'->'})
plot.annotate("Shrinking Core\nPlanetary Nebula", xy = (20000, 4), xytext = (15000, 3), arrowprops={'arrowstyle':'->'})
plot.annotate("White Dwarf Phse", xy = (20000, -1), xytext = (22000, 0), arrowprops={'arrowstyle':'->'})

plt.show()

# ============================================================================ #
# problem 4

# ............................................................................ #
# read data

with open("transition-probabilties.txt", "r") as handle :
  rdr = csv.reader(handle, delimiter="\t")

  # skip header line:
  line = next(rdr)                                # read first line
  while True :
    if len(line) == 0 :                           # skip empty lines
      line = next(rdr)
      continue

    if line[0].startswith("incoming") :           # we've found the data section when we hit the line starting with "incoming"
      headsX = line[1:]                           # save the column heads, excluding the "incomping/..." string
      break

    line = next(rdr)

  # read data section 1
  headsY = []                                     # line heads of the first data section
  data1  = []                                     # actual data
  for line in rdr :
    if len(line) == 0 : break

    headsY.append(line[0])
    data1.append(line[1:])

  # skip header data in section 2: copy and paste
  line = next(rdr)                                # skip first line
  while True :
    if len(line) == 0 :                           # skip empty lines
      line = next(rdr)
      continue

    if line[0].startswith("incoming") :           # up to the point where "incoming" marks the data section
      break

    line = next(rdr)

  data2 = []
  for line in rdr :
    if not len(line) : break
    data2.append(float(line[1]))


# convert text to numbers
for i, line in enumerate(data1) :
  data1[i] = [float(datapoint) for datapoint in line]

# ............................................................................ #
# complete plot

tickerX = lambda x, i : headsX[int(x)] if x < len(headsX) else f"{x:2.0f}"
tickerY = lambda y, i : headsY[int(y)] if y < len(headsY) else f"{y:2.0f}"

formatterX = FuncFormatter(tickerX)
formatterY = FuncFormatter(tickerY)

fig = plt.figure( figsize=(9,7))
gs  = fig.add_gridspec(1,4)

matView = fig.add_subplot(gs[:3])
barView = fig.add_subplot(gs[3:], sharey=matView)

matView.xaxis.set_major_formatter(formatterX)
matView.yaxis.set_major_formatter(formatterY)

col = matView.pcolor(data1)
barView.barh( range(len(headsY)), data2)
barView.yaxis.set_visible(False)

fig.suptitle("Transmission Experiment")
fig.colorbar(col, ax=barView)
matView.set_title("Transmssions")
matView.set_xlabel("Outgoing configuration")
matView.set_ylabel("Incoming configuration")

barView.set_title("Test Sum")

plt.show()

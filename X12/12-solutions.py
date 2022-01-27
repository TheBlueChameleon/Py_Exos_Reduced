import matplotlib.pyplot as plt
import csv

# ============================================================================ #
# problem 1

print("### Bakeries ###")

allData = []
with open("bakeries.csv", "r") as hFile :
    rdr = csv.reader(hFile)

    heads = next(rdr)

    for line in rdr :
        for i, x in enumerate(line) :
            line[i] = float(x)

        allData.append(line)

X, Y, S, C = tuple(zip(*allData))

plt.scatter(X, Y, S, C, cmap="summer")
plt.title("Bakery Sales in Town")
plt.xlabel(heads[0])
plt.ylabel(heads[1])
plt.colorbar().set_label(heads[3])
plt.show()

# ============================================================================ #
# problem 2

print("### Election Results ###")

colors = (
    "#000000", # CDU/CSU: black
    "#FF0000", # SPD: red
    "#FFFF00", # FDP: yellow
    "#00AA00", # Die Grünen: muted green
    "#00FF00", # Bündnis 90/Die Grünen: green
    "#AA0040", # Die Linke. PDS: blueish red
    "#00A0E0", # AfD: light blue
    "#888888", # Sonstige: grey
)

allData = []
with open("elections.csv", "r") as hFile :                                      # source: https://www.bundestag.de/parlament/wahlen/ergebnisse_seit1949-244692
    rdr = csv.reader(hFile)

    heads = next(rdr)

    for line in rdr :
        for i, x in enumerate(line) :
            try :
                line[i] = float(x)
            except ValueError as e :
                line[i] = 0             # empty cells should be ignored

        allData.append(line)

for i, year in enumerate(allData) :
    plt.pie(year[1:],
            labels = heads[1:] if i == 1 else None,
            radius = 1.25 - (i / 20),
            colors=colors,
            wedgeprops={'width' :0.05}
           )

plt.title("Deutsche Bundestagswahlen, 1949–2021")

plt.show()

# ============================================================================ #
# problem 3

print("### Predator/Prey: Lotka–Volterra Model ###")

# model parameters

x =  10         # number of rabbits
y =   5         # number of wolves

a = 1.0         # birth rate of rabbits
b = 0.3         # death rate of rabbits
c = 0.1         # birth rate of wolves
d = 0.3         # death rate of wolves

dt = 0.0001     # 1/T: granularity of the time step

years = 100     # how long to simuate

# simulation start

wolves  = []
rabbits = []

for step in range( int(years / dt) ) :
    if not (step % int(1/dt)) :             # append() takes considerable time.
        rabbits.append(x)                   # Also, having 10 000 values per year consumes A LOT of memory and doesn't add to the quality of the plot
        wolves .append(y)                   # Hence I make it easier on the machine and record only one value per year.

    x += (a * x     - b * x * y) * dt
    y += (c * x * y - d     * y) * dt

    if x < 0 or y < 0 : break

plt.plot(rabbits, label = "rabbits")
plt.plot(wolves , label = "wolves")

plt.xlabel("Time in years")
plt.ylabel("Population")
plt.title ("Lotka-Volterra Model")

for i, (x, y) in enumerate(zip(rabbits, wolves)) :
    print(f"Year {i:3}: {x:5.2f} rabbits and {y:5.2f} wolves")

plt.legend()

plt.show()

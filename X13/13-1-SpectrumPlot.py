import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import csv
import math
import random

# ============================================================================ #

class SpectrumPlot :
    def __init__(self, filename = None) :
        # numerical data
        self.wavenumbers = []
        self.intensities = []
        self.minima      = []

        # plot elements
        self.fig = None

        self.suptitle    = "IR Spectrum"
        self.title       = ""

        self.xlabel = "wavenumber (cm$^{-1})$"
        self.ylabel = "reflectance"

        self.linetype = "r-"

        # behaviour parameters for placing the minima arrows
        self.minWidth = 7
        self.minValBaseline = 0.4
        self.minOverlapWidth = 400

        self.plotsReady  = False

        if filename : self.loadFile(filename)

    # ........................................................................ #

    def loadFile(self, filename) :
        self.wavenumbers = []
        self.intensities = []
        self.plotsReady  = False

        # Einlesen
        with open(filename, "r") as handle :
            rdr = csv.reader(handle, delimiter=" ")

            for line in rdr :
                if line[0].startswith('##TITLE') : self.title=line[0][8:]
                if line[0].startswith('##END=')  : break
                if line[0].startswith('#')       : continue

                self.wavenumbers.append( float(line[0]) )
                self.intensities.append( float(line[1]) )

        # Normalize
        factor = 1 / max(self.intensities)
        for i, intensity in enumerate(self.intensities) :
            self.intensities[i] *= factor

        self.findMinima()

    # ........................................................................ #

    def findMinima(self) :
        self.minima = []

        for i, v in enumerate(self.intensities) :
            # we regard data points within +/- self.minWidth from point i.
            # These points need to exist in the first place:
            if i < self.minWidth or i > len(self.intensities) - self.minWidth :
                continue

            # exclude completely flat sections from our analysis
            currentSlice = self.intensities[i-self.minWidth:i+self.minWidth]
            if min(currentSlice) == max(currentSlice) :
                continue

            # v is a local minimum if it is the smallest value in the window:
            if v == min(currentSlice) :
                # from the index (and, by proxy) value of the minimum, we can
                # get x- and y-value which we need for the arrows
                self.minima.append(i)

            # another approach:
            # v will be accepted as a local minimum if:
            # a) the sign of the slope to the left and to the right changes,
            # i.e.:
            #    intensities[i - 1] > v and intensities[i + 1] > v
            # b) the distance v to <maximum of a window around v> is bigger than
            #    some threshold, i.e.:
            #    max(intensities[i - minWidth : i + minWidth]) - v > threshold
            #
            # You might have found different, reasonable solutions to this.

    # ........................................................................ #

    def preparePlot(self) :
        self.fig = plt.figure(figsize=(15,5))
        self.drw = self.fig.add_subplot(111)

        if len(self.wavenumbers) == 0 : raise RuntimeError("No data in the plot")

        self.fig.suptitle(self.suptitle)
        self.drw.set_title(self.title)

        self.drw.plot(self.wavenumbers, self.intensities, self.linetype)

        # reverse x-axis
        wn_max = max(self.wavenumbers)
        wn_min = min(self.wavenumbers)
        self.drw.set_xlim(wn_max, wn_min)

        self.drw.set_xlabel(self.xlabel)
        self.drw.set_ylabel(self.ylabel)

        yOff = self.minValBaseline
        for i, thisMinIdx in enumerate(self.minima) :
            if i > 0 :
                lastMinIdx = self.minima[i - 1]

                if self.wavenumbers[lastMinIdx] - self.wavenumbers[thisMinIdx] < self.minOverlapWidth :
                    yOff += 0.05
                    if yOff > 0.95 : yOff = self.minValBaseline
                else :
                    yOff  = self.minValBaseline

            self.drw.annotate(
                str(self.wavenumbers[thisMinIdx]),
                xy = (self.wavenumbers[thisMinIdx], self.intensities[thisMinIdx]),
                xytext = (self.wavenumbers[thisMinIdx] + .1, yOff),
                arrowprops = {
                    'color'      : 'grey',
                    'headwidth'  : 5,
                    'headlength' : 5,
                    'width'      : .1
                },
                horizontalalignment = 'center'
            )

        self.plotsReady = True

    # ........................................................................ #

    def show(self) :
        if not self.plotsReady : self.preparePlot()
        self.fig.show()

    # ........................................................................ #

# ============================================================================ #
# main: usage

# "out of the box
caffeine = SpectrumPlot("caffeine.jdx")
caffeine.show()

# different labels and line type
ethanol = SpectrumPlot("ethanol.jdx")
ethanol.suptitle = "IR Gas Phase Spectrum"
ethanol.ylabel = "transmittivity"
ethanol.linetype = "b:"
ethanol.show()

# completely artificial data
X_artificial = list(range(900, 7000))
Y_artificial = [math.sin(x / 200) * math.cos(x / 30) for x in X_artificial]

artificial = SpectrumPlot()

artificial.wavenumbers = X_artificial
artificial.intensities = Y_artificial

artificial.suptitle = r"$\sin(\frac{x}{200}) \cdot \cos(\frac{x}{30})$"
artificial.title = "Minima of an arbitrary function"
artificial.xlabel = "X"
artificial.ylabel = "Y"

artificial.findMinima()
artificial.show()

input("Please press Enter to quit")

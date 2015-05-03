import numpy as np
import scipy.io.wavfile
import chop
import matplotlib as mpl

# a bullshit version of a unittest,
# which will at least give me compiler errors :-)


rate, signal = scipy.io.wavfile.read('test.wav')

# a = chop.Chop(rate, signal, 100)

# b = chop.stFFT(rate, signal, 100)

c = chop.AverageEnergy(rate, signal, 100)

chop.AverageEnergyPlot(rate, signal, 100)


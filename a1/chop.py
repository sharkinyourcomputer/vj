import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# the function Chop takes in a signal, 
# its sampling rate, and the desired length 
# of frame in milliseconds, and it returns
# returns a vector of the individual frames

# this is a non-overlapping version. 
# an overlapping version should be written too

def Chop(rate, signal, frame_time):

  n = int(np.floor((rate * frame_time) / 1000))
  # n = number of samples per frame
  
  while True:
    if len(signal) % n == 0:
      break
    else:
      signal = np.append(signal, 0)
  # pad signal with zeros until length is divisible by n
 
  m = len(signal)/n
  output = np.zeros(shape=(m, n))
  
  for j in range(0,m):
    output[j,:]=signal[j*n:j*n+n]
    
  # build an array with len(signal) / n entries,
  # each of which contains an individual frame
  # (i.e. a vector with n entries)

  return(output)    

# the function stFFT takes in a signal,
# its sampling rate, and the desired length
# of frame in milliseconds, and it returns
# a vector containing the Fourier transforms
# of the individual frames.

# this function will call upon a Chop function,
# so the issue overlapping will be dealt with
# in the chop function. 

# later a "Hamming window" will be implemented
# to mollify the maleffects of sharp cutoffs

def stFFT(rate, signal, frame_time):

  chopped = Chop(rate, signal, frame_time)
  # chop up the signal into frames,
  # according to the Chop function
  
  # at this point, one should do something to deal
  # with non-smooth cutoffs: Hamming window
  
  output = np.fft.fft(chopped)
  # apply the FFT 
  
  return(output)
  
# AverageEnergy takes in a signal, its sampling rate,
# and the desired frame time. It then computes the
# short time Fourier transform via stFFT, then averages the 
# power spectrum of each frame. It will return a vector
# of the averages.  
  
def AverageEnergy(rate, signal, frame_time):
  
  ft = stFFT(rate, signal, frame_time)
  m = len(ft[:,1])
  n = len(ft[1,:])
  # take the stFFT of the signal, which is an array
  # of m vectors, each of length n. (m x n)
  # m is the number of frames,
  # n is the number of samples per frame.
    
  output = np.zeros(m)
  # set up a vector of zeros with length equal
  # to the number of frames
  
  for j in range(0, m):
    power = np.square(np.abs(ft[j,:]))
    sum = np.sum(power)
    output[j] = sum / n 
  # compute the average energy of each frame
  
  return(output)
  
def AverageEnergyPlot(rate, signal, frame_time):
  y = AverageEnergy(rate, signal, frame_time)
  x = np.arange(len(y))
  plt.plot(x, y)
  plt.show()
  return()
  
  
  return(output)  
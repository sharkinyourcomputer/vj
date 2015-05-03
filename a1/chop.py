import numpy as np

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
    if len(signal) % n == 0
      break
    else:
      np.append(signal, 0)
  # pad signal with zeros until length is divisible by n
 
  m = len(signal)/n
  output = np.zeros(shape=(m, n))
  
  for j in range(0,m):
    output[j,:]=signal[j:j+n]
    
  # build an array with len(signal) / n entries,
  # each of which contains an individual frame
  # (i.e. a vector with n entries)

  return(output)    
    
    
    
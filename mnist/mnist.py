
import numpy as np
import struct
import matplotlib.pyplot as plt


def LoadImageData(filepath):
  with open(filepath) as f:
    imagedata = f.read()
  # yann.lecun.com/exdb/mnist/
  magic, nimages, nrows, ncols = struct.unpack('>IIII', imagedata[:16])
  assert magic == 2051, (magic, filepath, nitems)
  images = np.zeros((nimages, nrows, ncols))
  npix = nrows * ncols
  for nimage in xrange(nimages):
    images[nimage,:,:] = np.transpose(np.asarray(
        struct.unpack(
            'B' * npix, imagedata[16 + nimage*npix : 16 + (nimage+1)*npix])
        )).reshape(nrows, ncols)
  return images

def LoadLabelData(filepath):
  with open(filepath) as f:
    labeldata = f.read()
  magic, nitems = struct.unpack('>II', labeldata[:8])
  print nitems
  assert magic == 2049, (magic, filepath, nitems)
  return [
      struct.unpack('B', labeldata[8+n:8+n+1])[0]
      for n in xrange(nitems)]


def DemoLoadingData():
  train_images = LoadImageData('train-images-idx3-ubyte')
  train_labels = LoadLabelData('train-labels-idx1-ubyte')

  plt.figure(1);
  plt.imshow(train_images[100,:,:]);
  plt.title(str(train_labels[100]));
  plt.show();

if __name__ == '__main__':
  DemoLoadingData()

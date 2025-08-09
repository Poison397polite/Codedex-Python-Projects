"""Program to create a gif"""

import imageio.v3 as iio

fileNames = ["nyan-cat1.png", "nyan-cat3.png", "nyan-cat2.png", "nyan-cat3.png"]
images = []

for fileName in fileNames:
    images.append(iio.imread(fileName))

iio.imwrite('nyan-cat.gif', images, duration = 500, loop = 0)

# pyframe

# By Newton Cazzaro

# Date: 11/7/2018
#
# Version:     Pyframe 1.0 - Horizontal implementation
#
# Description: Python program for encapsulating and framing pictures dynamically into a grid.
#
# Notes:       Pyframe version 1.0 contains only horizontal implementation due to time-line constraints.
#              For further versions, we are planning in developing vertical and matrix implementation
#              in addition to the already working horizontal implementation.
#
# Input:       Pre-defined pictures of jpg type. I'm using 'Frame_1', 'Frame_2', 'Frame_n'... to
#              determine the number of pictures to be stitched together in numerical order.
#
# Output:      Outputs an array of images stitched together in numerical order. The output will be
#              pyframe.jpg

import sys
from PIL import Image

images = map(Image.open, ['Frame_1.jpg', 'Frame_2.jpg', 'Frame_3.jpg', 'Frame_4.jpg'])
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0

for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('pyframe.jpg')

import os, sys
import numpy as np
from PIL import Image
a = sys.stdin.read()
a = [int(x) for x in a.strip().split(" ")]
print(len(a))
imgs = []
step = 101 * 101
c = 1
for i in range(15):
	imgs.append(a[c*step:(c+1)*step])
	# print(len(imgs), len(imgs[0]))
	im = np.array(imgs[i]).astype(np.uint8)
	im.resize((101, 101))
	im = Image.fromarray(im)
	im.show()
	sys.stdin.read()
	c += 4

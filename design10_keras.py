from PIL import Image
import numpy
import cPickle

img = Image.open('olivettifaces.gif')
# numpy supports conversion from image to ndarray and normalization by dividing 255
# 1140 * 942 ndarray
img_ndarray = numpy.asarray(img, dtype='float64') / 255
# create numpy array of 400*2679
img_rows, img_cols = 57, 47
face_data = numpy.empty((400, img_rows*img_cols))
# convert 1140*942 ndarray to 400*2679 matrix

for row in range(20):
    for col in range(20):
        face_data[row*20+col] = numpy.ndarray.flatten(img_ndarray[row*img_rows:(row+1)*img_rows, col*img_cols:(col+1)*img_cols])

# create label
face_label = numpy.empty(400, dtype=int)
for i in range(400):
    face_label[i] = i / 10

# pickling file
f = open('olivettifaces.pkl','wb')
# store data and label as a tuple
cPickle.dump((face_data,face_label), f)
f.close()
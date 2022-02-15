import json

from matplotlib import pyplot as plt
from skimage import transform
from skimage.exposure import histogram
from skimage.io import imread, imshow

# читаем из файла
with open('settings.json') as json_file:
    json_data = json.load(json_file)

for entry in json_data.keys():
    print(f'Название параметра: {entry}, значение параметра: {json_data[entry]}')

path = json_data['source_image_path']
img = imread(path)
print('Image shape: ', img.shape)

v_scale_xy = json_data['scale_XY']
v_shift_xy = json_data['shift_XY']
v_angle = json_data['angle']

tform = transform.AffineTransform(scale=v_scale_xy, rotation=v_angle, translation=v_shift_xy)
print('transform matrix: \n', tform.params)
img_tf = transform.warp(img, tform)

fig = plt.figure(figsize=(7, 7))
fig.add_subplot(2, 2, 1)
imshow(img)
fig.add_subplot(2, 2, 2)
imshow(img_tf)

hist_red, bins_red = histogram(img[500:600, 300:400, 2])
hist_green, bins_green = histogram(img[500:600, 300:400, 1])
hist_blue, bins_blue = histogram(img[500:600, 300:400, 0])

fig.add_subplot(2, 2, 3)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)

hist_red, bins_red = histogram(img_tf[500:600, 300:400, 2])
hist_green, bins_green = histogram(img_tf[500:600, 300:400, 1])
hist_blue, bins_blue = histogram(img_tf[500:600, 300:400, 0])

fig.add_subplot(2, 2, 4)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)
#show()

fig.savefig(json_data['image_save_path'])

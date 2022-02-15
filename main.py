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



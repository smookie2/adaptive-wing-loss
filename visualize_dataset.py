import matplotlib.pyplot as plt
import skimage.io as io
import os
from utils import load_ann

img_dir = 'dataset/WFLW_images';
ann_path = 'dataset/WFLW_annotations/list_98pt_rect_attr_train_test/list_98pt_rect_attr_test.txt'

imgs = load_ann(ann_path)

print('Number of images: {0}'.format(len(imgs)))

for img in imgs[0:10]:
	_, ax = plt.subplots(figsize=(15, 7.35))
	image_full_path = os.path.join(img_dir, img.image_base_name)
	pix = io.imread(image_full_path)
	ax.imshow(pix)

	plt.show()
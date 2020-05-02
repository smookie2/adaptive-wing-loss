import numpy as np

class WFLWInstance():
	def __init__(self, line, idx):
		self.idx = idx
		line = line.strip().split(' ')

		# convert landmarks
		landmarks_list = list(map(float, line[:196]))
		self.landmarks = []
		for i in range(0, 196, 2):
			self.landmarks.append([landmarks_list[i], landmarks_list[i+1]])
		self.landmarks = np.array(self.landmarks)

		# convert bboxes
		if len(line) == 207:
			self.bbox = list(map(float, line[196:200]))
		else:
			self.bbox = None

		# convert image name
		self.image_base_name = line[-1]
		self.image_first_point = line[0]

def load_ann(ann_path):
	with open(ann_path) as f:
		lines = f.readlines()

		ann_data = []

		idx = 0
		for line in lines:
			wflw_instance = WFLWInstance(line, idx)
			ann_data.append(wflw_instance)
			idx += 1

		return ann_data
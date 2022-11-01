
import cv2 as cv
import detectron2
from detectron2.data import DatasetFromList
from detectron2.utils.visualizer import Visualizer
from detectron2.structures import BoxMode
import keras
import numpy as np
import os
import pandas as pd
import sklearn as sk
import tensorflow
import time

from q8.ImageDataInfo import ImageDataInfo

data = []
data_path = "data/agri_data"
classes = []


"""
Read in the classification classes and create an array <data> which consists of an ImageDataInfo for each piece of data
in <path>/data
"""
def read_data(path=data_path, data=[], sample_size=10):
	classesf = open(path + "/../classes.txt")
	for line in classesf:
		classes.append(line.strip())

	files = os.listdir(data_path + "/data")
	for i in range(sample_size):
		dat = dict()
		dat["annotations"] = None
		if files[i*2-1].endswith(".jpeg"):
			dat["file_name"] = data_path + "/data/" + files[i*2-1]
			imTxt = open(data_path + "/data/" + files[i*2], mode='r').readline().strip()
		elif files[i*2-1].endswith(".txt"):
			dat["file_name"] = data_path + "/data/" + files[i*2]
			imTxt = open(data_path + "/data/" + files[i*2-1], mode='r').readline().strip()
		else:
			print("Got bad file extension")
			continue
		im = cv.imread(dat["file_name"])
		imBBox = [int(float(imTxt.split(' ')[1])*len(im)),
				  int(float(imTxt.split(' ')[2])*len(im[0])),
				  int(float(imTxt.split(' ')[3]) * len(im)),
				  int(float(imTxt.split(' ')[4]) * len(im[0]))]
		dat["height"] = len(im[0])
		dat["width"] = len(im)
		dat["image_id"] = dat["file_name"]
		dat["annotations"] = [dict({"bbox": imBBox,
									"bbox_mode": BoxMode.XYWH_ABS,
									"category_id": 0})]
		data.append(dat)
	return data


"""
Classification technique used in (a).
Follows tutorial here:
https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5#scrollTo=0d288Z2mF5dC
"""
def detectron2(data, classes=classes):
	dataset = DatasetFromList(data)
	for d in dataset:
		img = cv.imread(d["file_name"])
		visualizer = Visualizer(img[:, :, ::-1], scale=0.5)
		out = visualizer.draw_dataset_dict(d)
		cv.imshow('window', out.get_image()[:, :, ::-1])


"""
Classification technique used in (b).
Follows the OpenCV tutorial:
https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html
"""
def yolo(data, classes=classes):
	colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')
	net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
	net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
	ln = net.getLayerNames()
	# ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
	for i in range(len(data)):
		img = cv.imread(data[i]["file_name"])
		blob = cv.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)
		r = blob[0, 0, :, :]
		cv.imshow('blob', r)
		text = f'Blob shape={blob.shape}'
		# cv.displayOverlay('blob', text)
		cv.waitKey(1)
		net.setInput(blob)
		t0 = time.time()
		outputs = net.forward(ln)
		t = time.time()
		print('time =', t - t0)
		# print(len(outputs))
		# for out in outputs:
		# 	print(out.shape)

		# def trackbar2(x):
		confidence = 50 / 100

		cv.imshow('blob', r)
		text = f'Bbox confidence={confidence}'
		#cv.displayOverlay('blob', text)

		r0 = blob[0, 0, :, :]
		r = r0.copy()
		cv.imshow('blob', r)
		# cv.createTrackbar('confidence', 'blob', 50, 101, trackbar2)
		# trackbar2(50)

		boxes = []
		confidences = []
		classIDs = []
		h, w = img.shape[:2]
		for output in outputs:
			if len(output) < 5:
				continue
			if output[4].any() > confidence:
				x, y, w, h = output[:4]
				p0 = int((x[0] - w[0] / 2) * 416), int((y[0] - h[0] / 2) * 416)
				p1 = int((x[0] + w[0] / 2) * 416), int((y[0] + h[0] / 2) * 416)
				cv.rectangle(r0, p0, p1, 1, 1)

		for output in outputs:
			for detection in output:
				scores = detection[5:]
				classID = np.argmax(scores)
				confidence = scores[classID % len(scores)]
				if confidence.any() > 0.5:
					box = detection[:4, :5, 0] * np.array([w, h, w, h])[:, :5]
					(centerX, centerY, width, height) = box.astype("int")
					x = int(max(centerX) - (max(width) / 2))
					y = int(max(centerY) - (max(height) / 2))
					box = [x, y, int(max(width)), int(max(height))]
					boxes.append(box)
					confidences.append(confidence)
					classIDs.append(classID)

		indices = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
		if len(indices) > 0:
			for i in indices.flatten():
				(x, y) = (boxes[i][0], boxes[i][1])
				(w, h) = (boxes[i][2], boxes[i][3])
				color = [int(c) for c in colors[classIDs[i]]]
				cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
				text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
				cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

		cv.imshow('window', img)
		cv.waitKey(0)
		cv.destroyAllWindows()


"""
Classification technique used in (c)
"""
def technique2_TBD():
	pass


# Preliminary
data = read_data()


# (a): Faster RCNN Image Classification technique
detectron2(data)


# (b): YOLO Classification technique
#yolo(data)


# (c): Transfer learning on new object class
technique2_TBD()

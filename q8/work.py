

import os

data = []
data_path = "data/agri_data"


"""
Read in the classification classes and create an array <data> which consists of an ImageDataInfo for each piece of data
in <path>/data
"""
def read_data(path=data_path, data=[]):
	classesf = os.open(path + "/classes.txt", 1)
	classes = []
	for line in classesf:
		classes.append(line.remove("\n"))
	return data


"""
Classification technique used in (a).
"""
def technique1_TBD():
	pass


"""
Classification technique used in (b)
"""
def yolo():
	pass


"""
Classification technique used in (c)
"""
def technique2_TBD():
	pass


# Preliminary
data = read_data()


# (a): TBD Image Classification technique
technique1_TBD()


# (b): YOLO Classification technique
yolo()


# (c): Transfer learning on new object class
technique2_TBD()

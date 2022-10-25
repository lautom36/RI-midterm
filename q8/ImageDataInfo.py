

class ImageDataInfo:
	b_box_points = []  # bounding box vertices
	b_box_center = (0,0)
	b_box_length = 0
	b_box_width = 0
	image_name = "DEFAULT"

	def __init__(self, b_box, name):
		if b_box is None:
			print("No bounding box information provided")
		else:
			self.b_box_points = b_box
			# TODO: Other b_box calculations
		if name is None:
			print("Box is nameless")
		else:
			self.image_name = name

	# TODO: Other methods

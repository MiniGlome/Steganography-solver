from PIL import Image
import numpy as np

def compute_layers(array, mode, filename):
		# Compute each bits visual image for a given layer
		for i in range(8):  # 8 bits layer
			newdata = (array >> i) % 2 * 255  # Highlighting the layer bit 'i'
			if mode == 'RGBA':  # Force alpha layer (4th) to 255 if exist
				newdata[:, :, 3] = 255
			Image.fromarray(newdata, mode).save(f"Views/{filename}_{i+1}.png")

def extract_views(path):
	img = Image.open(path)

	if img.mode == "RGBA":
		print("[+] Image in RGBA mode")
	elif img.mode == "RGB":
		print("[+] Image in RGB mode")
	elif img.mode in ["P", "1", "L", "LA", "RGBX", "RGBa", "CMYK", "LAB", "YCbCr", "HSV", "I", "F"]:
		img = img.convert('RGBA')
		print("[+] Image converted to RGBA")			

	# Get numpy array
	npimg = np.array(img)

	# generate images from numpy array and save
	compute_layers(npimg, img.mode, f"image_rgb")  # rgb
	compute_layers(npimg[:, :, 0], 'L', f"image_r")  # r
	compute_layers(npimg[:, :, 1], 'L', f"image_g")  # g
	compute_layers(npimg[:, :, 2], 'L', f"image_b")  # b
	if img.mode == "RGBA":  # Should be RGB or RGBA
		compute_layers(npimg[:, :, 3], 'L', f"image_a")  # b

	print("[+] Bit layers saved in \\Views folder")


def LSB(path):
	print("Extracting bit layers, please wait...")
	extract_views(path)	
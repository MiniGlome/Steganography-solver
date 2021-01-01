import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS
from Exif import Exif
from LSB import LSB
from Thumbnail import Thumbnail


def run(path):
	print('''
Choose an option :

	[1] - Extract Exif
	[2] - Extract Bit layers
	[3] - Extract Thumbnail
		''')
	try : 
		option = int(input("Enter your value : "))
	except:
		print("ERROR, you must choose a number")
		exit()
	print("\n")
	if option == 1:
		Exif(path)
	elif option == 2:
		LSB(path)
	elif option == 3:
		Thumbnail(path)
	else:
		print("ERROR, the chosen option doesn't exist")


def show_usage():
	print(f"\nUsage : {sys.argv[0]} <file_name>")


if __name__ == '__main__':
	if len(sys.argv) != 2:
		show_usage()
	else:
		path = sys.argv[1]
		if os.path.isfile(path) :
			if path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', 'jfif')):
				run(path)
			else:
				print("File is not an image")
		else:
			print("File doesn't exist")
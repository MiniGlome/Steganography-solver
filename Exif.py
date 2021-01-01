from PIL import Image
from PIL.ExifTags import TAGS

def Exif(path):
	print("Extracting Exif...")
	image = Image.open(path)
	exif = {}
	try :
		for tag, value in image._getexif().items():
			if tag in TAGS:
				exif[TAGS[tag]] = value
	except:
		print("[-] No exif found.")

	else : 
		for k, v in exif.items():  # Print exif
			if isinstance(v, bytes):
				try:
					v = v.decode()     # Decode tag if tag is bytes
				except:
					v = "[-] Unable to decode tag"
			print(f'[+] {k} : {v}')

	if "GPSInfo" in exif:
		gps_coordinates = '{0} {1} {2:2f} {3}, {4} {5} {6:2f} {7}'.format(
			exif['GPSInfo'][2][0][0],
			exif['GPSInfo'][2][1][0],
			exif['GPSInfo'][2][2][0] / exif['GPSInfo'][2][2][1],
			exif['GPSInfo'][1],
			exif['GPSInfo'][4][0][0],
			exif['GPSInfo'][4][1][0],
			exif['GPSInfo'][4][2][0] / exif['GPSInfo'][4][2][1],
			exif['GPSInfo'][3]
			)
		print("\n---------------------------")
		print("[+] GPS coordinates found : "+gps_coordinates)
		print("[+] Link to the location : https://www.google.fr/maps/search/"+gps_coordinates.replace(" ", "%20"))
		print("---------------------------")
import sys
import os

def Thumbnail(file_path):
	print("Extracting Thumbnail...")
	# Create Thumbnails directory if don't exist
	if not os.path.exists("Thumbnails"):
	    os.mkdir("Thumbnails")

	startheader = "\xff\xd8"
	endheader = "\xff\xd9"	
	 
	with open(file_path, "rb") as img:
		data = img.read().decode("latin-1")

	nb_thumbnails = data.count(startheader)-1
	if nb_thumbnails < 1:
		print("[-] No Thumbnail found")
		nb_thumbnails = 0
	elif nb_thumbnails == 1:
		print("[+] 1 Thumbnail found")
	else:
		print(f"[+] {nb_thumbnails} Thumbnails found")

	for i in range(nb_thumbnails):
		data = data.replace(startheader, '', 1) # Remove the first image header
		data = data[:data.rfind(endheader)] + data[data.rfind(endheader)+len(endheader):]  # Remove the last image header

		start = data.find(startheader)
		end = data.rfind(endheader) + len(endheader)
		 
		img = data[start:end]
		outname = f"Thumbnails/thumbnail_{i+1}.jpg"
		with open(outname, "wb") as out:
		        out.write(img.encode("latin-1"))	 
		print("[+] Thumbnail saved as " + outname)

	_, file_extension = os.path.splitext(file_path)
	if file_extension not in ['.jpg', '.jpeg'] and nb_thumbnails > 0:
		print("[-] The file is not a JPG, the thumbnails found may be false positives")

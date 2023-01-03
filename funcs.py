from requests import post, get
from bs4 import BeautifulSoup as bs


def imgua(filename, efset=1):
	files = {"uploadfile":  (filename, open(f"original/{filename}", "rb"))}
	params = {"normset": 1, "briset": 0, "contrset": 0, "saturset": 0, "toneset": 0, "mpxlimit": 1, "outformat": 2, "jpegtype": 1, "jpegqual": 92}
	params["efset1"] = efset
	r = post("https://www.imgonline.com.ua/neural-effect-result.php", files=files, data=params)
	soup = bs(r.text, "html.parser")
	link = soup.find_all("a")[8]
	neuro_image_url = link.get("href")
	print(neuro_image_url)
	if not "https://" in neuro_image_url:
		neuro_image_url = "https://www.imgonline.com.ua/" + neuro_image_url
	
	#for index, link in enumerate(soup.find_all("a")):
#		print(index, link)
#		if "jpg" in link.get("href"):
#			neuro_image_url = link.get("href")
#			break
	neuro_image = get(neuro_image_url)
	with open(f"neuro/{filename}", "wb") as output:
		output.write(neuro_image.content)

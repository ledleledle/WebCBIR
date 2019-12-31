from libnya.colordescriptor import ColorDescriptor
from libnya.pencari import Searcher
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-g", "--gambar", required = True,
	help = "Pilih gambar yang ingin dicari")
args = vars(ap.parse_args())
 
cd = ColorDescriptor((8, 12, 3))
query = cv2.imread(args["gambar"])
features = cd.describe(query)
 
searcher = Searcher('index.csv')
results = searcher.search(features)
 
cv2.imshow("Gambar yang dicari", query)
 
for (score, resultID) in results:
	result = cv2.imread("static/coba/" + resultID)
	cv2.imwrite(resultID, result)
	#cv2.imshow("Hasil", result)
	print(resultID," ==> ",score)

	#cv2.waitKey(0)
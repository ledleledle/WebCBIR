from lib.colordescriptor import ColorDescriptor
import glob
import cv2
import csv
import os

cd = ColorDescriptor((8, 12, 3))
output = open("conf/index.csv", "w")

for imagePath in glob.glob("static/datasets/*"):
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    features = cd.describe(image)

    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))

output.close()

if os.path.exists('conf/conf.csv') == False:
    with open('conf/conf.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['tp', 'tn', 'fp', 'fn'])
        csvwriter.writerows([['1', '0', '0', '0']])
    print("Creating conf.csv")
else:
    print("conf.csv already initialized")

print("Job Done, Configuration initialized!")

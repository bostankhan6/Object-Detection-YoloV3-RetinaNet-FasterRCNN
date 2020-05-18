from bs4 import BeautifulSoup
from imutils import paths
import os

# initialize the base path for the logos dataset
BASE_PATH = "./"

annot_path = "SIMS_VOC_Annotations2/all_annotations/"

# build the path to the annotations and input images
train_images_path = "SIMS_Dataset/train_images/"
val_images_path = "SIMS_Dataset/validation_images/"
test_images_path = "SIMS_Dataset/test_images/"

#  build the path to the output training and test .csv files
train_csv = os.path.sep.join([BASE_PATH, 'train.csv'])
val_csv = os.path.sep.join([BASE_PATH, 'val.csv'])
test_csv = os.path.sep.join([BASE_PATH, 'test.csv'])

# build the path to the output classes CSV files
classes_csv = os.path.sep.join([BASE_PATH, 'classes.csv'])

# build the path to the output predictions dir
output_dir = os.path.sep.join([BASE_PATH, 'predictions'])

train_image_paths = list(paths.list_files(train_images_path))
val_image_paths = list(paths.list_files(val_images_path))
test_image_paths = list(paths.list_files(test_images_path))
# print(val_image_paths)

# create the list of datasets to build
dataset = [ ("train", train_image_paths, train_csv),
            ("val", val_image_paths, val_csv),
            ("test", test_image_paths, test_csv)]
# initialize the set of classes we have
CLASSES = set()

for (dType, imagePaths, outputCSV) in dataset:
    # load the contents
    print("[INFO] creating '{}' set...".format(dType))
    print("[INFO] {} total images in '{}' set".format(len(imagePaths), dType))

    # open the output CSV file
    csv = open(outputCSV, "w")

    # loop over the image paths
    for imagePath in imagePaths:
        # build the corresponding annotation path
        fname = imagePath.split(os.path.sep)[-1]
        fname = "{}.xml".format(fname[:fname.rfind(".")])
        annotPath = os.path.join(annot_path, os.path.basename(fname))

        # load the contents of the annotation file and buid the soup
        contents = open(annotPath).read()
        soup = BeautifulSoup(contents, "html.parser")

        # extract the image dimensions
        w = int(soup.find("width").string)
        h = int(soup.find("height").string)

        for o in soup.find_all("object"):
            #extract the label and bounding box coordinates
            label = o.find("name").string
            xMin = int(float(o.find("xmin").string))
            yMin = int(float(o.find("ymin").string))
            xMax = int(float(o.find("xmax").string))
            yMax = int(float(o.find("ymax").string))

            # truncate any bounding box coordinates that fall outside
            # the boundaries of the image
            xMin = max(0, xMin)
            yMin = max(0, yMin)
            xMax = min(w, xMax)
            yMax = min(h, yMax)

            # ignore the bounding boxes where the minimum values are larger
            # than the maximum values and vice-versa due to annotation errors
            if xMin >= xMax or yMin >= yMax:
                continue
            elif xMax <= xMin or yMax <= yMin:
                continue

            # write the image path, bb coordinates, label to the output CSV
            row = [os.path.abspath(imagePath),str(xMin), str(yMin), str(xMax),
                    str(yMax), str(label)]
            csv.write("{}\n".format(",".join(row)))

            # update the set of unique class labels
            CLASSES.add(label)

    # close the CSV file
    csv.close()

    print("[INFO] writing classes...")
    csv = open(classes_csv, "w")
    rows = [",".join([c, str(i)]) for (i, c) in enumerate(CLASSES)]
    csv.write("\n".join(rows))
    csv.close()
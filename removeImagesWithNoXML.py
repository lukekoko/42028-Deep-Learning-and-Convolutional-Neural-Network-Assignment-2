import os
from pathlib import Path

path = 'BloodRBC-Detection-Dataset-Processed'

images = []
xml = []

# iterate through images directory
for file in Path(path).iterdir():
    # get filename
    filename = file.stem
    # get extension of file
    ext = file.suffix
    if (ext == '.xml'): # if extension is xml add the filename to xml array
        xml.append(filename)
    if (ext == '.jpeg'): # if extension is jpeg add the filename and filepath to images array
        images.append([filename, file])

# iterate through each image in images array and search if it is in xml array. If it is not found in xml array delete.
for image in images:
    if (image[0] not in xml):
        print("Removing {}.jpeg because there is no corresponding {}.xml".format(image[0], image[0]))
        Path.unlink(image[1])

    
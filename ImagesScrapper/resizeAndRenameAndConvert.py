import os
import cv2

# Set the root directory of your dataset
root_dir = '/home/jakob/Documents/Projects/RGBD-Objects-Detection/ImagesScrapper/dataset/scraped+cifar100'
folder_new = '/home/jakob/Documents/Projects/RGBD-Objects-Detection/ImagesScrapper/dataset/scrappedAndCifar'

# Create the output directory if it does not exist
if not os.path.exists(folder_new):
    os.makedirs(folder_new)

# set output size
size = {"width": 32, "height": 32}

# Define function to downsize image
def resize_image(img, width=size["width"], height=size["height"]):
    img_resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    return img_resized

# list of image formats to convert to
output_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.webp']

# Iterate over each subdirectory
for subdir in os.listdir(root_dir):
    subdir_path = os.path.join(root_dir, subdir)
    
    # If the subdirectory is not a directory, skip it
    if not os.path.isdir(subdir_path):
        continue

    new_directory = os.path.join(folder_new, subdir)
    # Create the output directory if it does not exist
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    # RENAME & CONVERT
    # -----------------------------------------------------------------------------------

    # loop through all files in the input folder
    for i, filename in enumerate(os.listdir(subdir_path)):
        # check if the file is an image (i.e., has a valid file extension)
        if any(filename.lower().endswith(format) for format in output_formats):
            print(filename)

            # load the image file using OpenCV
            img = cv2.imread(os.path.join(subdir_path, filename))

            # resize image
            img = resize_image(img)

            # create a new filename for the output file with the correct extension
            new_filename = f"{subdir}_{i}" + ".png"
            # save the image in the output folder in the correct format using OpenCV
            path = os.path.join(folder_new, subdir, new_filename)
            cv2.imwrite(os.path.join(folder_new, subdir, new_filename), img)




import os
import cv2

# specify the path to the input folder
input_folder = "/home/jakob/Documents/Projects/RGBD-Objects-Detection/ImagesScrapper/dataset/full_images/other"

# specify the path to the output folder
output_folder = "/home/jakob/Documents/Projects/RGBD-Objects-Detection/ImagesScrapper/dataset/full_images/other_png"

# list of image formats to convert to
output_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.webp']

# loop through all files in the input folder
for filename in os.listdir(input_folder):
    # check if the file is an image (i.e., has a valid file extension)
    if any(filename.lower().endswith(format) for format in output_formats):
        print(filename)
        # load the image file using OpenCV
        img = cv2.imread(os.path.join(input_folder, filename))
        # create a new filename for the output file with the correct extension
        new_filename = os.path.splitext(filename)[0] + ".png"
        # save the image in the output folder in the correct format using OpenCV
        cv2.imwrite(os.path.join(output_folder, new_filename), img)

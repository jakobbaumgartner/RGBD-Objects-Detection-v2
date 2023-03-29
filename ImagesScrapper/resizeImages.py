import cv2
import os

# Define function to downsize image
def resize_image(img_path, width=200, height=200):
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    return img_resized

# Set folder path containing images to downsize
folder_path = "/home/jakob/Documents/Projects/RGBD-Objects-Detection/Images_ImageNet_and_Scrapper/wallet"
folder_new = '/home/jakob/Documents/Projects/RGBD-Objects-Detection/Images_ImageNet_and_Scrapper_Resized/wallet'

# Get list of all image files in folder
img_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(('.jpg', '.jpeg', '.png', '.JPEG'))]

# Iterate over image files and downsize each one
for img_file in img_files:
    img_path = os.path.join(folder_path, img_file)
    img_resized = resize_image(img_path)
    
    # Save downsized image with new filename
    new_filename = f"{os.path.splitext(img_file)[0]}_resized_{img_resized.shape[1]}x{img_resized.shape[0]}.png"
    cv2.imwrite(os.path.join(folder_new, new_filename), img_resized)

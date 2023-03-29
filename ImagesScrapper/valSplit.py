import os
import random
import shutil

# Set the root directory of your dataset
root_dir = '/home/jakob/Documents/Projects/RGBD-Objects-Detection/Images_ImageNet_and_Scrapper_Resized'
sorted_dir = '/home/jakob/Documents/Projects/RGBD-Objects-Detection/Images_ImageNet_and_Scrapper_Resized_Split'

# Set the directory names for the training, validation, and testing subsets
train_dir = os.path.join(sorted_dir, 'train')
val_dir = os.path.join(sorted_dir, 'val')
test_dir = os.path.join(sorted_dir, 'test')

# Create the validation and testing directories
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Set the percentage of images to use for validation and testing
val_percent = 0.15
test_percent = 0.1

# Iterate over each subdirectory in the root directory
for subdir in os.listdir(root_dir):
    subdir_path = os.path.join(root_dir, subdir)
    
    # If the subdirectory is not a directory, skip it
    if not os.path.isdir(subdir_path):
        continue
    
    # Create the subdirectories in the training, validation, and testing directories
    os.makedirs(os.path.join(train_dir, subdir), exist_ok=True)
    os.makedirs(os.path.join(val_dir, subdir), exist_ok=True)
    os.makedirs(os.path.join(test_dir, subdir), exist_ok=True)
    
    # Get the list of image filenames in the subdirectory
    filenames = os.listdir(subdir_path)
    random.shuffle(filenames)
    
    # Split the images into training, validation, and testing sets
    val_size = int(len(filenames) * val_percent)
    test_size = int(len(filenames) * test_percent)
    train_size = len(filenames) - val_size - test_size
    
    train_filenames = filenames[:train_size]
    val_filenames = filenames[train_size:train_size+val_size]
    test_filenames = filenames[train_size+val_size:]
    
    # Move the training images to the training directory
    for filename in train_filenames:
        src = os.path.join(subdir_path, filename)
        dst = os.path.join(train_dir, subdir, filename)
        shutil.copyfile(src, dst)
        
    # Move the validation images to the validation directory
    for filename in val_filenames:
        src = os.path.join(subdir_path, filename)
        dst = os.path.join(val_dir, subdir, filename)
        shutil.copyfile(src, dst)
        
    # Move the testing images to the testing directory
    for filename in test_filenames:
        src = os.path.join(subdir_path, filename)
        dst = os.path.join(test_dir, subdir, filename)
        shutil.copyfile(src, dst)

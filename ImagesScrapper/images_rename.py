import os

# Set the root directory of your dataset
root_dir = '/home/jakob/Documents/Projects/RGBD-Objects-Detection/ImagesScrapper/dataset/small_images'

# Iterate over each subdirectory
for subdir in os.listdir(root_dir):
    subdir_path = os.path.join(root_dir, subdir)
    
    # If the subdirectory is not a directory, skip it
    if not os.path.isdir(subdir_path):
        continue
    
    # Iterate over each file in the subdirectory
    for i, file in enumerate(os.listdir(subdir_path)):
        file_path = os.path.join(subdir_path, file)
        
        # Get the new name for the file
        new_name = f"{subdir}_{i}.png"  # Modify this line to fit your desired file format
        
        # Rename the file
        os.rename(file_path, os.path.join(subdir_path, new_name))

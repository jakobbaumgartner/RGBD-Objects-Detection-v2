import random
import pyrealsense2 as rs
import numpy as np
import cv2

picked_folder = 'class_test'

# Create a RealSense pipeline object
pipeline = rs.pipeline()

# Create a configuration object
config = rs.config()

# Enable the depth and color streams
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)

# Start the pipeline
pipeline.start(config)

# Create an align object

# Concept of spatial stream alignment.

# The need for spatial alignment (from here "align") arises from the fact
# that not all camera streams are captured from a single viewport.

# Align process lets the user translate images from one viewport to another.
# That said, results of align are synthetic streams, and suffer from several artifacts:

    # 1. Sampling - mapping stream to a different viewport will modify the resolution of the 
    # frame to match the resolution of target viewport. This will either cause 
    # downsampling or upsampling via interpolation. The interpolation used needs to be of 
    # type Nearest Neighbor to avoid introducing non-existing values.

    # 2. Occlussion - Some pixels in the resulting image correspond to 3D coordinates that 
    # the original sensor did not see, because these 3D points were occluded in the 
    # original viewport. Such pixels may hold invalid texture values.

align = rs.align(rs.stream.color)

try:
    while True:
        # Wait for the next frameset
        frames = pipeline.wait_for_frames()

        # Align the depth and color frames
        aligned_frames = align.process(frames)

        # Get the aligned depth and color frames
        aligned_depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()

        # Convert the frames to numpy arrays
        depth_image = np.asanyarray(aligned_depth_frame.get_data())

        # Apply the depth threshold
        depth_image[depth_image < 0] = 0
        depth_image[depth_image > 2000] = 0
        
        color_image = np.asanyarray(color_frame.get_data())

        
        # Apply color mapping to the depth image (for visualization)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Display the images
        cv2.imshow('Color Image', color_image)
        cv2.imshow('Depth Image', depth_colormap)

        # Wait for a key press
        key = cv2.waitKey(1)
        
        # Check if the user pressed the "q" key to quit
        if key == ord('q'):
            break

        # Check if user pressed "s" to save image 
        if key == ord('s'):
            # Generate a random file name for the images
            random_name = f"{random.randint(1,1000000)}"

            # Save the depth and color images as PNG files with the random name
            depth_file_name = f"{picked_folder}/depth_{random_name}.png"
            cv2.imwrite(depth_file_name, depth_image)

            color_file_name = f"{picked_folder}/color_{random_name}.png"
            cv2.imwrite(color_file_name, color_image)

            print(f"Saved depth image as {depth_file_name}")
            print(f"Saved color image as {color_file_name}")



finally:
    # Stop the pipeline
    pipeline.stop()

    # Close all windows
    cv2.destroyAllWindows()

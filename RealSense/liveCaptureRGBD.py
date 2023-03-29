import pyrealsense2 as rs
import numpy as np
import cv2
import random

# Create a RealSense pipeline object
pipeline = rs.pipeline()

# Create a configuration object for the pipeline
config = rs.config()

# Enable the depth and color streams
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)

# Start the pipeline
pipeline.start(config)

# Loop over the frames
while True:
    # Wait for the next frame
    frames = pipeline.wait_for_frames()

    # Get the depth and color frames
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    # Convert the depth frame to a numpy array
    depth_image = np.asanyarray(depth_frame.get_data())

    # Convert the color frame to a numpy array
    color_image = np.asanyarray(color_frame.get_data())

    # Apply colormap to the depth image for better visualization
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

    # Display the depth and color images in two separate windows
    cv2.imshow("Depth Stream", depth_colormap)
    cv2.imshow("RGB Stream", color_image)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Check if the user pressed the "q" key to quit
    if key == ord('q'):
        break

    # Check if user pressed "s" to save image 
    key = cv2.waitKey(1)
    if key == ord('s'):
        # Generate a random file name for the images
        random_name = f"{random.randint(1,1000000)}"

        # Save the depth and color images as PNG files with the random name
        depth_file_name = f"depth_{random_name}.png"
        cv2.imwrite(depth_file_name, depth_image)

        color_file_name = f"color_{random_name}.png"
        cv2.imwrite(color_file_name, color_image)

        print(f"Saved depth image as {depth_file_name}")
        print(f"Saved color image as {color_file_name}")

# Stop the pipeline
pipeline.stop()

# Close all windows
cv2.destroyAllWindows()

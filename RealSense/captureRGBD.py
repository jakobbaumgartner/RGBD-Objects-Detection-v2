import pyrealsense2 as rs
import numpy as np
import cv2

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
for i in range(6):
    # Wait for the next frame
    frames = pipeline.wait_for_frames()

    # Get the depth and color frames
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    if i == 5:
        # Convert the depth and color frames to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Save the depth and color images as PNG files
        cv2.imwrite("depth_image.png", depth_image)
        cv2.imwrite("color_image.png", color_image)

# Stop the pipeline
pipeline.stop()

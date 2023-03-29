import os
import pyrealsense2 as rs
import numpy as np
import cv2

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
align = rs.align(rs.stream.color)

# Create a new directory to save images
dirName = str(input("Enter video name:  "))

os.makedirs(dirName, exist_ok=True)

# Set the length of video capture in seconds (default is 5 seconds)
capture_length = int(input("Enter length of video capture in seconds (default is 5): ") or "5")

try:
    # Calculate the number of frames to capture based on the capture length and FPS
    num_frames = capture_length * 15

    for i in range(num_frames):
        # Wait for the next frameset
        frames = pipeline.wait_for_frames()

        # Align the depth and color frames
        aligned_frames = align.process(frames)

        # Get the aligned depth and color frames
        aligned_depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()

        # Convert the frames to numpy arrays
        depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Save the color image to disk
        cv2.imwrite(dirName+f"/color_{frames.frame_number}.png", color_image)

        # Save the depth image to disk
        cv2.imwrite(dirName+f"/depth_{frames.frame_number}.png", depth_image)
except KeyboardInterrupt:
    pass

pipeline.stop()
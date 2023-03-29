import pyrealsense2 as rs
import numpy as np
import cv2

# Create a RealSense pipeline object
pipeline = rs.pipeline()

# Create a configuration object for the pipeline
config = rs.config()

# Enable the depth stream
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)

# Start the pipeline
pipeline.start(config)

# Loop over some frames, because the first few frames are usually bad
i = 0

while i < 50:
    # Wait for the next frame
    frames = pipeline.wait_for_frames()

    # Get the depth frame
    depth_frame = frames.get_depth_frame()

    # Convert the depth frame to a numpy array
    depth_image = np.asanyarray(depth_frame.get_data())

    # Save the depth image as PNG file
    cv2.imwrite("depth_image.png", depth_image)

    i += 1

# Stop the pipeline
pipeline.stop()



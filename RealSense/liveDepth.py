import pyrealsense2 as rs
import numpy as np
import cv2

# Create a RealSense pipeline object
pipeline = rs.pipeline()

# Create a configuration object for the pipeline
config = rs.config()

# Enable the depth stream
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start the pipeline
pipeline.start(config)

# Create a window for the depth stream
cv2.namedWindow("Depth Stream", cv2.WINDOW_NORMAL)

# Loop over the frames
while True:
    # Wait for the next frame
    frames = pipeline.wait_for_frames()

    # Get the depth frame
    depth_frame = frames.get_depth_frame()

    # Convert the depth frame to a numpy array
    depth_image = np.asanyarray(depth_frame.get_data())

    # Normalize the depth image for display
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

    # Display the depth image
    cv2.imshow("Depth Stream", depth_colormap)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Check if the user pressed the "q" key to quit
    if key == ord('q'):
        break

# Stop the pipeline
pipeline.stop()

# Close all windows
cv2.destroyAllWindows()

"""
Script that records video from a camera and then converts and stores it as a depth video.
"""
from depth_estimation import MonoDepthEstimator
import cv2

depth_estimator = MonoDepthEstimator()

frame_list = []

while True:
    ret, frame = depth_estimator.video_capture.read()
    frame = cv2.resize(frame, (640, 480))

    if not ret:
        print("Camera not available")
        break

    frame_list.append(frame)
    cv2.imshow('Captured', frame)
    # Stop loop if "s" is pressed
    if cv2.waitKey(1) == ord("e"):
        break

cv2.destroyAllWindows()
depth_estimator.close_video_cap()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('depth_video.avi', fourcc, 24, (640, 480))

for frame in frame_list:
    depth = depth_estimator.find_frame_depth(frame)
    depth_colormap = cv2.applyColorMap(depth, cv2.COLORMAP_JET)
    out.write(depth_colormap)

out.release()

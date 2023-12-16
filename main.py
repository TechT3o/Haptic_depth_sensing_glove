"""
Main script reads a frame from the glove's camera, estimates the relative mono depth
maps the depth to the intensity that each motor should receive based on the motor coordinates and
transmits these intensities serially to the microcontroller. It also receives a feedback message
to debug serial connection.
Motor coordinates is a list of tuples that has the (y,x) positions of the motors in a coordinate system
Window size is the window over which depth values are averaged
Com port is the com port where the microcontroller is connected
"""

import cv2
from depth_estimation import MonoDepthEstimator
from serial_com import SerialCom
from intensity_mapper import IntensityMapper
import time

MOTOR_COORDINATES = [(180, 5), (180, 35), (180, 55),
                     (140, 5), (140, 55),
                     (110, 5), (110, 35), (110, 55),
                     (60, 5), (50, 25), (30, 35), (50, 55), (100, 80)]
WINDOW_SIZE = 10
COM_PORT = "COM9"

# Initialize objects
serial = SerialCom(COM_PORT)
depth_estimator = MonoDepthEstimator()
int_mapper = IntensityMapper(MOTOR_COORDINATES, WINDOW_SIZE)


# Main loop
while 1:
    start_time = time.time()
    ret, frame = depth_estimator.grab_frame()
    if not ret:
        serial.close_com()
        depth_estimator.close_video_cap()
        break
    depth_image = depth_estimator.find_frame_depth(frame)
    intensities = int_mapper.find_intensities(depth_image)
    serial.send_intensities(intensities)
    # prints frames per second
    print(1/(time.time()-start_time))
    cv2.imshow("Live cam", int_mapper.draw_points_with_boxes(frame))
    # Press e to exit
    if cv2.waitKey(1) == ord("e"):
        serial.close_com()
        depth_estimator.close_video_cap()
        break
    serial.get_feedback()
print("Finished running")

"""
This script reads a depth video and assigns the values to the motors of the glove
"""

import cv2
from serial_com import SerialCom
from intensity_mapper import IntensityMapper

MOTOR_COORDINATES = [(180, 5), (180, 35), (180, 55),
                     (140, 5), (140, 55),
                     (110, 5), (110, 35), (110, 55),
                     (60, 5), (50, 15), (30, 35), (50, 55), (100, 90)]
WINDOW_SIZE = 5


serial = SerialCom()
# depth_estimator = MonoDepthEstimator()
int_mapper = IntensityMapper(MOTOR_COORDINATES, WINDOW_SIZE)


depth_vid = cv2.VideoCapture("depth_video.avi")

while depth_vid.isOpened():
    ret, depth_image = depth_vid.read()
    if ret:
        intensities = int_mapper.find_intensities(depth_image)
        serial.send_intensities(intensities)
    else:
        depth_vid.release()
        serial.close_com()
    serial.get_feedback()

from depth_estimation import MonoDepthEstimator
from serial_com import SerialCom
from intensity_mapper import IntensityMapper
import numpy as np

MOTOR_COORDINATES = [(180, 10), (180, 30), (180, 60), (120, 10), (120, 30),
                     (120, 60), (100, 90), (60, 10), (40, 20), (40, 60)]
WINDOW_SIZE = 10


serial = SerialCom()
# depth_estimator = MonoDepthEstimator()
int_mapper = IntensityMapper(MOTOR_COORDINATES, WINDOW_SIZE)

depth_image = np.load("depth.npy")

# image = serial.receive_img()
# depth_image = depth_estimator.find_frame_depth()

intensities = int_mapper.find_intensities(depth_image)
serial.send_intensities(intensities)
while 1:
    serial.get_feedback()
serial.close_com()



import numpy as np


class IntensityMapper:
    def __init__(self, motor_coordinates: list = None, window_size: int = 5):

        if motor_coordinates is None:
            self.motor_coordinates = []
        else:
            self.motor_coordinates = motor_coordinates

        self.window_size = window_size

    def find_intensities(self, depth_map: np.ndarray) -> str:
        """
        Uses the motor position and window information to find what PWM intensity each of the motors should have
        :param depth_map: numpy array of the depth map of the  current frame
        :return: comma separated string that has the PWM intensities for each motor
        """

        motor_intensities = []
        max_x, max_y = max([motor_coordinate[1] for motor_coordinate in self.motor_coordinates]),\
                       max([motor_coordinate[0] for motor_coordinate in self.motor_coordinates])
        x_scale = depth_map.shape[1] / max_x
        y_scale = depth_map.shape[0] / max_y

        # Map motor coordinates to depth pixels and find average value based on window size
        for y, x in self.motor_coordinates:
            depth_x = int(x * x_scale)
            depth_y = int(y * y_scale)

            lower_x = max(0, depth_x-self.window_size)
            upper_x = min(depth_x+self.window_size, depth_map.shape[1])

            lower_y = max(0, depth_y-self.window_size)
            upper_y = min(depth_y+self.window_size, depth_map.shape[0])

            motor_value = int(np.mean(depth_map[lower_y: upper_y, lower_x: upper_x]))

            motor_intensities.append(motor_value)

        # Concatenate in a comma separated string to be able to transmit to microcontroller
        motor_intensities = ",".join(map(str, motor_intensities))
        return motor_intensities

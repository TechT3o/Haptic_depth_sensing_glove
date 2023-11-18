import numpy as np
import cv2


class IntensityMapper:
    def __init__(self, motor_coordinates: list = None, window_size: int = 5):

        if motor_coordinates is None:
            self.motor_coordinates = []
        else:
            self.motor_coordinates = motor_coordinates

        self.window_size = window_size
        self.threshold_intensity = 0
        self.max_intensity = 255
        self.optical_center = 0
        self.motor_intensities_list = []
        self.depth_coordinates = []
        # self.max_x, self.max_y = max([motor_coordinate[1] for motor_coordinate in self.motor_coordinates]), \
        #                max([motor_coordinate[0] for motor_coordinate in self.motor_coordinates])
        self.max_x, self.max_y = 110, 190

    def normalize_intensity(self, intensity: int) -> int:
        """
        Normalizes the intensity to be within threshold intensity and max intensity
        :param intensity: calculated motor intensity
        :return: normalized motor intensity integer
        """
        return int(intensity/self.max_intensity*(self.max_intensity-self.threshold_intensity)+self.threshold_intensity)

    def find_intensities(self, depth_map: np.ndarray) -> str:
        """
        Uses the motor position and window information to find what PWM intensity each of the motors should have
        :param depth_map: numpy array of the depth map of the  current frame
        :return: comma separated string that has the PWM intensities for each motor
        """

        x_scale = depth_map.shape[1] / self.max_x
        y_scale = depth_map.shape[0] / self.max_y

        self.depth_coordinates = []
        self.motor_intensities_list = []

        # Map motor coordinates to depth pixels and find average value based on window size
        for y, x in self.motor_coordinates:
            depth_x = int(x * x_scale)
            depth_y = int(y * y_scale)
            self.depth_coordinates += [(depth_x, depth_y)]
            lower_x = max(0, depth_x-self.window_size)
            upper_x = min(depth_x+self.window_size, depth_map.shape[1])

            lower_y = max(0, depth_y-self.window_size)
            upper_y = min(depth_y+self.window_size, depth_map.shape[0])

            motor_value = int(np.mean(depth_map[lower_y: upper_y, lower_x: upper_x]))

            self.motor_intensities_list.append(self.normalize_intensity(motor_value))

        return self.motor_intensities

    def draw_points_with_boxes(self, image: np.ndarray) -> np.ndarray:
        """
        Draw the points, motor index and windows on the input image to visualize which area each motor covers
        :param image: Image to annotate
        :return: annotated image
        """

        annotated_img = image.copy()

        for i, (x, y) in enumerate(self.depth_coordinates):

            # Draws point
            cv2.circle(annotated_img, (int(x), int(y)), 5, (0, 255, 0), -1)
            # Draws motor index
            cv2.putText(annotated_img, str(i), (int(x) + 10, int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                        2)

            # Draws window
            half_width = int(self.window_size / 2)
            cv2.rectangle(annotated_img, (int(x) - half_width, int(y) - half_width),
                          (int(x) + half_width, int(y) + half_width), (0, 255, 0), 2)
        return annotated_img

    @property
    def motor_intensities(self):
        # Concatenate in a comma separated string to be able to transmit to microcontroller
        return ",".join(map(str, self.motor_intensities_list))


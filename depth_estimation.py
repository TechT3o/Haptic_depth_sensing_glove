from transformers import DPTImageProcessor, DPTForDepthEstimation
import torch
import cv2
import numpy as np
from typing import Tuple


class MonoDepthEstimator:
    def __init__(self):
        self.processor = DPTImageProcessor.from_pretrained("Intel/dpt-large", low_cpu_mem_usage=True)
        self.model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")
        print(torch.cuda.is_available())
        self.computing_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.computing_device)
        self.video_capture = cv2.VideoCapture(0)

    def find_frame_depth(self, frame: np.ndarray) -> np.ndarray:
        """
        Uses Intel DPT model to estimate the mono depth from a single frame
        :param frame: Input RGB frame HxWx3
        :return: Numpy array of the frame's depth map HxWx1
        """

        # preprocess frame and send to gpu for faster calculation
        inputs = self.processor(images=frame, return_tensors="pt").to(self.computing_device)

        # predict depth and process model's output
        with torch.no_grad():
            outputs = self.model(**inputs)
            predicted_depth = outputs.predicted_depth

        # interpolate to original size
        prediction = torch.nn.functional.interpolate(
            predicted_depth.unsqueeze(1),
            size=frame.shape[:2],
            mode="bicubic",
            align_corners=False,
        )

        output = prediction.squeeze().cpu().numpy()
        depth = (output * 255 / np.max(output)).astype("uint8")

        return depth

    def capture_live_depth(self, save_np: bool = False) -> None:
        """
        Find and show depth frames captured by primary input camera
        :param save_np: if True saves a numpy frame on every loop
        :return: None
        """

        # video_capture = cv2.VideoCapture(0)
        print("Starting live capture. Press s to stop")
        while True:
            ret, frame = self.video_capture.read()
            frame = cv2.resize(frame, (640, 480))

            if not ret:
                print("Camera not available")
                break

            depth = self.find_frame_depth(frame)

            if save_np:
                np.save("depth.npy", depth)

            cv2.imshow('depth', depth)

            # Stop loop if "s" is pressed
            if cv2.waitKey(1) == ord("s"):
                break

        self.close_video_cap()
        print("Stopped live capture.")

    def grab_frame(self) -> Tuple[bool, np.ndarray]:
        """
        Grabs current frame from video capture device
        :return: ret: bool value if frame is valid, frame: numpy array image captured
        """
        return self.video_capture.read()

    def close_video_cap(self) -> None:
        """
        Closes video capture object
        :return: None
        """
        if self.video_capture.isOpened():
            self.video_capture.release()


if __name__ == "__main__":
    # Tests capturing live depth
    depth_est = MonoDepthEstimator()
    depth_est.capture_live_depth(True)

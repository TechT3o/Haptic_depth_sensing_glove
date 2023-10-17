from transformers import DPTImageProcessor, DPTForDepthEstimation, GLPNFeatureExtractor, GLPNForDepthEstimation
import torch
import cv2
import numpy as np


class MonoDepthEstimator:
    def __init__(self):
        self.processor = DPTImageProcessor.from_pretrained("Intel/dpt-hybrid-midas", low_cpu_mem_usage=True)
        self.model = DPTForDepthEstimation.from_pretrained("Intel/dpt-hybrid-midas")
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

        video_capture = cv2.VideoCapture(0)
        print("Starting live capture. Press s to stop")
        while True:
            ret, frame = video_capture.read()

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

        video_capture.release()
        print("Stopped live capture.")


if __name__ == "__main__":
    depth_est = MonoDepthEstimator()
    depth_est.capture_live_depth(True)

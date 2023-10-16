from transformers import DPTImageProcessor, DPTForDepthEstimation, GLPNFeatureExtractor, GLPNForDepthEstimation
import torch
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

print(torch.cuda.is_available())
# processor = GLPNFeatureExtractor.from_pretrained("vinvino02/glpn-kitti")
# model = GLPNForDepthEstimation.from_pretrained("vinvino02/glpn-kitti")

processor = DPTImageProcessor.from_pretrained("Intel/dpt-hybrid-midas", low_cpu_mem_usage=True)
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-hybrid-midas")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


cap = cv2.VideoCapture(0)
# prepare image for the model

while True:
    ret, frame = cap.read()
    inputs = processor(images=frame, return_tensors="pt").to(device)

    # cv2.imshow('pic', frame)
    # cv2.waitKey(0)

    with torch.no_grad():
        outputs = model(**inputs)
        predicted_depth = outputs.predicted_depth

    # interpolate to original size
    prediction = torch.nn.functional.interpolate(
        predicted_depth.unsqueeze(1),
        size=frame.shape[:2],
        mode="bicubic",
        align_corners=False,
    )

    # visualize the prediction
    output = prediction.squeeze().cpu().numpy()
    formatted = (output * 255 / np.max(output)).astype("uint8")
    #depth = Image.fromarray(formatted)

    # Plot the image and the semantic map tensor.
    # point_cloud = cv2.reprojectImageTo3D(depth_map, Q)
    cv2.imshow('depth', formatted)
    cv2.waitKey(1)
    np.save("depth.npy", formatted)

# if __name__ == "__main__":
#     print(torch.cuda.is_available())
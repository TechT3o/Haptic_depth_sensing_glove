import cv2
import numpy as np
import open3d as o3d

depth_map = np.load("depth.npy")


# Camera intrinsics (example values, replace with your own)
camera_mat = np.load("calib_cam_mat.npy")
fx = camera_mat[0][0]  # Focal length in pixels (x-axis)
fy = camera_mat[1][1]  # Focal length in pixels (y-axis)
cx = camera_mat[0][2]
cy = camera_mat[1][2]

# Create a grid of (x, y) coordinates
rows, cols = depth_map.shape
x, y = np.meshgrid(np.arange(cols), np.arange(rows))

# Calculate 3D coordinates using depth and camera parameters
X = (x - cx) * depth_map / fx
Y = (y - cy) * depth_map / fy
Z = depth_map

# Stack the (X, Y, Z) coordinates into a (N, 3) array
point_cloud = np.dstack((X, Y, Z)).reshape(-1, 3)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud)
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
# rotation = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
# pcd.transform(rotation)
o3d.visualization.draw_geometries([downpcd])

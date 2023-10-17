import cv2
import numpy as np
import open3d as o3d
from depth_estimation import MonoDepthEstimator


class Reconstruct3D:
    def __init__(self):
        self.depth_estimator = MonoDepthEstimator()
        self.load_camera_parameters()
        # depth_map = np.load("depth.npy")

    def load_camera_parameters(self):
        """
        Loads camera intrinsic parameters obtained form calibration script
        :return:
        """

        camera_mat = np.load("calib_cam_mat.npy")
        self.fx = camera_mat[0][0]  # Focal length in pixels (x-axis)
        self.fy = camera_mat[1][1]  # Focal length in pixels (y-axis)
        self.cx = camera_mat[0][2]
        self.cy = camera_mat[1][2]

    def create_point_cloud(self, depth_map: np.ndarray) -> o3d.geometry.PointCloud:
        """
        Creates point cloud from depth map
        :param depth_map: Input depth map
        :return: returns an open3d point cloud object
        """

        # Create a grid of (x, y) coordinates
        rows, cols = depth_map.shape
        x, y = np.meshgrid(np.arange(cols), np.arange(rows))

        # Calculate 3D coordinates using depth and camera parameters
        X = (x - self.cx) * depth_map / self.fx
        Y = (y - self.cy) * depth_map / self.fy
        Z = depth_map

        # Stack the (X, Y, Z) coordinates into a (N, 3) array
        point_cloud = np.dstack((X, Y, Z)).reshape(-1, 3)

        # Create and downsample point cloud
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(point_cloud)
        down_pcd = pcd.voxel_down_sample(voxel_size=0.05)
        # o3d.visualization.draw_geometries([downpcd])
        return down_pcd

    def live_point_cloud(self) -> None:
        """
        Record live frames form camera and display the point clouds
        :return: None
        """
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            depth_map = self.depth_estimator.find_frame_depth(frame)

            point_cloud = self.create_point_cloud(depth_map)

            o3d.visualization.draw_geometries([point_cloud])


if __name__ == "__main__":
    reconstructor = Reconstruct3D()
    reconstructor.live_point_cloud()

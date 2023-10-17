"""
Script that is used for camera calibration in order to find the camera intrinsic parameters.
You need to print a charuco board pattern before using this.
If you have already captured images with the charuco board set Use images to True and the images directory
Also depending on your charuco bard set the pattern (columnsxrows) of blocks
If you capture live video press a to accept a frame and e when you are ready to exit and get the parameters
It is recommended taht at least 10 images are captured with different orientations of the charuco board.
"""

import cv2
import numpy as np
import cv2 as cv
import os

# Variables
USE_IMAGES = False
CAMERA_PICS_DIR = "checkboard_pics"
CHECKBOARD_PATTERN = (8, 6)


# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((CHECKBOARD_PATTERN[1]*CHECKBOARD_PATTERN[0], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKBOARD_PATTERN[0], 0:CHECKBOARD_PATTERN[1]].T.reshape(-1, 2) * 30  # scale to by 30 mm
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

if USE_IMAGES:
    for img_name in os.listdir(CAMERA_PICS_DIR):
        img = cv.imread(os.path.join(CAMERA_PICS_DIR, img_name))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (CHECKBOARD_PATTERN[0], CHECKBOARD_PATTERN[1]), None)
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
            # Draw and display the corners
            cv.drawChessboardCorners(img, (CHECKBOARD_PATTERN[0], CHECKBOARD_PATTERN[1]), corners2, ret)
            cv.imshow('img', img)
            cv.waitKey(500)
    cv.destroyAllWindows()
else:
    cap = cv2.VideoCapture(0)
    number_of_frames = 0
    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Find the chess board corners
        found_chessboard, corners = cv.findChessboardCorners(gray, (CHECKBOARD_PATTERN[0], CHECKBOARD_PATTERN[1]), None)
        # If found, add object points, image points (after refining them)
        if found_chessboard:
            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            # Draw and display the corners
            cv.drawChessboardCorners(frame, (CHECKBOARD_PATTERN[0], CHECKBOARD_PATTERN[1]), corners2, ret)
        cv.imshow('img', frame)
        key = cv.waitKey(2000)
        if key == ord("e"):
            break
        if found_chessboard and (key == ord("a")):
            objpoints.append(objp)
            imgpoints.append(corners2)
            number_of_frames += 1
            print(number_of_frames)

cv.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

np.save('calib_cam_mat.npy', mtx)
np.save('calib_dist_mat.npy', dist)
np.save('calib_rvecs_mat.npy', rvecs)
np.save('calib_tvecs_mat.npy', tvecs)

mean_error = 0
for i in range(len(objpoints)):
 imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
 error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
 mean_error += error
print("total error: {}".format(mean_error/len(objpoints)) )
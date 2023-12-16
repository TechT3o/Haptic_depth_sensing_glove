# Haptic_depth_sensing_glove

Haptic feedback glove device that uses a motor camera and mini motor disks to help visually impaired people understand the 3d space around them.

The idea is to mount a small camera on the palm of the visually impaired user, construct the depth map, and perform sensory substitution of vision by using a high-resolution haptic feedback glove comprised of an array of vibrational mini DC motor disks to assign a different intensity in the direction where the user's hand is pointing at, analogous to how close the object is.

The goal is for the user to be able to identify what type of object their hand is pointing at for object recognition and object fetching and for the user to be able to do wayfinding and navigate in a room using the device.

User studies that examine the usability (Learnability, Efficiency, Memorability, Errors, Satisfaction) and effectiveness of the device will be done.

# Hardware

- 1x [ESP32](https://www.espressif.com/en/products/socs/esp32)
- 1x [OV5640 camera module](https://www.amazon.com/Cameras-2592X1944-Industrial-Windows-Raspberry/dp/B088RD74VC?th=1)
- 20x [Mini motor disk](https://www.adafruit.com/product/1201#technical-details)
- 20x [p2n222A npn transistor](https://www.onsemi.com/pdf/datasheet/p2n2222a-d.pdf)
- 20x 30 Ohms resistor
- 20x 2.2k Ohms resistor
- 20x 33 pF capacitor
- 20x 1N4001 diode
- 20x [motor circuit PCB](https://github.com/TechT3o/Haptic_depth_sensing_glove/tree/main/PCB%20files)

## Motor driver circuit

The mini disk motors require around 100 mA of current in order to rotate at full speed with 5V power. The Arduino output pins can provide up to 10 mA, therefore we need a driver circuit to be able to power the motor using a PWM signal. The circuit shown in Figure 1 was built. It uses an NPN transistor whose base is connected to the GPIO output pin of the Arduino. When the PWM signal gets applied to the base of the transistor the Collector Emitter channel opens and current from the VCC flows through the disk motor and makes it spin with intensity analogous to the PWM signal. The resistor R2 limits the current flowing through the disk motor. A value of 30 Ohms was selected as 5V/30 = 166 mA max current that could flow through R2 ignoring rest of the circuit resistances. R1 was selected to limit the base current. As the base current is very small values of up to 5k could be selected but the chosen value for R1 in this project was 2.2k Ohms. The capacitor is used to soften voltage spikes from the power supply and suppress electrical noise from the motor's rotation and a diode is put to protect against back EMF.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/c52ca1bd-b7f3-442d-acfb-adf6d63f25e5" alt="drawing" width="200" align="center"/>

*Figure 1: Motor driver circuit*

The PCB of this circuit shown in Figure 2 was made and the Gerber files were sent to [OSHPARK](https://oshpark.com/) for manufacturing.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/0849f1bc-9bf5-438c-accb-9387e1dbf27c" alt="drawing" width="200" align="center"/>

*Figure 2: Motor driver PCB*

The received PCBs arrived and the components were soldered on top of it with the disk motors attached to the back of the PCB.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/5368494d-5bee-4cc1-82d2-87d380974121" alt="drawing" width="200" align="center"/>

*Figure 3: PCB*

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/4977230c-6801-469e-8884-8b859b470c98" alt="drawing" width="200" align="center"/>

*Figure 4: Soldered circuits and motor coordinates*

## Camera

When choosing the camera we wanted a camera with a small size that could fit the device, as little distortion as possible (no wide angle cameras that tend to have a lot of barrel distortion), low latency and good enough resolution for the depth estimation model to give accurate results. The camera selected was a 5MP USB Camera Webcam with 60 Degree FOV and Autofocus Lens by IFWATER.

It used the OV5640 CMOS (Complementary Metal-Oxide-Semiconductor) image sensor which has high resolution of 2592 x 1944 pixels and can achieve frame rates of 30 FPS.

The location of the camera was another dilemma in our design consideration. As originally intended, it was supposed to be connected to the user's body. However, by relocating the camera to the palm, we eliminated the need to determine the depth relative to the hand, thereby simplifying the entire system. Placing the camera on the palm allows for a more natural interaction with the environment.

## Microcontroller
The microcontroller picked is an ESP32 DevkitC module. It was selected because it is affordable, has the options of wireless connectivity and low power consumption and unlike the Arduino Nano 33 BLE Sense which was the first attempt has no upper limit into how many GPIO pins can provide a PWM signal concurrently. 

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/88ff2443-5617-46f3-9696-089be96f96b0" alt="drawing" width="200" align="center"/>

*Figure 5: ESP32 module*

## Depth Estimation

In order to estimate the depth from a mono camera the vision transformer model DPT-Large by Intel was used. This transformer was trained on 1.4 million images for monocular depth estimation and it can predict the relative depth in an image frame. The Python class [MonoDepthEstimator](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/depth_estimation.py) implements this transformer with functions that can find the depth of a frame. For sanity checking the depth frames are visualized as a 3D point cloud using the [3D reconstruction](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/3d_reconstruct.py) script and the relative distances between the objects captured seem reasonable and is accurate for which object is closer to the camera. A sample depth video that is used to test the glove in its early stages and to visualize the depth estimation created by the [depth video creating script](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/depth_video_creating_script.py) is shown in Figure 5.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/135776e8-b464-43d5-a2df-3e344ee7d691" alt="drawing" width="200" align="center"/>

*Figure 6: Mono depth video example*

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/2aa2a9c4-4d7b-4847-aadd-1fce5db49565" alt="drawing" width="200" align="center"/>

*Figure 7: Point cloud*

## Intensity mapping

The [IntensityMapper](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/intensity_mapper.py) class is responsible for getting the depth map and the positions of the motors on the glove and getting the PWM values by averaging the values around the corresponding pixel in the depth map. It performs the mapping by being input teh positions of the motors in a coordinate system on the frame of the device.


## Serial Communication

The [serial communicator](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/serial_com.py) class is responnsible for connecting the Python backend serially to the ESP32, transmitting the motor intensities and validating if those intensities were properly received.

## Microcontroller script

The [ESP32 script](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/motor_test.ino) is responsible for listening to the serial communication channel and reading and decoding the comma seperated string message that has the motor itnensities sent by the Python backend. Then it assigns these PWM intensities as PWM signals to the pins corresponding to each motor and send back the received intensities for the backend to confirm whether the communication was correct.

 ## Helper scripts

The [camera calibration](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/calibrate_cam_script.py) script is used to obtain camera parameters such as the foundational matrix, the intrinsic and extrinsic parameters and the lens distortions to be used in the 3D reconstruction or in estimating the depth.

## Prototype

A generic hand shaped frame was formed by gluing together wooden popsickles. Then all the electronics were mounted on top of the frame. The camera and the ESP32 are connected to the laptop through USB ports. The cables controlling the motors are connected to respective digital and analog pins (they both can provide PWM signals) of the ESP32. Lastly the power supply wires are connected to a 5V pwoer supply output and the ground of the power supply and the ESP32 are connected.

By running the [main.py](https://github.com/TechT3o/Haptic_depth_sensing_glove/blob/main/main.py) script we can operate the prototype and a visualziation that shows what the device captures and where the intensity of each motor is found from is shown.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/69f96527-aa2f-44b2-b332-74a325bf75b6" alt="drawing" width="200" align="center"/>

*Figure 6: Prototype*


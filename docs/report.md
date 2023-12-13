# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

A Haptic feedback glove device that uses a motor camera and mini motor disks to help visually impaired people understand the 3d space around them.
A small camera is mounted on the palm of a visually impaired user and is used to construct a depth map used to perform sensory substituition of vision using a high resolution haptic feedback device comprised of an array of mini DC motor discs with intensity analogous to how close an object is.
The goal is for the user to be able to do wayfinding and navigate in a room using the device. User studies that examine the usability and quality of the device were done showing that the glove ... .

# 1. Introduction

This section should cover the following items:

* Motivation & Objective: What are you trying to do and why? (plain English without jargon)
* State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
* Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
* Challenges: What are the challenges and risks?
* Requirements for Success: What skills and resources are necessary to perform the project?
* Metrics of Success: What are metrics by which you would check for success?

# 2. Related Work

There are multiple different approaches that have been performed for sensory substitution of vision to aid VI people in performing multiple different tasks and with multiple different technologies.

The tasks are:
- Navigating a map
- Wayfinding
- Mental mapping
- VR navigating
- Fetching objects
- Driving
- Feeling 2D data

And the technologies used vary and are:
- Vibrotactile on a mobile device
- Smart walker
- Belt
- Smartphone
- Drone
- VR headset
- Camera Bracelet
- Smart Cane
- Tactile wristband
- Sonar array with vibrotactile motors
- Resonating pin array
- Glove with motors
- Audio feedback
- Tablet
- Sleeve
- Smartwatch

The technologies that rely on audio feedback have the limitations of overloading the sensory channel and are slow to transmit environmental information to the user.
Smartphones, tablets, canes, smartwatches, belts, wristbands, and sleeves can transmit a limited amount of information and can't directly provide the 3D space information but require an encoding of this information that is difficult for the user to learn.
Resonating pin arrays and sonar arrays require expensive, bulky, and not portable equipment.

# 3. Technical Approach

The design of our glove encompasses two fundamental aspects: the hardware and the software

## Hardware

The hardware required for the project involved the camera which was needed to sense the environment as vision is the sense that we want to substitute, the actuator was chosen to be an array of mini vibrational disk motors, the motor driver which was required to operate the disk motors, the microcontroller that was responsible for controlling the disk motor array, the wooden frame that would structure the device and the PC which was the main computational unit.

### Motor array

A motor array was selected to encode the visual information to touch. It was shown that an array of virbtactile motors with enough resolution could be used to understand shapes and therefore it could be used to help BVI understand what kind objects are found around them in space. Vibrating mini motor discs were chosen as they are cheap and small enough to fit in the human palm and can stimulate the pacinian corpuscles (PC) that are the sensory nerve responsible for receiving pressure and vibration that are located in the human palm in high density. 8 motors were placed in the middle of the palm in a square shape and 5 more motors were placed on the finger tips (which have the highest density of PCs) resulting in a 13 motor array.

### Motor driver circuit

From the electronic perspective, the vibrating mini motors that we are using for haptic feedback demand approximately 100 mA of current to achieve optimal rotation at 5V power. Given that the processor’s output pins cannot supply this current, a dedicated driver circuit is essential for powering the motor through a PWM (Pulse Width Modulation) signal. Therefore, we are using NPN transistors with bases connected to the processor pins functioning as a dynamic voltage-controlled current source, to supply the necessary current for motors to work in their optimal operational range. A PWM signal modulates the current supplied to the motors through this configuration, enabling the processor to control the transistors. In addition to meeting the motor's power requirements, this also provides us with haptic feedback because it gives us control over the motor's power.

The mini disk motors require around 100 mA of current in order to rotate at full speed with 5V power. The ESP32 GPIO output pins can provide up to 40 mA, therefore we designed a driver circuit to be able to power the motor using a PWM signal. The circuit shown in Figure 1 was built. It uses an NPN transistor whose base is connected to the GPIO output pin of the ESP32. When the PWM signal gets applied to the base of the transistor the Collector Emitter channel opens and current from the VCC flows through the disk motor and makes it spin with intensity analogous to the PWM signal. The resistor R2 limits the current flowing through the disk motor. A value of 30 Ohms was selected as 5V/30 = 166 mA max current that could flow through R2 ignoring rest of the circuit resistances. R1 was selected to limit the base current. As the base current is very small values of up to 5k could be selected but the chosen value for R1 in this project was 2.2k Ohms. The capacitor is used to soften voltage spikes from the power supply and suppress electrical noise from the motor's rotation and a diode is put to protect against back EMF.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/c52ca1bd-b7f3-442d-acfb-adf6d63f25e5" alt="drawing" width="200" align="center"/>

*Figure 1: Motor driver circuit*

The PCB of this circuit shown in Figure 2 was made and the Gerber files were sent to [OSHPARK](https://oshpark.com/) for manufacturing.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/0849f1bc-9bf5-438c-accb-9387e1dbf27c" alt="drawing" width="200" align="center"/>

*Figure 2: Motor driver PCB*

The received PCBs arrived and the components were soldered on top of it with the disk motors attached to the back of the PCB.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/5368494d-5bee-4cc1-82d2-87d380974121" alt="drawing" width="200" align="center"/>

*Figure 3: PCB*

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/4977230c-6801-469e-8884-8b859b470c98" alt="drawing" width="200" align="center"/>

*Figure 4: Soldered circuits*

### Camera

When choosing the camera we wanted a camera with a small size that could fit the device, as little distortion as possible (no wide angle cameras that tend to have a lot of barrel distortion), low latency and good enough resolution for the depth estimation model to give accurate results. The camera selected was a 5MP USB Camera Webcam with 60 Degree FOV and Autofocus Lens by IFWATER.

It used the OV5640 CMOS (Complementary Metal-Oxide-Semiconductor) image sensor which has high resolution of 2592 x 1944 pixels and can achieve frame rates of 30 FPS.

The location of the camera was another dilemma in our design consideration. As originally intended, it was supposed to be connected to the user's body. However, by relocating the camera to the palm, we eliminated the need to determine the depth relative to the hand, thereby simplifying the entire system. Placing the camera on the palm allows for a more natural interaction with the environment.

### Microcontroller
The microcontroller picked is an ESP32 DevkitC module. It was selected because it is affordable, has the options of wireless connectivity and low power consumption and unlike the Arduino Nano 33 BLE Sense which was the first attempt has no upper limit into how many GPIO pins can provide a PWM signal concurrently. 

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/88ff2443-5617-46f3-9696-089be96f96b0" alt="drawing" width="200" align="center"/>


*Figure 5: ESP32 module*

### Frame

In order to structure the device and mount these electronics a frame was created by gluing wooden popsickles together into the hand like structure. A whole was cut in the middle in order for the wires to pass through and then the motor modules and the camera were hot glued on the wooden skeleton. A rubber band was also hot glued in order to be able to attach the device on the user creating the prototype shown in Figure 6.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/69f96527-aa2f-44b2-b332-74a325bf75b6" alt="drawing" width="200" align="center"/>


*Figure 6: Prototype*

### Computational Unit (PC)

For running the backend and perform the most computationally intensive parts we used an HP Pavilion gaming laptop with an AMD Ryzen 7 5800H CPU and an NVIDIA GeForce RTX 3050 Laptop GPU.

## Software
The software side consisted of the depth estimation algorithm, the serial communication and mapping the depth to the intensity of the motor.


### Depth Estimation

In order to estimate the depth from a mono camera the vision transformer model DPT-Large by Intel was used. This transformer was trained on 1.4 million images for monocular depth estimation and it can predict the relative depth in an image frame. DPT uses the Vision Transformer (ViT) as backbone and adds a neck + head on top for monocular depth estimation.

A depth video produced with this model is shown in Figure 7. For this particular application the relative depth works well as we want to make sure that the user can understand which object is closer to them to avoid collision and we are not as interested in the absolute depth value. By reconstructing the point cloud of a depth frame in Figure 8 we see that the scales captured are sensible.

The depth estimation is the bottleneck of this pipeline with inferences taking approximately 160ms when operating in our computing unit and it's performance reduces in challenging or low light conditions.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/135776e8-b464-43d5-a2df-3e344ee7d691" alt="drawing" width="200" align="center"/>

*Figure 7: Mono depth video example*

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/2aa2a9c4-4d7b-4847-aadd-1fce5db49565" alt="drawing" width="200" align="center"/>

*Figure 8: Point cloud*

### Intensity mapping

We investigated a mapping technique in order to translate the visual depth information into a PWM value that will control the intensity of the motor. The locations of the motors in a device surface coordinate system is given and is projected on the dimensions of the depth map. Then a window is taken around each pixel value and the average of the depth values is found to avoid extreme erroneous depth values that may result by considering a single pixel. As the motors start to operate with a PWM signal above 70 / 255, objects that are very far away do not make the motors vibrate which is beneficial as we do not want the sensory channel to get oversaturated.


### Serial Communication

A serial communication of 9600 baud rate is formed between the Python backend that captures the image, finds the depth, maps the intensity and transmits it and the ESP32 that can send feedback that the communication is succesfull as well as if the motors are in operation. 

## Pototype device

With this we have the prototype device. It works by:
- uploading .ino code to ESP32
- Connecting the ESP32 serially to a USB port of the PC
- Connecting the camera to another USB port of the PC
- Connecting the glove to a power supply
- Conencting the GND of the ESP32 to the glove's power supply
- Running the main.py of the Python backend

This prototype was used for the user study but had limitations such as the length of the USB cables and the power supply cable. Future work should investigate a wireless design that would not require the PC to be dragged along the subject.

# 4. Evaluation and Results

In order to evaluate the usability of the glove a user study was performed on 5 not blind or visually impaired users and qualitative and quantitative feedback was gathered. We measure usability by seperating it into five qualitative metrics Learnability, Efficiency, Memorability, Errors and Satisfaction.  

The study consisted of the physical test where participants had to walk the corridor of engineering 4 UCLA building blindfolded in order to test the sensory substitution ability of the device. The path started inside the graduate lounge where the participants had to find the door and exit the room. Then the participants had to move toward the corner and then proceed to the first corridor. The participants then had to walk down the corridor for 10 m where the end of the path was. This path is shown on Figure 9. 

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/9193547a-0531-414e-80df-614dae292c88" alt="drawing" width="200" align="center"/>

*Figure 9: Navigation path*

The time taken to get to the finish line as well as the number of errors (collisions) was recorded and is shown in Table 1.

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/2e97c733-72c0-4fcc-8978-1eda7f81e20c" alt="drawing" width="200" align="center"/>

*Table 1: Path completion times and number of errors / collision*

After completing the path the users were given a likert scale questionnaire. The questionnaire is shown in Appendix 1 and had the questions seperated into these five different metrics with 2 for Learnability, 4 for Efficiency, 3 for Memorability, 2 for Errors and 4 for Satisfaction. The mean values for each question are foudn in Table 2 and the box plots of the responses of each participant for every metric is shown in Figure 10. 

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/af4924fb-0dc8-4613-bb7e-6a532a74188b" alt="drawing" width="200" align="center"/>

*Table 2: Questionnaire mean value answers for each question*

<img src="https://github.com/TechT3o/Haptic_depth_sensing_glove/assets/87833804/faf4ff55-705f-4ff2-8e06-105ff37edbe9" alt="drawing" width="200" align="center"/>

*Figure 10: Questionnaire results box plots for different metrics*

Observing the comments of the participants while performing the physical task we recorded comments such as "This feels cool", "Interesting", "I can't understand where the object is" and "I can't move my hand without pulling the cables".


# 5. Discussion and Conclusions


The user study gave insights about the usability of the device at the current prototype stage.

Concerning the wayfinding efficiency we see that the time taken for the participants to complete the path had a mean of 75.4 seconds (compared to approximately 12 seconds with sense of vision) and standard deviation of 6.7 and the number of errors was 4.4 errors with standard deviation 1.51. We see that the standard deviations of the time and errors are small that shows consistency accross participants and indicates that the learnability of the device was similar between subjects. We see that all participants have at least 3 errors so there is a learning curve in learning to operate the device. The fact that all participants completed the wayfinding path shows the potential of this device to perform sensory substitution for the task of navigating in a closed space. It is worth to be noted that the participants probably already had a mental model of the building so it might have been easier to navigate compared to being subjected to a completely usneen environment. Getting access to one of the relevant devices discussed in section 2 or a white cane to have a comparison metric would be of interest.

Analyzing the results of the questionnaire by drawing box plots for the different usability metrics we can see that the learnability of this device rates the highest as the time and error metrics also suggested and shows that this type of sensory substitution feels intuitive for the users. The second highest metric is memorability that shows that the user's felt confident reusing or teaching other people how to use the device. This gives insight that the device is considered simple to use. Then the Errors, Satisfaction and Efficiency metrics average around the value of 4 which is a neutral stance with small deviation from the median value showing that all users agreed that the device was not satisfactory, not efficient and had errors. By inspecting the answers in Table 2 for these 3 metrics we see that concerning the error there were many difficulties when using the device but it was easy to recover from these mistakes. Concerning Satisfaction they found the activity engaging but would not use this device for wayfinding. And concerning efficiency they found the device easy to use but they couldn't effectively perform wayfinding.

Combining the qualitative feedback we see that we have positive comments such as "This feels cool" and "Interesting" but also negative comments such as "I can't understand where the object is" and "I can't move my hand without pulling the cables" that agrees with the satisfaction, errors and efficiency metrics being in the middle of the likert scale.

# 6. References

[1]Yatani, K., Banovic, N., & Truong, K. (2012, May). SpaceSense: representing geographical information to visually impaired people using spatial tactile feedback. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 415-424).

[2] Jimenez, M. F., Mello, R. C., Bastos, T., & Frizera, A. (2020). Assistive locomotion device with haptic feedback for guiding visually impaired people. Medical Engineering & Physics, 80, 18-25.

[3] Katzschmann, R. K., Araki, B., & Rus, D. (2018). Safe local navigation for visually impaired users with a time-of-flight and haptic feedback device. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 26(3), 583-593.

[4] Fagernes, S., & Grønli, T. M. (2018). Navigation for visually impaired using haptic feedback. In Human-Computer Interaction. Interaction in Context: 20th International Conference, HCI International 2018, Las Vegas, NV, USA, July 15–20, 2018, Proceedings, Part II 20 (pp. 347-356). Springer International Publishing.

[5] Huppert, F., Hoelzl, G., & Kranz, M. (2021, May). GuideCopter-A precise drone-based haptic guidance interface for blind or visually impaired people. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (pp. 1-14).

[6] Lahav, O., & Mioduser, D. (2008). Haptic-feedback support for cognitive mapping of unknown spaces by people who are blind. International Journal of Human-Computer Studies, 66(1), 23-35.

[7] Moustakas, K., Nikolakis, G., Kostopoulos, K., Tzovaras, D., & Strintzis, M. G. (2007). Haptic rendering of visual data for the visually impaired. IEEE MultiMedia, 14(1), 62-72.

[8] Scheggi, S., Talarico, A., & Prattichizzo, D. (2014, June). A remote guidance system for blind and visually impaired people via vibrotactile haptic feedback. In 22nd Mediterranean conference on control and automation (pp. 20-23). IEEE.

[9] Zhang, X., Zhang, H., Zhang, L., Zhu, Y., & Hu, F. (2019). Double-diamond model-based orientation guidance in wearable human–machine navigation systems for blind and visually impaired people. Sensors, 19(21), 4670.

[10] Kuriakose, B., Shrestha, R., & Sandnes, F. E. (2020, July). Smartphone navigation support for blind and visually impaired people-a comprehensive analysis of potentials and opportunities. In Universal Access in Human-Computer Interaction. Applications and Practice: 14th International Conference, UAHCI 2020, Held as Part of the 22nd HCI International Conference, HCII 2020, Copenhagen, Denmark, July 19–24, 2020, Proceedings, Part II (pp. 568-583). Cham: Springer International Publishing.

[11] Cardin, S., Thalmann, D., & Vexo, F. (2007). A wearable system for mobility improvement of visually impaired people. The Visual Computer, 23, 109-118.

[12] Ramirez, A. R. G., da Silva, R. F. L., Cinelli, M. J., & de Albornoz, A. D. C. (2012). Evaluation of electronic haptic device for blind and visually impaired people: a case study. Journal of Medical and Biological Engineering, 32(6), 423-428.

[13] He, L., Wang, R., & Xu, X. (2020, April). PneuFetch: supporting blind and visually impaired people to fetch nearby objects via light haptic cues. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems (pp. 1-9).

[14] Pokluda, L., & Sochor, J. (2003). Spatial haptic orientation for visually impaired people. EG, 3, 29-34.

[15] Wi, D., Sodemann, A., & Chicci, R. (2017, August). Vibratory haptic feedback assistive device for visually-impaired drivers. In 2017 IEEE SmartWorld, Ubiquitous Intelligence & Computing, Advanced & Trusted Computed, Scalable Computing & Communications, Cloud & Big Data Computing, Internet of People and Smart City Innovation (SmartWorld/SCALCOM/UIC/ATC/CBDCom/IOP/SCI) (pp. 1-5). IEEE.

[16] Poggi, M., & Mattoccia, S. (2016, June). A wearable mobility aid for the visually impaired based on embedded 3D vision and deep learning. In 2016 IEEE symposium on computers and communication (ISCC) (pp. 208-213). IEEE.

[17] Xiao, J., Joseph, S. L., Zhang, X., Li, B., Li, X., & Zhang, J. (2015). An assistive navigation framework for the visually impaired. IEEE transactions on human-machine systems, 45(5), 635-640.

[18] Treuillet, S., Royer, E., Chateau, T., Dhome, M., & Lavest, J. M. (2007, August). Body Mounted Vision System for Visually Impaired Outdoor and Indoor Wayfinding Assistance. In CVHI.

[19] Kulyukin, V., Gharpure, C., Nicholson, J., & Osborne, G. (2006). Robot-assisted wayfinding for the visually impaired in structured indoor environments. Autonomous robots, 21, 29-41.

[20] Zhang, H., & Ye, C. (2016, December). An indoor navigation aid for the visually impaired. In 2016 IEEE international conference on robotics and biomimetics (ROBIO) (pp. 467-472). IEEE.

[21] Yang, G., & Saniie, J. (2020). Sight-to-sound human-machine interface for guiding and navigating visually impaired people. IEEE Access, 8, 185416-185428.

[22] Zöllner, M., Huber, S., Jetter, H. C., & Reiterer, H. (2011). NAVI–a proof-of-concept of a mobile navigational aid for visually impaired based on the microsoft kinect. In Human-Computer Interaction–INTERACT 2011: 13th IFIP TC 13 International Conference, Lisbon, Portugal, September 5-9, 2011, Proceedings, Part IV 13 (pp. 584-587). Springer Berlin Heidelberg.

[23] Kammoun, S., Parseihian, G., Gutierrez, O., Brilhault, A., Serpa, A., Raynal, M., ... & Jouffrais, C. (2012). Navigation and space perception assistance for the visually impaired: The NAVIG project. Irbm, 33(2), 182-189.

[24] Bai, J., Liu, Z., Lin, Y., Li, Y., Lian, S., & Liu, D. (2019). Wearable travel aid for environment perception and navigation of visually impaired people. Electronics, 8(6), 697.

[25] Li, B., Munoz, J. P., Rong, X., Chen, Q., Xiao, J., Tian, Y., ... & Yousuf, M. (2018). Vision-based mobile indoor assistive navigation aid for blind people. IEEE transactions on mobile computing, 18(3), 702-714.

[26] Gay, S. L., Pissaloux, E., Romeo, K., & Truong, N. T. (2021). F2T: a novel force-feedback haptic architecture delivering 2D data to visually impaired people. IEEE Access, 9, 94901-94911.

[27] Zahn, M., & Khan, A. A. (2022). Obstacle avoidance for blind people using a 3D camera and a haptic feedback sleeve. arXiv preprint arXiv:2201.04453.

[28] Zelek, J. S., Bromley, S., Asmar, D., & Thompson, D. (2003). A haptic glove as a tactile-vision sensory substitution for wayfinding. Journal of Visual Impairment & Blindness, 97(10), 621-632.

[29] Shrewsbury, B. T. (2011, October). Providing haptic feedback using the kinect. In The proceedings of the 13th international ACM SIGACCESS conference on Computers and accessibility (pp. 321-322).

[30] Shen, H., Edwards, O., Miele, J., & Coughlan, J. M. (2013, October). CamIO: a 3D computer vision system enabling audio/haptic interaction with physical objects by blind users. In Proceedings of the 15th International ACM SIGACCESS Conference on Computers and Accessibility (pp. 1-2).

[31] Bauer, Z., Dominguez, A., Cruz, E., Gomez-Donoso, F., Orts-Escolano, S., & Cazorla, M. (2020). Enhancing perception for the visually impaired with deep learning techniques and low-cost wearable sensors. Pattern recognition letters, 137, 27-36.

[32] Yelamarthi, K., DeJong, B. P., & Laubhan, K. (2014, August). A kinect based vibrotactile feedback system to assist the visually impaired. In 2014 IEEE 57th International Midwest Symposium on Circuits and Systems (MWSCAS) (pp. 635-638). IEEE.

[33] Kaczmarek, K. A., Webster, J. G., Bach-y-Rita, P., & Tompkins, W. J. (1991). Electrotactile and vibrotactile displays for sensory substitution systems. IEEE transactions on biomedical engineering, 38(1), 1-16.

[34] Ribani, R., & Marengoni, M. (2019, January). Vision Substitution with Object Detection and Vibrotactile Stimulus. In VISIGRAPP (4: VISAPP) (pp. 584-590).

[35] Bach-y-Rita, P., & Kercel, S. W. (2003). Sensory substitution and the human–machine interface. Trends in cognitive sciences, 7(12), 541-546.

[36] Mante, N., & Weiland, J. D. (2018, July). Visually impaired users can locate and grasp objects under the guidance of computer vision and non-visual feedback. In 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (pp. 1-4). IEEE.

[37] Alahakone, A. U., & Senanayake, S. A. (2009, July). Vibrotactile feedback systems: Current trends in rehabilitation, sports and information display. In 2009 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (pp. 1148-1153). IEEE.

[38] Bastidas Cuya, F. G., Martins Guarese, R. L., Johansson, C. G., Giambastiani, M., Iquiapaza, Y., de Jesus Oliveira, V. A., ... & Maciel, A. (2021, October). Vibrotactile Data Physicalization: Exploratory Insights for Haptization of Low-resolution Images. In Symposium on Virtual and Augmented Reality (pp. 84-91).

[39] Intel DPT-Large Mono depth estimator

[40] Eagle EDA

# Appendix 1

[depth_glove_form.pdf](https://github.com/TechT3o/Haptic_depth_sensing_glove/files/13643433/depth_glove_form.pdf)

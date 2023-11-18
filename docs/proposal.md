# Project Proposal

## 1. Motivation & Objective

About 284 million people are visually impaired (VI) worldwide and of these, 39 million of them are blind. Common problems that VI people face are the difficulty in navigating / finding their way in the environment, losing objects that are misplaced on surfaces, or identifying and fetching objects around them that are further away from their grasp.

In this project a haptic feedback glove device that uses a motor camera and mini motor disks to help visually impaired people understand the 3D space around them is built. The idea is to mount a small camera on the palm of the visually impaired user, construct the depth map, and perform sensory substitution of vision by using a high-resolution haptic feedback glove comprised of an array of mini DC motor disks to assign a different intensity in the direction where the user's hand is pointing at, analogous to how close the object is.

The goal is for the user to be able to identify what type of object their hand is pointing at for object recognition and object fetching and for the user to be able to do wayfinding and navigate in a room using the device. User studies that examine the usability and effectiveness of the device will be done.

## 2. State of the Art & Its Limitations

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

## 3. Novelty & Rationale

Our proposed solution belongs to the family of gloves with motors and aims to tackle the problems of object fetching and wayfinding by allowing for cheap, portable, easy to learn, direct and low-latency feedback of the 3D space without sensory overload.

The resources indicate that:
- Relative depth information can be extracted from a mono camera using neural networks
- Sensory substitution can be performed with vibrotactile motor arrays
- Shapes, faces and objects can be recognized using motor arrays.

Therefore, it should be feasible to combine this research and construct a haptic depth sensing glove that can perform sensory substitution and explore its effectiveness and usability for the tasks of object fetching and wayfinding.


## 4. Potential Impact

### Technical Impact

The technologies developed for this project will have a technical impact since:
- A haptic feedback device will be developed
- The sensitivity and resolution of the human palm to vibrotactile feedback will be investigated
- A real-time mono camera depth estimation system that can be used by embedded devices will be developed

  ### Broad impact

  There are multiple applications for such a device and multiple people can benefit from it.
  
  Visually impaired people will now:
  - have an alternative to navigate in new environments resulting in greater mobility and quality of life.
  - have a way to recognize and fetch objects making them more self-reliant and solving the problem of lost objects.

  Therefore such a device could practically improve the quality of life of the visually impaired community, let them become more self-reliant, more easily navigate to new places, and alleviate pressure from their caregivers.

   With the rise of Virtual Reality headsets and Augmented Reality applications, there is an active research field and a need to develop ubiquitous haptic feedback devices to help a user interact with the virtual world. This glove could be used to address this need and provide haptic feedback such as for button pressing or touching and recognizing virtual objects tasks frequently encountered in Human-Computer Interaction.

## 5. Challenges

- Achieving depth estimation with good enough resolution to understand relative distances between camera objects
- Achieve real-time performance so that there is no latency between where the user is pointing and the perceived haptic feedback
- Achieve good enough haptic resolution with the motor array for the user to recognize different objects and perform wayfinding

## 6. Requirements for Success

- Python skills are required to make a running backend that can collect camera information, find the depth, and determine the mapping and intensities of the motors.
- C++ skills are needed to program the Arduino to communicate with the Python backend, and to control the intensities of each motor.
- Electronic circuit design and soldering skills are required to connect the motors and camera to the microcontroller and to create the motor driver circuit and PCBs.
- 3D printing and design skills are required to print casing for electronic components.
- Hands-on skills are required to put the glove together.

## 7. Metrics of Success

### Quantitative

#### Wayfinding / navigation study
Navigation accuracy - Able to navigate in the room?
Navigation speed - How much time to reach the destination?

#### Object recognition / fetching study
Recognition accuracy - How many objects were detected? 
Recognition speed - How much time to figure out an object?

### Qualitative
- Interview (record answers and do affinity diagram)
- Likert scale questionnaires to figure usability

#### Usability
- Learnability
- Efficiency
- Memorability
- Errors
- Satisfaction

## 8. Execution Plan

### Glove / Haptic side

- Design motor driver circuit.
- Design motor pcb.
- Assemble motor PCBs.
- Check which array configuration is best ( How many motors are in an array, in which places to be placed, what kind of depth to intensity mapping).
- Check if it is possible to understand the type of object using the sensor array. (we can use depth maps from other sources as well for testing this).
- Figure depth resolution ( Can you understand two objects being n meters apart from each other).
(These might all change depending on depth to intensity mapping, the position of motors etc)

### Camera side

- Find which camera to use.
- Find where/ how it is convenient to place the camera.
- Transmit camera data to PC.
- Optimize depth estimation pipeline (model, processing, depth to motor intensity conversion etc) to run in real time. (What is the effect of different estimations per second on perceived accuracy?).

### Combine the two

- 3D print cases / parts for mounting electronic components.
- Assemble the glove.
- Transmit data serially (or wirelessly) between the processing backend and haptic glove.
- Start user testing.

### Extension:

- Make glove wireless.
- Make glove battery-powered.
- Try 3d reconstruction of space and handling VR objects

## 9. Related Work

### 9.a. Papers

- SpaceSense: representing geographical information to visually impaired people using spatial tactile feedback.

Related since it uses tactile feedback to transfer digital information to VI people.

- Assistive locomotion device with haptic feedback for guiding visually impaired people.

Another type of haptic feedback device is used for wayfinding of VI people.

- Safe local navigation for visually impaired users with a time-of-flight and haptic feedback device.

Similar concept but uses the time of flight sensor and doesn't use a motor array.

- Navigation for the visually impaired using haptic feedback.

Also explores using haptic feedback to transfer location information.

- GuideCopter-A precise drone-based haptic guidance interface for blind or visually impaired people.

Different haptic feedback techniques for guiding VI people.

- Haptic-feedback support for cognitive mapping of unknown spaces by people who are blind.

Present haptic feedback and the idea of mental mapping for blind people that is a potential application of our proposed solution 

- Haptic rendering of visual data for the visually impaired.

Related since it uses tactile feedback to transfer digital information to VI people.

- A remote guidance system for blind and visually impaired people via vibrotactile haptic feedback.

Also explores using vibrotactile haptic feedback to guide VI people.

- Double-diamond model-based orientation guidance in wearable human–machine navigation systems for blind and visually impaired people.

Explains other types of HCI for orientation guidance of VI people.

- Smartphone navigation support for blind and visually impaired people-a comprehensive analysis of potentials and opportunities.

Other types of navigation devices for VI people.

- A wearable system for mobility improvement of visually impaired people.

Similar kind of system improves the mobility of VI people.

- Evaluation of electronic haptic device for blind and visually impaired people: a case study.

Summary paper explaining many uses of haptic devices to aid VI people.

- PneuFetch: supporting blind and visually impaired people to fetch nearby objects via light haptic cues.

A different approach to object fetching for VI people.

- Spatial haptic orientation for visually impaired people.

Similar approach of using haptic feedback for orientation for VI people.

- Vibratory haptic feedback assistive device for visually-impaired drivers.

Haptic feedback method for VI people even though the addressed problem is driving

- A wearable mobility aid for the visually impaired based on embedded 3D vision and deep learning.

Similar to the concept of finding depth map with embedded devices even though different device type

- An assistive navigation framework for the visually impaired.

Other types of navigation for visually impaired people

- Body Mounted Vision System for Visually Impaired Outdoor and Indoor Wayfinding Assistance.

Other approaches of wayfinding using body mounted components for VI people.

- Robot-assisted wayfinding for the visually impaired in structured indoor environments.

Other approaches of wayfinding for VI people.

- An indoor navigation aid for the visually impaired.

Other types of navigation approach for VI people.

- Sight-to-sound human-machine interface for guiding and navigating visually impaired people.

Other types of sensory substitution systems for aiding VI people.

- NAVI–a proof-of-concept of a mobile navigational aid for the visually impaired based on the Microsoft Kinect.

Other types of using depth cameras for the navigation of VI people.

- Navigation and space perception assistance for the visually impaired: The NAVIG project.

Similar in the way that it explores navigation in space for VI people.

- Wearable travel aid for environment perception and navigation of visually impaired people.

Similar problems are solved with different types of devices.

- Vision-based mobile indoor assistive navigation aid for blind people.

Another use of vision for navigation for VI people.

- F2T: a novel force-feedback haptic architecture delivering 2D data to visually impaired people.

Related since it uses tactile feedback to transfer digital information to VI people.

- Obstacle avoidance for blind people using a 3D camera and a haptic feedback sleeve.

Similar concept but it uses a sleeve instead of a glove.

- A haptic glove as a tactile-vision sensory substitution for wayfinding.

Very similar paper as they also use a glove-based embedded system to do sensory substitution for wayfinding.

- Providing haptic feedback using the Kinect.

Similar in that they use 3d maps and haptic feedback.

- CamIO: a 3D computer vision system enabling audio/haptic interaction with physical objects by blind users.

Related to the extension of the project for VR applications, but the technology vision and haptic part of technology are similar.

- Enhancing perception for the visually impaired with deep learning techniques and low-cost wearable sensors.

Similar idea of using deep learning vision and low-cost wearable sensors.

- A Kinect-based vibrotactile feedback system to assist the visually impaired.

Similar project where they use depth map to provide tactile feedback.

- Electrotactile and vibrotactile displays for sensory substitution systems.

Checks the effectiveness of a vibrotactile display (similar to a motor array) for sensory substitution. 

- Vision Substitution with Object Detection and Vibrotactile Stimulus.

Checks vision substitution system with vibrotactile motors.

- Sensory substitution and the human–machine interface.

Summary of sensory substitution in HCI.

- Visually impaired users can locate and grasp objects under the guidance of computer vision and non-visual feedback.

Similar concept of recognizing and fetching objects using computer vision. Different types of stimulus such as audio and tactile explored.

- Vibrotactile feedback systems: Current trends in rehabilitation, sports, and information display.

Summary of uses of vibrotactile feedback systems.

- Vibrotactile Data Physicalization: Exploratory Insights for Haptization of Low-resolution Images.

Gives insights on understanding low-resolution images using vibrotactile motors.

### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

### 9.c. Software

Intel DPT-Large mono depth sensing model

Eagle EDA

## 10. References

[[1](https://www.researchgate.net/publication/254005210_SpaceSense_Representing_Geographical_Information_to_Visually_Impaired_People_Using_Spatial_Tactile_Feedback)]Yatani, K., Banovic, N., & Truong, K. (2012, May). SpaceSense: representing geographical information to visually impaired people using spatial tactile feedback. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 415-424).

[[2](https://pubmed.ncbi.nlm.nih.gov/32446757/)] Jimenez, M. F., Mello, R. C., Bastos, T., & Frizera, A. (2020). Assistive locomotion device with haptic feedback for guiding visually impaired people. Medical Engineering & Physics, 80, 18-25.

[[3](https://dspace.mit.edu/bitstream/handle/1721.1/114285/Katzschmann%20et%20al.%20-%202018%20-%20Safe%20Local%20Navigation%20for%20Visually%20Impaired%20Users%20with%20a%20Time-of-Flight%20and%20Haptic%20Feedback%20Device%20-%20Final.pdf)]  Katzschmann, R. K., Araki, B., & Rus, D. (2018). Safe local navigation for visually impaired users with a time-of-flight and haptic feedback device. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 26(3), 583-593.

[[4](https://www.researchgate.net/publication/325468302_Navigation_for_Visually_Impaired_Using_Haptic_Feedback)] Fagernes, S., & Grønli, T. M. (2018). Navigation for visually impaired using haptic feedback. In Human-Computer Interaction. Interaction in Context: 20th International Conference, HCI International 2018, Las Vegas, NV, USA, July 15–20, 2018, Proceedings, Part II 20 (pp. 347-356). Springer International Publishing.

[[5](https://dl.acm.org/doi/10.1145/3411764.3445676)] Huppert, F., Hoelzl, G., & Kranz, M. (2021, May). GuideCopter-A precise drone-based haptic guidance interface for blind or visually impaired people. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (pp. 1-14).

[[6](https://www.sciencedirect.com/science/article/pii/S1071581907001012)] Lahav, O., & Mioduser, D. (2008). Haptic-feedback support for cognitive mapping of unknown spaces by people who are blind. International Journal of Human-Computer Studies, 66(1), 23-35.

[[7](https://www.researchgate.net/publication/3338948_Haptic_Rendering_of_Visual_Data_for_the_Visually_Impaired)] Moustakas, K., Nikolakis, G., Kostopoulos, K., Tzovaras, D., & Strintzis, M. G. (2007). Haptic rendering of visual data for the visually impaired. IEEE MultiMedia, 14(1), 62-72.

[[8](https://www.researchgate.net/publication/263195992_A_remote_guidance_system_for_blind_and_visually_impaired_people_via_vibrotactile_haptic_feedback)] Scheggi, S., Talarico, A., & Prattichizzo, D. (2014, June). A remote guidance system for blind and visually impaired people via vibrotactile haptic feedback. In 22nd Mediterranean conference on control and automation (pp. 20-23). IEEE.

[[9](https://pubmed.ncbi.nlm.nih.gov/31661798/)] Zhang, X., Zhang, H., Zhang, L., Zhu, Y., & Hu, F. (2019). Double-diamond model-based orientation guidance in wearable human–machine navigation systems for blind and visually impaired people. Sensors, 19(21), 4670.

[[10](https://www.researchgate.net/publication/342835249_Smartphone_Navigation_Support_for_Blind_and_Visually_Impaired_People_-_A_Comprehensive_Analysis_of_Potentials_and_Opportunities)] Kuriakose, B., Shrestha, R., & Sandnes, F. E. (2020, July). Smartphone navigation support for blind and visually impaired people-a comprehensive analysis of potentials and opportunities. In Universal Access in Human-Computer Interaction. Applications and Practice: 14th International Conference, UAHCI 2020, Held as Part of the 22nd HCI International Conference, HCII 2020, Copenhagen, Denmark, July 19–24, 2020, Proceedings, Part II (pp. 568-583). Cham: Springer International Publishing.

[[11](https://link.springer.com/article/10.1007/s00371-006-0032-4)] Cardin, S., Thalmann, D., & Vexo, F. (2007). A wearable system for mobility improvement of visually impaired people. The Visual Computer, 23, 109-118.

[[12](https://staff.www.ltu.se/~kalevi/References/Evaluation%20of%20electronic%20haptic%20device%20for%20blind%20and%20visually%20impaired%20people%20A%20case%20study.pdf)] Ramirez, A. R. G., da Silva, R. F. L., Cinelli, M. J., & de Albornoz, A. D. C. (2012). Evaluation of electronic haptic device for blind and visually impaired people: a case study. Journal of Medical and Biological Engineering, 32(6), 423-428.

[[13](https://makeabilitylab.cs.washington.edu/media/publications/He_PneufetchSupportingBlindAndVisuallyImpairedPeopleToFetchNearbyObjectsViaLightHapticCues_CHI2020.pdf)] He, L., Wang, R., & Xu, X. (2020, April). PneuFetch: supporting blind and visually impaired people to fetch nearby objects via light haptic cues. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems (pp. 1-9).

[[14](https://decibel.fi.muni.cz/download/papers/pokluda03.pdf)] Pokluda, L., & Sochor, J. (2003). Spatial haptic orientation for visually impaired people. EG, 3, 29-34.

[[15](https://www.researchgate.net/publication/326050483_Vibratory_Haptic_feedback_assistive_device_for_visually-impaired_drivers)] Wi, D., Sodemann, A., & Chicci, R. (2017, August). Vibratory haptic feedback assistive device for visually-impaired drivers. In 2017 IEEE SmartWorld, Ubiquitous Intelligence & Computing, Advanced & Trusted Computed, Scalable Computing & Communications, Cloud & Big Data Computing, Internet of People and Smart City Innovation (SmartWorld/SCALCOM/UIC/ATC/CBDCom/IOP/SCI) (pp. 1-5). IEEE.

[[16](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7543741&tag=1)] Poggi, M., & Mattoccia, S. (2016, June). A wearable mobility aid for the visually impaired based on embedded 3D vision and deep learning. In 2016 IEEE symposium on computers and communication (ISCC) (pp. 208-213). IEEE.

[[17](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7010003)] Xiao, J., Joseph, S. L., Zhang, X., Li, B., Li, X., & Zhang, J. (2015). An assistive navigation framework for the visually impaired. IEEE transactions on human-machine systems, 45(5), 635-640.

[[18](https://www.researchgate.net/publication/221311676_Body_Mounted_Vision_System_For_Visually_Impaired_Outdoor_And_Indoor_Wayfindind_Assistance)] Treuillet, S., Royer, E., Chateau, T., Dhome, M., & Lavest, J. M. (2007, August). Body Mounted Vision System for Visually Impaired Outdoor and Indoor Wayfinding Assistance. In CVHI.

[[19](https://link.springer.com/article/10.1007/s10514-006-7223-8)] Kulyukin, V., Gharpure, C., Nicholson, J., & Osborne, G. (2006). Robot-assisted wayfinding for the visually impaired in structured indoor environments. Autonomous robots, 21, 29-41.

[[20](https://dl.acm.org/doi/abs/10.1109/ROBIO.2016.7866366)] Zhang, H., & Ye, C. (2016, December). An indoor navigation aid for the visually impaired. In 2016 IEEE international conference on robotics and biomimetics (ROBIO) (pp. 467-472). IEEE.

[[21](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9216032)] Yang, G., & Saniie, J. (2020). Sight-to-sound human-machine interface for guiding and navigating visually impaired people. IEEE Access, 8, 185416-185428.

[[22](https://link.springer.com/chapter/10.1007/978-3-642-23768-3_88)] Zöllner, M., Huber, S., Jetter, H. C., & Reiterer, H. (2011). NAVI–a proof-of-concept of a mobile navigational aid for visually impaired based on the microsoft kinect. In Human-Computer Interaction–INTERACT 2011: 13th IFIP TC 13 International Conference, Lisbon, Portugal, September 5-9, 2011, Proceedings, Part IV 13 (pp. 584-587). Springer Berlin Heidelberg.

[[23](https://www.researchgate.net/publication/257736351_Navigation_and_space_perception_assistance_for_the_visually_impaired_The_NAVIG_project)] Kammoun, S., Parseihian, G., Gutierrez, O., Brilhault, A., Serpa, A., Raynal, M., ... & Jouffrais, C. (2012). Navigation and space perception assistance for the visually impaired: The NAVIG project. Irbm, 33(2), 182-189.

[[24](https://www.mdpi.com/2079-9292/8/6/697)] Bai, J., Liu, Z., Lin, Y., Li, Y., Lian, S., & Liu, D. (2019). Wearable travel aid for environment perception and navigation of visually impaired people. Electronics, 8(6), 697.

[[25](https://pubmed.ncbi.nlm.nih.gov/30774566/)] Li, B., Munoz, J. P., Rong, X., Chen, Q., Xiao, J., Tian, Y., ... & Yousuf, M. (2018). Vision-based mobile indoor assistive navigation aid for blind people. IEEE transactions on mobile computing, 18(3), 702-714.

[[26](https://hal.science/hal-03351798/document)] Gay, S. L., Pissaloux, E., Romeo, K., & Truong, N. T. (2021). F2T: a novel force-feedback haptic architecture delivering 2D data to visually impaired people. IEEE Access, 9, 94901-94911.

[[27](https://arxiv.org/abs/2201.04453)] Zahn, M., & Khan, A. A. (2022). Obstacle avoidance for blind people using a 3D camera and a haptic feedback sleeve. arXiv preprint arXiv:2201.04453.

[[28](https://journals.sagepub.com/doi/10.1177/0145482X0309701007)] Zelek, J. S., Bromley, S., Asmar, D., & Thompson, D. (2003). A haptic glove as a tactile-vision sensory substitution for wayfinding. Journal of Visual Impairment & Blindness, 97(10), 621-632.

[[29](https://dl.acm.org/doi/abs/10.1145/2049536.2049628)] Shrewsbury, B. T. (2011, October). Providing haptic feedback using the kinect. In The proceedings of the 13th international ACM SIGACCESS conference on Computers and accessibility (pp. 321-322).

[[30](https://dl.acm.org/doi/10.1145/2513383.2513423)] Shen, H., Edwards, O., Miele, J., & Coughlan, J. M. (2013, October). CamIO: a 3D computer vision system enabling audio/haptic interaction with physical objects by blind users. In Proceedings of the 15th International ACM SIGACCESS Conference on Computers and Accessibility (pp. 1-2).

[[31](https://www.sciencedirect.com/science/article/pii/S0167865519300881)] Bauer, Z., Dominguez, A., Cruz, E., Gomez-Donoso, F., Orts-Escolano, S., & Cazorla, M. (2020). Enhancing perception for the visually impaired with deep learning techniques and low-cost wearable sensors. Pattern recognition letters, 137, 27-36.

[[32](https://www.researchgate.net/publication/264192906_A_Kinect_based_Vibrotactile_Feedback_System_to_Assist_the_Visually_Impaired)] Yelamarthi, K., DeJong, B. P., & Laubhan, K. (2014, August). A kinect based vibrotactile feedback system to assist the visually impaired. In 2014 IEEE 57th International Midwest Symposium on Circuits and Systems (MWSCAS) (pp. 635-638). IEEE.

[[33](https://pubmed.ncbi.nlm.nih.gov/2026426/)] Kaczmarek, K. A., Webster, J. G., Bach-y-Rita, P., & Tompkins, W. J. (1991). Electrotactile and vibrotactile displays for sensory substitution systems. IEEE transactions on biomedical engineering, 38(1), 1-16.

[[34](https://pdfs.semanticscholar.org/06c1/926b0c793d6be8537534c48518e40fc2cb58.pdf)] Ribani, R., & Marengoni, M. (2019, January). Vision Substitution with Object Detection and Vibrotactile Stimulus. In VISIGRAPP (4: VISAPP) (pp. 584-590).

[[35](https://pubmed.ncbi.nlm.nih.gov/14643370/)] Bach-y-Rita, P., & Kercel, S. W. (2003). Sensory substitution and the human–machine interface. Trends in cognitive sciences, 7(12), 541-546.

[[36](https://pubmed.ncbi.nlm.nih.gov/30440276/)] Mante, N., & Weiland, J. D. (2018, July). Visually impaired users can locate and grasp objects under the guidance of computer vision and non-visual feedback. In 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (pp. 1-4). IEEE.

[[37](https://www.researchgate.net/publication/224586228_Vibrotactile_feedback_systems_Current_trends_in_rehabilitation_sports_and_information_display)] Alahakone, A. U., & Senanayake, S. A. (2009, July). Vibrotactile feedback systems: Current trends in rehabilitation, sports and information display. In 2009 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (pp. 1148-1153). IEEE.

[[38](https://www.researchgate.net/publication/355410847_Vibrotactile_Data_Physicalization_Exploratory_Insights_for_Haptization_of_Low-resolution_Images)] Bastidas Cuya, F. G., Martins Guarese, R. L., Johansson, C. G., Giambastiani, M., Iquiapaza, Y., de Jesus Oliveira, V. A., ... & Maciel, A. (2021, October). Vibrotactile Data Physicalization: Exploratory Insights for Haptization of Low-resolution Images. In Symposium on Virtual and Augmented Reality (pp. 84-91).

[[39](https://huggingface.co/Intel/dpt-large)] Intel DPT-Large Mono depth estimator

[[40](https://www.autodesk.com/products/eagle/features)] Eagle EDA

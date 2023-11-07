# Project Proposal

## 1. Motivation & Objective

What are you trying to do and why? (plain English without jargon)

## 2. State of the Art & Its Limitations

How is it done today, and what are the limits of current practice?

## 3. Novelty & Rationale

What is new in your approach and why do you think it will be successful?

## 4. Potential Impact

If the project is successful, what difference will it make, both technically and broadly?

## 5. Challenges

- Achieving depth estimation with good enough resolution to understand relative distances between camera objects
- Achieve real time performance so that there is no latency between where the user is pointing at and the perceived haptic feedback
- Achieve good enough haptic resolution with the motor array for the user to recognize different object and perform wayfinding

## 6. Requirements for Success

What skills and resources are necessary to perform the project?

## 7. Metrics of Success

### Quantitative

#### Wayfinding / navigation study
Navigation accuracy - Able to navigate room?
Navigation speed - How much time to reach destination?

#### Object recognition / fetching study
Recognition accuracy - How many objects detected? 
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
- Assemble motor pcbs
- Check which array configuration is best ( How many motors in array, in which places to be placed, what kind of depth to intensity mapping)
- Check if it is possible to understand the type of object using the sensor array. (we can use depth maps from other sources as well for testing this)
- Figure depth resolution. ( Can you understand two objects being n meters apart from each other)
(These might all change depending on depth to intensity mapping, position of motors etc)

### Camera side

- Find which camera to use.
- Find where/ how it is convenient to place the camera.
- Transmit camera data to PC
- Optimize depth estimation pipeline (model, processing, depth to motor intensity conversion etc) to run in real time. ( What is the effect of different estimations per seconds on perceived accuracy?)



### Combine the two

- Assemble glove.
- Transmit data serially (or wirelessly) between processing backend and haptic glove
- Start user testing.

### Extension:

- Make glove wireless.
- Make glove battery powered.
- Try 3d reconstruction of space and handling VR objects


## 9. Related Work

### 9.a. Papers

List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).

### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

### 9.c. Software

List softwate that you have identified and plan to use. Provide references (with full citation in the References section below).

## 10. References

[1](https://www.researchgate.net/publication/254005210_SpaceSense_Representing_Geographical_Information_to_Visually_Impaired_People_Using_Spatial_Tactile_Feedback) Yatani, K., Banovic, N., & Truong, K. (2012, May). SpaceSense: representing geographical information to visually impaired people using spatial tactile feedback. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 415-424).

[2](https://pubmed.ncbi.nlm.nih.gov/32446757/) Jimenez, M. F., Mello, R. C., Bastos, T., & Frizera, A. (2020). Assistive locomotion device with haptic feedback for guiding visually impaired people. Medical Engineering & Physics, 80, 18-25.

[3](https://dspace.mit.edu/bitstream/handle/1721.1/114285/Katzschmann%20et%20al.%20-%202018%20-%20Safe%20Local%20Navigation%20for%20Visually%20Impaired%20Users%20with%20a%20Time-of-Flight%20and%20Haptic%20Feedback%20Device%20-%20Final.pdf)  Katzschmann, R. K., Araki, B., & Rus, D. (2018). Safe local navigation for visually impaired users with a time-of-flight and haptic feedback device. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 26(3), 583-593.

[4](https://www.researchgate.net/publication/325468302_Navigation_for_Visually_Impaired_Using_Haptic_Feedback) Fagernes, S., & Grønli, T. M. (2018). Navigation for visually impaired using haptic feedback. In Human-Computer Interaction. Interaction in Context: 20th International Conference, HCI International 2018, Las Vegas, NV, USA, July 15–20, 2018, Proceedings, Part II 20 (pp. 347-356). Springer International Publishing.

[5](https://dl.acm.org/doi/10.1145/3411764.3445676) Huppert, F., Hoelzl, G., & Kranz, M. (2021, May). GuideCopter-A precise drone-based haptic guidance interface for blind or visually impaired people. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (pp. 1-14).

[6](https://www.sciencedirect.com/science/article/pii/S1071581907001012) Lahav, O., & Mioduser, D. (2008). Haptic-feedback support for cognitive mapping of unknown spaces by people who are blind. International Journal of Human-Computer Studies, 66(1), 23-35.

[7](https://www.researchgate.net/publication/3338948_Haptic_Rendering_of_Visual_Data_for_the_Visually_Impaired) Moustakas, K., Nikolakis, G., Kostopoulos, K., Tzovaras, D., & Strintzis, M. G. (2007). Haptic rendering of visual data for the visually impaired. IEEE MultiMedia, 14(1), 62-72.

[8](https://www.researchgate.net/publication/263195992_A_remote_guidance_system_for_blind_and_visually_impaired_people_via_vibrotactile_haptic_feedback) Scheggi, S., Talarico, A., & Prattichizzo, D. (2014, June). A remote guidance system for blind and visually impaired people via vibrotactile haptic feedback. In 22nd Mediterranean conference on control and automation (pp. 20-23). IEEE.

[9](https://pubmed.ncbi.nlm.nih.gov/31661798/) Zhang, X., Zhang, H., Zhang, L., Zhu, Y., & Hu, F. (2019). Double-diamond model-based orientation guidance in wearable human–machine navigation systems for blind and visually impaired people. Sensors, 19(21), 4670.

[10](https://www.researchgate.net/publication/342835249_Smartphone_Navigation_Support_for_Blind_and_Visually_Impaired_People_-_A_Comprehensive_Analysis_of_Potentials_and_Opportunities) Kuriakose, B., Shrestha, R., & Sandnes, F. E. (2020, July). Smartphone navigation support for blind and visually impaired people-a comprehensive analysis of potentials and opportunities. In Universal Access in Human-Computer Interaction. Applications and Practice: 14th International Conference, UAHCI 2020, Held as Part of the 22nd HCI International Conference, HCII 2020, Copenhagen, Denmark, July 19–24, 2020, Proceedings, Part II (pp. 568-583). Cham: Springer International Publishing.

[11](https://link.springer.com/article/10.1007/s00371-006-0032-4) Cardin, S., Thalmann, D., & Vexo, F. (2007). A wearable system for mobility improvement of visually impaired people. The Visual Computer, 23, 109-118.

[12](https://staff.www.ltu.se/~kalevi/References/Evaluation%20of%20electronic%20haptic%20device%20for%20blind%20and%20visually%20impaired%20people%20A%20case%20study.pdf) Ramirez, A. R. G., da Silva, R. F. L., Cinelli, M. J., & de Albornoz, A. D. C. (2012). Evaluation of electronic haptic device for blind and visually impaired people: a case study. Journal of Medical and Biological Engineering, 32(6), 423-428.

[13](https://makeabilitylab.cs.washington.edu/media/publications/He_PneufetchSupportingBlindAndVisuallyImpairedPeopleToFetchNearbyObjectsViaLightHapticCues_CHI2020.pdf) He, L., Wang, R., & Xu, X. (2020, April). PneuFetch: supporting blind and visually impaired people to fetch nearby objects via light haptic cues. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems (pp. 1-9).

[14](https://decibel.fi.muni.cz/download/papers/pokluda03.pdf) Pokluda, L., & Sochor, J. (2003). Spatial haptic orientation for visually impaired people. EG, 3, 29-34.

[15](https://www.researchgate.net/publication/326050483_Vibratory_Haptic_feedback_assistive_device_for_visually-impaired_drivers) Wi, D., Sodemann, A., & Chicci, R. (2017, August). Vibratory haptic feedback assistive device for visually-impaired drivers. In 2017 IEEE SmartWorld, Ubiquitous Intelligence & Computing, Advanced & Trusted Computed, Scalable Computing & Communications, Cloud & Big Data Computing, Internet of People and Smart City Innovation (SmartWorld/SCALCOM/UIC/ATC/CBDCom/IOP/SCI) (pp. 1-5). IEEE.

[16](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7543741&tag=1) Poggi, M., & Mattoccia, S. (2016, June). A wearable mobility aid for the visually impaired based on embedded 3D vision and deep learning. In 2016 IEEE symposium on computers and communication (ISCC) (pp. 208-213). IEEE.

[17](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7010003) Xiao, J., Joseph, S. L., Zhang, X., Li, B., Li, X., & Zhang, J. (2015). An assistive navigation framework for the visually impaired. IEEE transactions on human-machine systems, 45(5), 635-640.

[18](https://www.researchgate.net/publication/221311676_Body_Mounted_Vision_System_For_Visually_Impaired_Outdoor_And_Indoor_Wayfindind_Assistance) Treuillet, S., Royer, E., Chateau, T., Dhome, M., & Lavest, J. M. (2007, August). Body Mounted Vision System for Visually Impaired Outdoor and Indoor Wayfinding Assistance. In CVHI.

[19](https://link.springer.com/article/10.1007/s10514-006-7223-8) Kulyukin, V., Gharpure, C., Nicholson, J., & Osborne, G. (2006). Robot-assisted wayfinding for the visually impaired in structured indoor environments. Autonomous robots, 21, 29-41.

[20](https://dl.acm.org/doi/abs/10.1109/ROBIO.2016.7866366) Zhang, H., & Ye, C. (2016, December). An indoor navigation aid for the visually impaired. In 2016 IEEE international conference on robotics and biomimetics (ROBIO) (pp. 467-472). IEEE.

[21](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9216032) Yang, G., & Saniie, J. (2020). Sight-to-sound human-machine interface for guiding and navigating visually impaired people. IEEE Access, 8, 185416-185428.

[22](https://link.springer.com/chapter/10.1007/978-3-642-23768-3_88) Zöllner, M., Huber, S., Jetter, H. C., & Reiterer, H. (2011). NAVI–a proof-of-concept of a mobile navigational aid for visually impaired based on the microsoft kinect. In Human-Computer Interaction–INTERACT 2011: 13th IFIP TC 13 International Conference, Lisbon, Portugal, September 5-9, 2011, Proceedings, Part IV 13 (pp. 584-587). Springer Berlin Heidelberg.

[23](https://www.researchgate.net/publication/257736351_Navigation_and_space_perception_assistance_for_the_visually_impaired_The_NAVIG_project) Kammoun, S., Parseihian, G., Gutierrez, O., Brilhault, A., Serpa, A., Raynal, M., ... & Jouffrais, C. (2012). Navigation and space perception assistance for the visually impaired: The NAVIG project. Irbm, 33(2), 182-189.

[24](https://www.mdpi.com/2079-9292/8/6/697) Bai, J., Liu, Z., Lin, Y., Li, Y., Lian, S., & Liu, D. (2019). Wearable travel aid for environment perception and navigation of visually impaired people. Electronics, 8(6), 697.

[25](https://pubmed.ncbi.nlm.nih.gov/30774566/) Li, B., Munoz, J. P., Rong, X., Chen, Q., Xiao, J., Tian, Y., ... & Yousuf, M. (2018). Vision-based mobile indoor assistive navigation aid for blind people. IEEE transactions on mobile computing, 18(3), 702-714.

[26](https://hal.science/hal-03351798/document) Gay, S. L., Pissaloux, E., Romeo, K., & Truong, N. T. (2021). F2T: a novel force-feedback haptic architecture delivering 2D data to visually impaired people. IEEE Access, 9, 94901-94911.

[27](https://arxiv.org/abs/2201.04453) Zahn, M., & Khan, A. A. (2022). Obstacle avoidance for blind people using a 3D camera and a haptic feedback sleeve. arXiv preprint arXiv:2201.04453.

[28](https://journals.sagepub.com/doi/10.1177/0145482X0309701007) Zelek, J. S., Bromley, S., Asmar, D., & Thompson, D. (2003). A haptic glove as a tactile-vision sensory substitution for wayfinding. Journal of Visual Impairment & Blindness, 97(10), 621-632.

[29](https://dl.acm.org/doi/abs/10.1145/2049536.2049628) Shrewsbury, B. T. (2011, October). Providing haptic feedback using the kinect. In The proceedings of the 13th international ACM SIGACCESS conference on Computers and accessibility (pp. 321-322).

[30](https://dl.acm.org/doi/10.1145/2513383.2513423) Shen, H., Edwards, O., Miele, J., & Coughlan, J. M. (2013, October). CamIO: a 3D computer vision system enabling audio/haptic interaction with physical objects by blind users. In Proceedings of the 15th International ACM SIGACCESS Conference on Computers and Accessibility (pp. 1-2).

[31](https://www.sciencedirect.com/science/article/pii/S0167865519300881) Bauer, Z., Dominguez, A., Cruz, E., Gomez-Donoso, F., Orts-Escolano, S., & Cazorla, M. (2020). Enhancing perception for the visually impaired with deep learning techniques and low-cost wearable sensors. Pattern recognition letters, 137, 27-36.

[32](https://www.researchgate.net/publication/264192906_A_Kinect_based_Vibrotactile_Feedback_System_to_Assist_the_Visually_Impaired) Yelamarthi, K., DeJong, B. P., & Laubhan, K. (2014, August). A kinect based vibrotactile feedback system to assist the visually impaired. In 2014 IEEE 57th International Midwest Symposium on Circuits and Systems (MWSCAS) (pp. 635-638). IEEE.

[33](https://pubmed.ncbi.nlm.nih.gov/2026426/) Kaczmarek, K. A., Webster, J. G., Bach-y-Rita, P., & Tompkins, W. J. (1991). Electrotactile and vibrotactile displays for sensory substitution systems. IEEE transactions on biomedical engineering, 38(1), 1-16.

[34](https://pdfs.semanticscholar.org/06c1/926b0c793d6be8537534c48518e40fc2cb58.pdf) Ribani, R., & Marengoni, M. (2019, January). Vision Substitution with Object Detection and Vibrotactile Stimulus. In VISIGRAPP (4: VISAPP) (pp. 584-590).

[35](https://pubmed.ncbi.nlm.nih.gov/14643370/) Bach-y-Rita, P., & Kercel, S. W. (2003). Sensory substitution and the human–machine interface. Trends in cognitive sciences, 7(12), 541-546.

[36](https://pubmed.ncbi.nlm.nih.gov/30440276/) Mante, N., & Weiland, J. D. (2018, July). Visually impaired users can locate and grasp objects under the guidance of computer vision and non-visual feedback. In 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (pp. 1-4). IEEE.

[37](https://www.researchgate.net/publication/224586228_Vibrotactile_feedback_systems_Current_trends_in_rehabilitation_sports_and_information_display) Alahakone, A. U., & Senanayake, S. A. (2009, July). Vibrotactile feedback systems: Current trends in rehabilitation, sports and information display. In 2009 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (pp. 1148-1153). IEEE.

[38](https://www.researchgate.net/publication/355410847_Vibrotactile_Data_Physicalization_Exploratory_Insights_for_Haptization_of_Low-resolution_Images) Bastidas Cuya, F. G., Martins Guarese, R. L., Johansson, C. G., Giambastiani, M., Iquiapaza, Y., de Jesus Oliveira, V. A., ... & Maciel, A. (2021, October). Vibrotactile Data Physicalization: Exploratory Insights for Haptization of Low-resolution Images. In Symposium on Virtual and Augmented Reality (pp. 84-91).

# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

Provide a brief overview of the project objectives, approach, and results.

# 1. Introduction

* Motivation & Objective:
Globally, there are approximately 284 million people in the visually impaired (VI) community with 39 million among them facing blindness. Navigational difficulties, locating misplaced items, and accessing objects beyond their immediate reach are common challenges a visually impaired encounters.
Findings show a critical consideration in the design and development of technologies for visually impaired individuals. The preference of VI people in the adoption of such devices depends on factors like affordability, portability, and integration into existing devices.
- Cost-Effective Solutions: expensive devices are a barrier to widespread technology and a balance between functionality and affordability makes them accessible to a broader range of population.
- Lightweight Design: Users have a better experience with devices that are lightweight as heavy gadgets are impractical for everyday use. Designs that prioritize simplicity align with the need for easy-to-carry solutions.
- Integration with Existing Tools: A notable preference is for devices that integrate with tools visually impaired individuals already use, such as canes, guide dogs, or smartphones. Rather than introducing standalone devices, the goal is to enhance existing aids, ensuring that users are able to use new technologies without additional effort or requiring any adjustment.
Users express a particular interest in solutions that can be integrated directly into their smartphones. This is convenient, as individuals are more likely to carry these items regularly.
- User-Friendly: Visually impaired individuals prefer devices that are easy to operate and do not require complex instructions or learning processes. 

* State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
* Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
* Challenges: What are the challenges and risks?
* Requirements for Success: What skills and resources are necessary to perform the project?
* Metrics of Success: What are metrics by which you would check for success?





# 2. Related Work

# 3. Technical Approach
The design of our glove encompasses two fundamental aspects: the mechanical and hardware components. 

In focusing on the mechanical aspect, placing multiple vibration motors at precise locations on the glove, and aligning them with the skin's sensitivity on the palm was the taken approach to optimize the user experience. The objective is to create a sense of realistic feedback for the user, therefore the number of vibration motors is maximized.
Moreover, the design needs the integration of two circuits, each serving a distinct function. One circuit is dedicated to providing instructions to the vibration motors, orchestrating dynamic feedback. The other circuit is responsible for supplying the power to drive the motors, ensuring a consistent user experience.
Considering the wiring challenges associated with such a setup, we designed a PCB (Printed Circuit Board) to connect the motors and their drivers. This PCB serves as the central hub, connecting the vibration motors and their corresponding drivers.
The location of the camera was another dilemma in our design consideration. As originally intended, it was supposed to be connected to the user's body. However, by relocating the camera to the palm, we eliminated the need to determine the depth relative to the hand, thereby simplifying the entire system. Placing the camera on the palm allows for a more natural interaction with the environment.

From the electronic perspective, the vibrating mini motors that we are using for haptic feedback demand approximately 100 mA of current to achieve optimal rotation at 5V power. Given that the processor’s output pins cannot supply this current, a dedicated driver circuit is essential for powering the motor through a PWM (Pulse Width Modulation) signal. Therefore, we are using NPN transistors with bases connected to the processor pins functioning as a dynamic voltage-controlled current source, to supply the necessary current for motors to work in their optimal operational range. A PWM signal modulates the current supplied to the motors through this configuration, enabling the processor to control the transistors. In addition to meeting the motor's power requirements, this also provides us with haptic feedback because it gives us control over the motor's power.

# 4. Evaluation and Results

# 5. Discussion and Conclusions

# 6. References

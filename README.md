# AIDD
AI Dolphin Deter
![image](https://github.com/LabMACS/MAXFISH_Simulator/assets/64741263/17e16013-9c0a-459e-b3f7-c2a549fa2d81) ![image](https://github.com/LabMACS/MAXFISH_Simulator/assets/64741263/45443654-a834-47ae-9590-ab8ababafb62)


# Table of contents
1. [Preface](#preface)
2. [Installation](#installation)
    1. [Requirements](#requirements)
    2. [Run the simulation](#run)
3. [Legal](#legal)
    1. [Credits](#credits)
    2. [License](#license)
     

## Preface <a name="preface"></a>
This project includes a MAXFISH simulator for MATLAB/ Simulink and a GUI application. The goal is to provide an advanced and controllable tool that can simulate in precise detail the NGC system of a robotic bio-inspired fish.

The simulator allows for the execution of programmed trajectories and for analysis of the fish's dynamic behavior. It deals with the mathematical model of kinematics and dynamics, as well as the propulsion system and NGC system, including line of sight guidance law and path following control system using PID, creating an accurate virtual model of the fish, through the 3D World Editor (native VRML editor), which is included in the Simulink 3D Animation. This enables the identification of potential issues, optimization of performance, and evaluation of the system's robustness in a detailed and controlled manner.

The application facilitates users to simulate and analyze data with greater control. Its intuitive interface allows for modification of physical parameters of the fish, such as masses and component lengths, and to start the desired simulation. The application GUI performs several tasks, including importing model parameters from an Excel file, starting the simulation of the Simulink model, plotting variables of interest in the simulation, plotting the trajectory taken by MAXFISH and the desired trajectory.
![image](https://github.com/LabMACS/MAXFISH_Simulator/assets/64741263/4f95ff26-68b8-44e9-a83c-e53748c2be8b)


  
***For further information about the Simulink model and parameters, please look at the [user manual](Documentation/user_manual.docx).***

## Installation <a name="installation"></a>
### Requirements <a name="requirements"></a>
* MATLAB version R2023b or newer. **Older versions may not ensure proper functioning of the simulator**.
* The following add-ons in MATLAB:
  * [DSP System Toolbox](https://it.mathworks.com/products/dsp-system.html)
  * [Signal Processing Toolbox](https://it.mathworks.com/products/signal.html)
  * [Simulink 3D Animation](https://it.mathworks.com/products/3d-animation.html)
  * [Vehicle Dynamics Blockset](https://it.mathworks.com/products/vehicle-dynamics.html)
  
### Run the simulation <a name="run"></a>
In the MAXFISH folder, the file â€œ_App.mlapp_â€ opens the GUI application. To change the parameters of the simulation, it is necessary to modify the Excel file â€œ_data.xlsx_â€. 

The interface of the application includes two buttons: '_Load Parameters_' to import data from an Excel file and '_Run Simulation_' to initiate the simulation. Once the simulation has started, the behaviour of the digital fish and the 2D kinematics of the tail can be observed. By selecting the relevant tab in the app, itâ€™s possible to display the position, orientation, linear velocities, and angular velocities graphs of the fish, graph of all actuators, including the frequency and bias control of the fish's tail, as well as the effective trajectory compared to the desired one. 

## Legal <a name="legal"></a>
### Credits <a name="credits"></a>
If you have any suggestions or comments related to this simulator, please contact:
* **Project Leader**: [David Scaradozzi](mailto:d.scaradozzi@staff.univpm.it)
* **Project Developer**: [Flavia Gioiello](mailto:f.gioiello@staff.univpm.it)

*LabMACS, DII, UniversitÃ  Politecnica delle Marche, Via Brecce Bianche, 12, Ancona, 60131, Italy*

[https://www.labmacs.university/](https://www.labmacs.university/)

### License <a name="license"></a>
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

To acknowledge the material, the following information must be reported:
* Attribution: MAXFISH PRIN project (20225RYMJE)
             <[https://www.maxfish.it/](https://www.maxfish.it/)> 
* Title of the Work: â€œMAXFISH Matlab/Simulink Simulatorâ€
* Source: [https://www.labmacs.university/maxfish-simulator/](https://www.labmacs.university/maxfish-simulator/)
* License information: CC BY-NC-SA 4.0

The â€œMAXFISH Matlab/Simulink Simulatorâ€ is free available.


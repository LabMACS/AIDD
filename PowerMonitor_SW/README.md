# Monitoring of Power Consumption
Software for the monitoring of A.I.D.D. power consumption.

<p float="left">
<img src="https://github.com/LabMACS/AIDD/blob/main/images/Extended_Logo.png" width="85" height="85">
<img src="https://github.com/LabMACS/AIDD/blob/main/images/CNR-IRBIM_colori.png" width="380" height="120">
<img src="https://github.com/LabMACS/AIDD/blob/main/images/ANcyb_300DPIOK.png"width="380" height="120">
</p>

# Table of contents
1. [Preface](#preface)
2. [Legal](#legal)
    1. [Credits](#credits)
    2. [Funding](#funding) 
    3. [License](#license)
     

## Preface <a name="preface"></a>
The enclosed routine (INA_219_Logger) is designed to provide an estimation of the power consumption of the A.I.D.D. device using a 12-bit I2C output digital power monitor, the INA219 sensor. The sensor was connected to a monitoring system based on a Raspberry Pi 3 Model A running Python sampling software. This setup acquires the voltage and current supplied to the A.I.D.D. system and classifies seven different operating stages: 

1.	Data read from audio device 
2.	STFT process
3.	Image conversion (Plot)
4.	CNN inference
5.	Data logging (in case of positive events)
6.	Sleep mode (waiting for the timestep of 0.4s)
7.	Start-up of the environment

The running states were transmitted from the Raspberry Pi Zero 2 W of the device to the monitoring Raspberry Pi 3 Model A via a three-wire GPIO connection (using GPIO pins 27, 17, and 22). These pins encoded the current running stage as a 3-bit integer value. The trials were conducted using the same criteria as in the previous section (Real-time software validation). 

  
***
For further information about the project, model and parameters, please look at 
- https://www.irbim.cnr.it/progetto-dettagli/life-delfi/
- Francesco Di Nardo, David Scaradozzi, Rocco De Marco, Laura Screpanti, and Alessandro Lucchetti, Intelligent identification of dolphin whistle in acoustic signals via convolutional neural networks, Science Advances, Submitted
***


## Legal <a name="legal"></a>
### Credits <a name="credits"></a>
If you have any suggestions or comments related to this software, please contact:
* **Project Leader**: [David Scaradozzi](mailto:d.scaradozzi@univpm.it)
* **Project Developer**: [Rocco De Marco](mailto:rocco.demarco@cnr.it)
* **Project Developer**: [Francesco Di Nardo](mailto:f.dinardo@univpm.it)

- *LabMACS, DII, UniversitÃ  Politecnica delle Marche, Via Brecce Bianche, 12, Ancona, 60131, Italy*
- *Institute of Biological Resources and Marine Biotechnology (IRBIM), National Research Council (CNR), Ancona, Italy.*
- *ANcybernetics, Università Politecnica delle Marche, Ancona, Italy.*

[https://www.labmacs.university/](https://www.labmacs.university/)

### Funding <a name="funding"></a> 
This work was supported in part by LIFE Financial Instrument of the European Community, Life Delfi Project – Dolphin Experience: Lowering Fishing Interactions (LIFE18NAT/IT/000942) and by the National Recovery and Resilience Plan (NRRP), Mission 4 Component 2 Investment 1.4 (Call for tender No. 3138 of 16 December 2021, rectified by Decree n.3175 of 18 December 2021 of Italian Ministry of University and Research funded by the European Union) NextGenerationEU.

### License <a name="license"></a>
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

To acknowledge the material, the following information must be reported:
* Attribution: DELFI project
             <[https://www.labmacs.university/](https://www.labmacs.university/)> 
* Title of the Work: AIDD - AI Dolphin Deter 
* Source: [https://github.com/LabMACS/AIDD](https://github.com/LabMACS/AIDD)
* License information: CC BY-NC-SA 4.0

The AIDD - AI Dolphin Deter is free available.


# A.I.D.D.
The Artificial Intelligent Dolphin Deterrent: a novel low-cost intelligent robotic system capable of identifying dolphin vocalizations and consequently responding in real-time to dissuade the dolphins from approaching.

<p float="left">
<img src="https://github.com/LabMACS/AIDD/blob/main/images/Extended_Logo.png" width="85" height="85">
<img src="https://github.com/LabMACS/AIDD/blob/main/images/CNR-IRBIM_colori.png" width="380" height="120">
</p>

# Table of contents
1. [Preface](#preface)
2. [Installation](#installation)
    1. [Requirements](#requirements)
    2. [Usage](#run)
3. [Legal](#legal)
    1. [Credits](#credits)
    2. [Funding](#funding) 
    3. [License](#license)
     

## Preface <a name="preface"></a>
Dolphin bycatch and depredation in commercial fisheries pose serious ecological and socio-economic challenges, often resulting in injury or death of non-target marine mammals and financial loss for fishers. Conventional mitigation strategies, including static acoustic deterrent devices (pingers), have shown limited long-term efficacy due to habituation, non-selective operation, and environmental side effects. In this repository, we introduce the Artificial Intelligent Dolphin Deterrent (A.I.D.D.), a novel low-cost mechatronic system designed to reduce dolphin bycatch through underwater acoustic sensing, real-time machine learning, and programmable deterrent emissions.The device features a hydrophone-based acquisition unit, a Raspberry Pi Zero 2 W for onboard processing, and a dual-function acquisition/emitter system powered by a customized preamplifier and amplifier chain. The computational core of the system is a convolutional neural network (CNN) optimized with TensorFlow Lite to detect dolphin whistles and trigger deterrent sounds only upon verified presence
This repository provides:

    The complete Electronic Scheme of A.I.D.D.

    An advanced version of the convolutional neural network (CNN) optimized with TensorFlow Lite

    The Electronic scheme of the Power Monitoring module and its calculation software

    STL files for 3D printing the hydrophone

A.I.D.D. is a low-cost, fully replicable, and customizable solution that aims to make intelligent bycatch mitigation technologies accessible, representing a promising step toward sustainable and intelligent fishery practices.
  
***
For further information about the project and the A.I.D.D., please look at 
- https://www.irbim.cnr.it/progetto-dettagli/life-delfi/
- Francesco Di Nardo,  Rocco De Marco, Daniele Costa, Alessandro Lucchetti, and David Scaradozzi. A.I.D.D.: A Low-Cost, AI Powered, Acoustic Deterrent to Prevent Dolphin Bycatch and Depredation, Submitted to Science Robotics, July 2025.
- Rocco De Marco, Francesco Di Nardo, Alessandro Rongoni, Laura Screpanti, and David Scaradozzi. Real-Time Dolphin Whistle Detection on Raspberry Pi Zero 2 W with a TFLite Convolutional Neural Network. Robotics 2025, 14, 67. https://doi.org/10.3390/robotics14050067
- David Scaradozzi, Rocco de Marco, Daniel Li Veli, Alessandro Lucchetti, Laura Screpanti, and Francesco Di Nardo, Convolutional Neural Networks for Enhancing Detection of Dolphin Whistles in a Dense Acoustic Environment. IEEE Access, 2024, 12, 127141-127148.  doi: 10.1109/ACCESS.2024.3454815
- Rocco De Marco, Francesco Di Nardo, Alessandro Lucchetti, Massimo Virgili, Andrea Petetta, Daniel Li Veli, Laura Screpanti, Veronica Bartolucci, David Scaradozzi. The Development of a Low-Cost Hydrophone for Passive Acoustic Monitoring of Dolphin’s Vocalizations. Remote Sensing. 2023, 15, 1946. https://doi.org/10.3390/rs15071946
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


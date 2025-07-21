# A.I.D.D. Electronic schemes
AI Dolphin Deter: Basic algorithm to test the functionality of the CNN model trained to recognize bottlenose dolphin whistles.

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
This section contains the electronic schemes developed for A.I.D.D. The "main board" fold includes the schematics, PCB, and Gerber files of the main device which connects each specialised module composing the A.I.D.D. This board presents two 40-pins socket connector to mount the Raspberry Pi Zero 2 W and the high-quality audio expansion board, the HiFiBerry DAC+ADC Pro. The boards allows to connect the customized preamplifier ()


  
***
For further information about the project, model and parameters, please look at 
- https://www.irbim.cnr.it/progetto-dettagli/life-delfi/
- Francesco Di Nardo, David Scaradozzi, Rocco De Marco, Laura Screpanti, and Alessandro Lucchetti, Intelligent identification of dolphin whistle in acoustic signals via convolutional neural networks, Science Advances, Submitted
***

## Installation <a name="installation"></a>
### Requirements <a name="requirements"></a>
* TbD 
  
### Usage <a name="run"></a>
This simple application requires that spectrograms be prepared by applying a Sobel vertical filter and saved in PNG format with a resolution of 300x150 pixels. Files containing whistles should have filenames starting with POS, otherwise NEG. All these files should be saved in a folder named "sobel". Please note: a sample trained model is available in "Release"

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


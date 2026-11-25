

# Selecting ICA components manually

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Marks ICA components for exclusion in an MNE ICA object and saves it with a plot of the components (MNE-Python).**

Reads an MNE ICA solution, sets ica.exclude and saves the updated ICA file with a topography plot of the components. Use it to record which artefact components should be removed before applying ICA to MEG/EEG data. Warning: on this branch the excluded components are hard-coded to [0, 1] and the exclude parameter is not read.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/ica` |
| 📤 **Outputs** | `neuro/meeg/mne/ica` · `generic/image/png` |
| 🐳 **Container** | `brainlife/mne:1.0.2` |
| ⚙️ **Resources** | 8 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.678](https://doi.org/10.25663/brainlife.app.678) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `ica` | `neuro/meeg/mne/ica` | yes | MNE ICA solution file (ica.fif). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/ica` | ICA file (ica.fif) with the excluded components set. |
| `out_figs` | `generic/image/png` | Plot of the ICA component topographies (ica.png). |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `exclude` | number |  | Intended indices of the ICA components to exclude; currently not read by main.py (components 0 and 1 are always excluded). |

</details>

📚 **References used by this App:**
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7(267):1-13 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.530-blue.svg)](https://doi.org/10.25663/brainlife.app.530)

Brainlife App to inorder to exclude ICA components manually based on `ica.exclude`.

## app-selecting-ICA-components-manually
 documentation

2) Input file is:
    * components to be excluded
    * `ica/fif` ica object file
5) Ouput files are:
    * `ica/fif` ica object file which included the indices to be execluded 
   
   

## Authors
- Saeed ZAHRAN(saeedzahranutc@gmail.com)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*- brainlife.io Publishing and Apps:*

Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

*- MNE-Python package:* 

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  **MEG and EEG data analysis with MNE-Python**. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University

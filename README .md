# Experimental Tasks for the 10 Hz rTMS vs iTBS RCT in Adolescent Depression

This repository contains computerized experimental tasks used in a randomized controlled trial comparing 10 Hz rTMS and iTBS in adolescents with major depressive disorder.

## Trial Registration

- Registration No.: [to be added]
- Ethics Approval: Ethics Committee of Shandong Mental Health Center (KYSJWLL2025-1-019)

---

## Overview

| Category | Task | Platform |
|---|---|---|
| Clinical Questionnaires | CDI, MASC, PSQI |Python v.3.11.7 |
| Cognitive Tasks | Spatial N-back | Python v.3.11.7  |
|  | Wisconsin Card Sorting Test (WCST) | Python v.3.11.7  |
|  | Balloon Analog Risk Task (BART) | Python v.3.11.7  |
| fMRI Task | Simple Guessing Task | PsychoPy (builder) v.2022.2.5 |

### Python requirements
|Package Index | Version |
|---|---|
|Pandas| 2.2.1 |
|numpy | 1.23.5 | 
|pygame |2.5.2 | 
| PsychoPy (PyPI)  | 2023.1.3 |
| pypinyin | 0.51.0 |
| matplotlib | 3.8.3 |
| fpdf2 | 2.7.8 |

---

## Clinical Self-Report Questionnaires

### Children's Depression Inventory (CDI)
### Multidimensional Anxiety Scale for Children (MASC)
### Pittsburgh Sleep Quality Index (PSQI)

Self-report scales implemented in PsychoPy to ensure standardized, computerized administration.

---

## Cognitive Tasks

### 1. Spatial N-back Task

Assesses working memory. Participants judge whether the current spatial position of an orange square matches the position N steps earlier. Three difficulty levels: 1-back, 2-back, 3-back.

### 2. Wisconsin Card Sorting Test (WCST)

Assesses executive function. Participants match cards to stimulus cards by color, shape, or number. The sorting rule changes unpredictably after each block of consecutive correct responses. Records reaction time, accuracy, perseverative errors, and completed categories.

### 3. Balloon Analog Risk Task (BART)

Assesses risk-taking behavior. Participants inflate virtual balloons to earn rewards; each pump increases both potential gain and explosion risk. Three balloon types with different explosion probabilities. Primary index: number of pumps per trial.

---

## fMRI Task

### Simple Guessing Task

A reward-processing fMRI paradigm. Participants select one of two doors in each trial and receive win/loss feedback. Includes high-reward and low-reward conditions, designed to assess neural responses during reward anticipation and outcome processing.

---

## Repository Structure

```
├── questionnaires/
│   ├── cdi/
│   ├── masc/
│   └── psqi/
├── cognitive_tasks/
│   ├── n_back/
│   ├── wcst/
│   └── bart/
├── fmri_tasks/
│   └── guessing_task/
├── README.md
├── README_CN.md
└── LICENSE
```

## Requirements

- PsychoPy ≥ [version]
- Python ≥ [version]

## Citation

If you use these tasks, please cite our study protocol:

> Tian X, Sun H, Li X, et al. A randomized controlled trial protocol comparing 10 Hz rTMS and iTBS for adolescent depression: clinical efficacy, neurocognitive and neurobiological mechanisms. [to be added]

## Contact

- Corresponding Author: [name to be added]
- Email: [email to be added]

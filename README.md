
# Evaluating the Impact of Lab Test Results on Large Language Models Generated Differential Diagnoses from Clinical Case Vignettes

**Authors:**  
Balu Bhasuran, PhD<sup>1</sup>, Qiao Jin, MD<sup>2</sup>, Yuzhang Xie, MS<sup>3</sup>, Carl Yang, PhD<sup>3</sup>, Karim Hanna, MD<sup>4</sup>, Jennifer Costa, MD<sup>4</sup>, Cindy Shavor, MD<sup>4</sup>, Zhiyong Lu, PhD<sup>2</sup>, Zhe He, PhD<sup>1</sup>  
<sup>1</sup> Florida State University, Tallahassee, FL  
<sup>2</sup> National Library of Medicine, Bethesda, MD  
<sup>3</sup> Emory University, Atlanta, GA  
<sup>4</sup> Morsani College of Medicine, University of South Florida, Tampa, FL  

---

## Introduction

This repository contains code and datasets for the study titled **"Evaluating the Impact of Lab Test Results on Large Language Models Generated Differential Diagnoses from Clinical Case Vignettes."** The research aims to assess how laboratory test results influence the accuracy of differential diagnosis (DDx) generated by large language models (LLMs) using clinical case reports.

### Study Overview

- **Dataset:** A set of 50 clinical case reports was collected from PubMed Central (PMC). Each report was transformed into a vignette format that includes patient age, gender, symptoms, and lab test results.
  
- **Models Evaluated:**
  - GPT-4
  - GPT-3.5
  - Llama-2-70b
  - Claude-2
  - Mixtral-8x7B
  
- **Evaluation Metrics:** Models were evaluated based on their ability to generate the Top 10, Top 5, and Top 1 differential diagnoses both with and without lab test results.

### Key Results

- **GPT-4** demonstrated the highest performance, achieving:
  - 55% accuracy for Top 1 diagnoses with lab results.
  - 60% accuracy for Top 10 diagnoses with lab results.
  - 80% lenient accuracy for differential diagnoses.
  
- **Mixtral** also performed well with a 60% accuracy rate for Top 5 diagnoses when lab results were included.

- The inclusion of lab results improved diagnostic accuracy across all evaluated models.

- Despite the improvements, exact match rates for diagnoses were relatively low, indicating that LLMs excel in generating relevant differential diagnoses but often fall short of perfect matches.

---

## PMC-Patients Dataset

**PMC-Patients** is a large-scale dataset used in this study to benchmark retrieval-based clinical decision support systems. The dataset contains:

- 167k patient summaries from PubMed Central.
- 3.1 million annotated relevant articles.
- 293k similar patients, defined by citation relationships from PubMed.

### Download and Contribution

You can download the **PMC-Patients** dataset from the following link:  
[https://pmc-patients.github.io/](https://pmc-patients.github.io/)

---

## Repository Contents

- `notebooks/`: Contains the Jupyter notebooks used for data preprocessing, model evaluation, and result analysis.
- `data/`: Sample case vignettes and instructions on how to process the complete dataset.
- `scripts/`: Python scripts for running differential diagnosis predictions with the evaluated LLMs.
- `requirements.txt`: List of required dependencies to replicate the experiments.
  
---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/balubhasuran/DDx_CaseReports.git
   cd DDx_CaseReports
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebooks for evaluating the differential diagnoses:
   ```bash
   jupyter notebook
   ```

---

## Citation

Please cite this repository if you use the dataset or models in your research:

```
@article{bhasuran2024impact,
  title={Evaluating the Impact of Lab Test Results on Large Language Models Generated Differential Diagnoses from Clinical Case Vignettes},
  author={Bhasuran, Balu and Jin, Qiao and Xie, Yuzhang and Yang, Carl and Hanna, Karim and Costa, Jennifer and Shavor, Cindy and Lu, Zhiyong and He, Zhe},
  journal={Unpublished manuscript},
  year={2024}
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

If you have any questions, please feel free to open an issue or contact the authors.

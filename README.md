
<p align="center">
  <img height="140" src="./img/logo3.png" />
</p>

---

## What is BioAI ？

**BioAI** is a library built upon scikit-learn and PyTorch to easily write and train machine learning or deep learning models for biological omics data.  

---

## What can BioAI do for you ?


---

## What is the scope of BioAI ?

**BioAI** is designed for fast and easy building of machine/deep learning models for bioinformatics. It can handle arbitrarily formatted omics datasets. 

The methods currently integrated by BioAI are all supervised learning, which means that you need to provide training examples for your application. These methods are all derived from published articles. Collectively, these methods enable **classification** and **regression** tasks such as predicting disease subtypes (classification), predicting generation time (regression).

In terms of data, it supports single-omics and multi-omics integration. Off note, the omics data needs to meet the following structure, that is, each row represents a sample, and each column represents an omics feature, such as a gene or a mutation. An example is as follows:

|            | Gene-A | Gene-B | Gene-C | Gene-D | Gene-E | Gene-F | Gene-G | Gene-H |
| ---        | ---    | ---    | ---    | ---    | ---    | ---    | ---    | ---    |
| patient-1  | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    |
| patient-2  | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    |
| patient-3  | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    |
| patient-4  | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    |
| patient-5  | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    | 0.01    |
| ...  | ...    | ...    | ...    | ...    | ...    | ...    | ...    | ...    |

All data should be saved in `.csv` format, of course you can use `gz` for compression. You can also refer to the [example data](https://github.com/BioAI-kits/BioAI/tree/master/example) we provide for a more intuitive understanding.


---

## How does BioAI work ?


---

## How to get started ?



---

## What algorithms are currently supported?


---

### Data preprocessing


---

### Machine/Deep learning algorithms

| Algorithm | Scope | Task |Paper | 
| --- | --- | -- | --- | 
| Random Forest | single/multi omics | classification/regression | ?? |
| XGBoost | single/multi omics | classification/regression | ?? |
| SVM | single/multi omics | classification/regression | ?? |
| LASSO | single/multi omics | classification/regression | ?? |
| PathGNN | Transcription | classification | Liang B, Gong H, Lu L, et al. Risk stratification and pathway analysis based on graph neural network and interpretable algorithm[J]. BMC bioinformatics, 2022, 23(1): 394. |
| AttentionMOI | multi omics | classification | ?? |







TODO: Introduction 

**BioAI** is a library built upon scikit-learn and PyTorch to easily write and train machine learning or deep learning models for biological omics data.  

It consists of various methods from a variety of published papers. 


[简体中文](https://github.com/BioAI-kits/BioAI/blob/master/README-Zh.md)



--- 



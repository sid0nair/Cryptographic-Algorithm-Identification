**Work in Progress**

# Cryptographic-Algorithm-Identification
Repository for Cryptographic Algorithm Identification using ML. Implements feature extraction via NIST randomness tests and ensemble learning methods (Random Forest &; Logistic Regression) to classify cryptographic algorithms. Includes Python scripts, dataset, and research references demonstrating enhanced identification accuracy. Work in progress.

## Project Overview

Cryptographic algorithm identification is essential in cryptanalysis, especially when only ciphertext is available. This project extracts unique features from ciphertext using the NIST SP 800-22 randomness tests and applies ensemble learning techniques to improve identification accuracy. The current focus is on classifying algorithms like AES, 3DES, Blowfish, and RC4.

### Key Features
- **Feature Extraction**: NIST randomness tests are employed to gather distinctive features from ciphertext.
- **Modeling**: Ensemble methods, including Hybrid Random Forest and Logistic Regression, are used to build a robust classification model.
- **Research-Based Approach**: This project builds on recent studies in cryptographic identification, ensuring that the approach is grounded in existing research.

## Repository Structure

The repository is organized as follows:

```plaintext
Cryptographic_Algorithm_Identification/
├── data/
│   └── nist_feature_dataset.csv       # Dataset used for training and evaluation
├── docs/
│   ├── research_background/           # Folder containing research PDFs used in this project
│   │   ├── hybrid_Random_forest&logistic_regressor.pdf
│   │   ├── 3DES_8KB_2.pdf
│   │   ├── Cryptographic_Algorithm_Identification_through_Machine_Learning_for_Enhanced_Data_Security.pdf
│   │   └── Machine_Learning_for_Cryptographic_Algorithm_Ident.pdf
├── src/
│   ├── model.py                       # Main model implementation
│   ├── Dataset.py                     # Dataset handling script
│   ├── csv_creator.py                 # Script to generate CSV from data
│   └── run_nist_tests.py              # Script to run NIST randomness tests for feature extraction
├── README.md                          # Project overview and usage instructions
└── requirements.txt                   # Python dependencies
````



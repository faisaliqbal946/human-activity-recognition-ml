# Human Activity Recognition using Machine Learning

This project applies machine learning techniques to classify human activities from time-series sensor data. It uses the `WalkingSittingStanding.ts` dataset and compares classical classification models after preprocessing and dimensionality reduction.

The workflow includes data loading, feature scaling, PCA for dimensionality reduction, model training, and evaluation.

## Key Features

- Loads and processes `.ts` time-series sensor data
- Applies feature scaling and PCA for dimensionality reduction
- Trains and compares multiple classical machine learning models
- Evaluates model performance using standard classification metrics

## Implemented Models

- k-Nearest Neighbors (k-NN)
- Support Vector Machine (SVM)
- Gaussian Naive Bayes

## Technologies Used

- Python
- NumPy
- Matplotlib
- scikit-learn
- PyTorch
- SciPy

## Project Structure

```text
.
|-- Iqbal_Faisal.ipynb          # Main notebook for analysis, training, and evaluation
|-- utils.py                    # Utility function for loading the .ts dataset
|-- WalkingSittingStanding.ts   # Human activity time-series dataset
|-- requirements.txt            # Python dependencies
|-- README.md                   # Project documentation
```

## Installation and Usage

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

Then open and run the notebook:

```bash
jupyter notebook Iqbal_Faisal.ipynb
```

## Results

| Model | Accuracy |
| --- | --- |
| k-NN | To be updated |
| SVM | To be updated |
| Gaussian Naive Bayes | To be updated |

## Notes

The notebook demonstrates a complete machine learning workflow for human activity recognition, including PCA-based dimensionality reduction and evaluation of k-NN, SVM, and Gaussian Naive Bayes classifiers.

## Author

Faisal Iqbal

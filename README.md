# Gender Classification Project

This is a simple data science project aimed at classifying gender based on physical characteristics such as height, weight, and shoe size. The project utilizes popular machine learning classifiers from the scikit-learn library in Python.

## Getting Started

To get started with this project, ensure you have Python installed on your system along with the required dependencies, particularly scikit-learn.

```bash
pip install scikit-learn
```

## Project Structure

- **gender_classification.py**: This is the main Python script containing the code for the gender classification task.
- **README.md**: This file provides an overview of the project, installation instructions, and usage guidelines.

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/gappeah/gender_classification.git
```

2. Navigate to the project directory:

```bash
cd gender-classification
```

3. Run the `demo.py` script:

```bash
python demo.py
```

4. View the predicted gender based on the provided input data.

## Classifier Used

The project utilizes the following machine learning classifiers:

- **Decision Tree Classifier**: `DecisionTreeClassifier` from scikit-learn's `tree` module.
- **K-Nearest Neighbors Classifier**: `KNeighborsClassifier` from scikit-learn's `neighbors` module.
- **Random Forest Classifier**: `RandomForestClassifier` from scikit-learn's `ensemble` module.
- **Support Vector Machine Classifier**: `SVC` from scikit-learn's `svm` module.

## Input Data

The input data consists of physical characteristics represented as a list of lists `x` and corresponding gender labels represented as a list `y`. Each sublist in `x` contains height, weight, and shoe size, while each element in `y` represents the gender (male or female) corresponding to the respective sublist in `x`.

## Example

An example prediction is made using the Decision Tree Classifier for the input `[190, 70, 8]`, where 190 represents height, 70 represents weight, and 8 represents shoe size. The predicted gender is printed to the console.
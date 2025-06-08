# Text Classification with Word Embeddings

## Project Overview
This project implements a text classification system using word embeddings and neural networks. The goal is to effectively train a feedforward neural network for text classification while simultaneously deriving meaningful word embeddings.

## Team Members
- Prahlad Kumar Sahu - 2024ab05083

## Problem Statement
Develop an approach to effectively train a feedforward neural network for text classification while simultaneously deriving meaningful word embeddings.

## Project Structure
```
.
├── README.md
├── requirements.txt
├── setup.py
├── text_classification_embeddings_final.ipynb
└── ScienceTopics.csv
```

## Dataset
The project uses a dataset containing text comments labeled with topics (Biology, Chemistry, Physics). The dataset consists of 8,695 samples with the following distribution:
- Biology: 3,591 samples
- Chemistry: 2,920 samples
- Physics: 2,184 samples

## Methodology

### 1. Data Preparation
- Text preprocessing including tokenization and stopword removal
- Label encoding for topic categories
- Text length analysis and padding sequences
- Train-test split for model evaluation

### 2. Model Architecture
- Feedforward neural network with embedding layer
- Custom word embeddings derived during training
- Dense layers for classification
- Dropout for regularization

### 3. Training Process
- Model training with TensorFlow/Keras
- Hyperparameter tuning
- Performance evaluation using accuracy metrics
- Visualization of results

## Key Features
- Simultaneous word embedding learning and text classification
- Custom preprocessing pipeline
- Neural network architecture optimized for text classification
- Performance analysis and visualization tools

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ps2program/NLP-Text-Classification.git
   cd NLP-Text-Classification
   ```

2. Run the setup script:
   ```bash
   python setup.py
   ```
   This will:
   - Create a virtual environment using Python's built-in `venv`
   - Install all required dependencies from `requirements.txt` using `pip`

3. Activate the virtual environment:
   - On Unix/macOS:
     ```bash
     source ./.venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\.venv\Scripts\activate
     ```

## Dependencies
The project uses the following main dependencies:
- numpy: For numerical computations
- pandas: For data manipulation and analysis
- scikit-learn: For machine learning algorithms
- torch: For deep learning
- transformers: For pre-trained language models
- nltk: For natural language processing
- matplotlib & seaborn: For data visualization
- jupyter & notebook: For running Jupyter notebooks
- tensorflow: For deep learning models

## Project Files
- `text_classification_embeddings_final.ipynb`: Main Jupyter notebook containing the implementation
- `ScienceTopics.csv`: Dataset containing scientific topics for classification
- `setup.py`: Automated setup script for environment and dependencies using `venv` and `pip`
- `requirements.txt`: List of Python package dependencies

## Usage
After setting up the environment, you can run the Jupyter notebook:
```bash
# Activate the virtual environment if not already active
# source ./.venv/bin/activate (Unix/macOS) or .\.venv\Scripts\activate (Windows)

jupyter notebook text_classification_embeddings_final.ipynb
```
Follow the notebook cells to:
- Preprocess the data
- Train the model
- Evaluate performance
- Visualize results

## Results
The model achieves competitive performance in text classification while learning meaningful word embeddings that capture semantic relationships between words in the scientific domain.

## Future Work
- Experiment with different neural network architectures
- Try alternative embedding techniques
- Explore transfer learning approaches
- Apply the model to other text classification tasks

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details. 
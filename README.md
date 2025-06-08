# NLP Text Classification Project

This project focuses on text classification using neural language modeling and embeddings. It includes implementations for processing and classifying scientific topics using various NLP techniques.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── setup.py
├── text_classification_embeddings_final.ipynb
└── ScienceTopics.csv
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install `uv` (if not already installed):
```bash
pip install uv
```

3. Run the setup script:
```bash
python setup.py
```
This will:
- Create a virtual environment using `uv`
- Install all required dependencies from `requirements.txt` using `uv`

4. Activate the virtual environment:
```bash
# On Unix/macOS
source ./.venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

## Dependencies

The project uses the following main dependencies, managed by `uv`:
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
- `setup.py`: Automated setup script for environment and dependencies using `uv`
- `requirements.txt`: List of Python package dependencies

## Usage

After setting up the environment, you can run the Jupyter notebook:
```bash
# Activate the virtual environment if not already active
# source ./.venv/bin/activate (Unix/macOS) or .\.venv\Scripts\activate (Windows)

jupyter notebook text_classification_embeddings_final.ipynb
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
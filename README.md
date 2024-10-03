<a id="readme-top"></a>


# Amazon Books Genre Classifier
<div align="center">
  
  [![Static Badge](https://img.shields.io/badge/v3.12.3-blue?label=Python)](https://www.python.org/)
  [![Static Badge](https://img.shields.io/badge/1.5.2-blue?label=Scikit-learn)](https://scikit-learn.org/stable/)
  [![Static Badge](https://img.shields.io/badge/2.2.3-purple?label=Pandas)](https://pandas.pydata.org/)
  [![Static Badge](https://img.shields.io/badge/3.9.2-%23C6BEEE?label=Matplotlib)](https://matplotlib.org/)
  [![Static Badge](https://img.shields.io/badge/3.9.1-darkblue?label=Nltk)](https://www.nltk.org/)
  [![Static Badge](https://img.shields.io/badge/4.44.1-%23ff7c00?label=Gradio)](https://www.gradio.app/)
</div>

## About The Project
This project aims to classify books into their main genres based on their titles or descriptions. It uses Machine Learning techniques, particularly a Support Vector Machine (SVM) model, to analyze book titles and predict their respective genres. The model was trained on a Amazon books dataset containing book `Titles`, `Authors`, `Main Genre`, `Sub Genre` and more attributes.

## Features
- Dataset: The dataset can be found in the following link: [here](https://www.kaggle.com/datasets/chhavidhankhar11/amazon-books-dataset?resource=download). It includes 3 different datasets: **Books_df**, **Genre**, and **Sub_Genre**.  
  For this project we used **Books_df** dataset, which contains the following columns: `Titles`, `Authors`, `Main Genre`, `Subgenre`, `Type`, `Price`, `Rating`, `No. of people voted`, `URLs`. Subsequently, a transformation process was carried out to clean and prepare the data for analysis and model trainning.
- Data Analysis: Several visualizations were performed to gain insights into the dataset:
  - A plot showing the relationship between book ratings and the number of votes each book received per genre.
  - Analysis of average book prices across different genres, revealing pricing trends per genre.
  - Visualization of the top 10 authors with the most expensive books registerd by Amazon, highlighting high-value authors.
  - A scatter plot showing book price distribution by genre, providing an overview of price variability within each genre.
- Preprocessing: Text preprocessing includes lowering case, removing stop words, and using n-grams to capture meaningful patterns in the titles.
- Model: The core classifier is a trained **SVM model** that processes the titles or descriptions and predicts the most likely genre.
- Vectorization: The titles are converted into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency) to represent their text-based features in a way the **SVM model** can process.
- Evaluation: The performance of the model was evaluated using metrics like F1-score and recall.
- Gradio Interface: An interactive interface was built using Gradio to allow users to input a book title and receive predictions about the book's most likely genre based on the trained model.

## Getting started

### To get running locally:
- Clone the repository
  ```sh
  git clone https://github.com/ALEXUSCR-27/Amazon-Books-Genre-Classifier.git
  ```
- Install all dependencies
  ```sh
  pip install -r requirements.txt
  ```
- Execute app.py file
  ```sh
  python app.py
  ```
- Access the interface with the local URL created by Gradio
  ```sh
  http://localhost:port
  ```

  <p align="center"><a href="#readme-top">Back to top ☝🏼</a></p>

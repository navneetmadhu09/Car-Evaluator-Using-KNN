# 🚗 Car Evaluator Using KNN

## 📌 Project Overview

Car Evaluator is a Machine Learning project that predicts the evaluation category of a car based on its characteristics. It uses the **K-Nearest Neighbors (KNN) classification algorithm** and a Streamlit web application to provide an interactive user experience.

Users can select different car features and receive a predicted car evaluation category.

## 🎯 Objectives

- Build a car evaluation classification model using KNN.
- Process car attributes into numerical features for prediction.
- Integrate the trained model into a Streamlit web application.
- Provide a simple and user-friendly interface for car evaluation.

## ⚙️ Features

- Interactive input fields for car characteristics.
- Prediction based on six car attributes.
- Machine Learning model integration.
- Dark-themed user interface.
- Displays the predicted evaluation category.

## 📊 Input Features

The application uses the following attributes:

| Feature | Description |
|---|---|
| Buying Price | Buying cost of the car |
| Maintenance Cost | Cost of maintaining the car |
| Doors | Number of doors |
| Persons | Seating capacity |
| Luggage Boot | Luggage boot size |
| Safety | Safety level |

## 🧠 Machine Learning Algorithm

**K-Nearest Neighbors (KNN)** is a supervised Machine Learning algorithm used for classification. It predicts a category by considering the nearest data points to a new input.

The trained model predicts one of the following car evaluation categories:

- **Very Good (`vgood`)**
- **Good (`good`)**
- **Acceptable (`acc`)**
- **Unacceptable (`unacc`)**

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

## 📁 Project Structure

```text
Car-Evaluator-KNN/
│
├── car_app.py
├── carmodel.sav
├── carscaler.sav
├── carlabel.sav
├── requirements.txt
├── README.md
└── dataset/
    └── car_evaluation.csv
```

*Update the file structure above to match your actual repository.*

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Car-Evaluator-KNN
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run car_app.py
```

The application will open in your web browser.

## 📈 Project Workflow

1. Collect the car evaluation dataset.
2. Preprocess the input features.
3. Train the KNN classification model.
4. Save the trained model and preprocessing objects.
5. Load the saved objects into the Streamlit application.
6. Accept user inputs and predict the car evaluation category.

## 📚 Learning Outcomes

Through this project, I practiced:

- Understanding and implementing a classification algorithm.
- Data preprocessing and feature encoding.
- Using a saved Machine Learning model for predictions.
- Integrating Machine Learning with Streamlit.
- Developing an interactive Python application.

## 🔮 Future Improvements

- Improve model performance through hyperparameter tuning.
- Add model evaluation metrics such as accuracy, precision, recall, and F1-score.
- Deploy the application online.
- Improve input validation and error handling.

## 👨‍💻 Author

**Your Name**

Connect with me on [LinkedIn](YOUR_LINKEDIN_PROFILE_URL).

---

⭐ If you find this project useful, consider giving the repository a star!

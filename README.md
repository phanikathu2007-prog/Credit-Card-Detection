# Credit-Card-Detection

This project is a machine learning web application that predicts whether a credit card transaction is likely to be fraudulent. The application allows a user to enter transaction information through a web interface, sends the data to a Flask backend, and returns a fraud prediction along with a risk score and visual indicators that explain the result.

I built this project to gain hands-on experience with machine learning, Flask, JavaScript, and web development while learning how fraud detection systems work. The goal was to create a simple application that demonstrates the complete process of collecting user input, preprocessing data, making a prediction with a trained model, and displaying the results in an easy-to-understand format.

## Technologies

This project was built using Python, Flask, Scikit-learn, Pandas, NumPy, HTML, CSS, and JavaScript.

## Dataset

The model was trained using the Credit Card Fraud Detection dataset from Kaggle. The dataset contains anonymized European credit card transactions and is commonly used for fraud detection research because of its highly imbalanced distribution between legitimate and fraudulent transactions.

Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Running the Project

Clone the repository, install the required dependencies, and start the Flask server.

```bash
git clone https://github.com/yourusername/CreditCardFraudDetection.git
cd CreditCardFraudDetection
pip install -r requirements.txt
python app.py
```

After the server starts, open your browser and go to:

```text
http://127.0.0.1:5000
```

From there, enter the transaction details and click **Analyze Transaction** to receive a fraud prediction.

## Future Improvements

There are several features I would like to add in the future, including a more advanced machine learning model, better explanations for each prediction, user authentication, transaction history, and deployment to a cloud platform so the application can be accessed online.

## Acknowledgments

The dataset used in this project was provided by the Machine Learning Group at Université Libre de Bruxelles (ULB) and is publicly available on Kaggle.

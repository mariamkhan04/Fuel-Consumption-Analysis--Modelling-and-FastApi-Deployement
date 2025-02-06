# **Fuel Consumption Prediction: Data Analysis, ML Modeling & API Development with FastAPI**

## **Overview**

This project focuses on **analyzing vehicle fuel consumption and developing a predictive model using FastAPI**. The dataset used contains information on vehicles manufactured in the year 2000, including attributes such as **engine size, cylinder count, CO₂ emissions, and fuel consumption**. Due to the dataset's historical nature, the fuel efficiency trends may differ from modern vehicles.

A **Linear Regression model** has been trained to predict fuel consumption (L/100 km) based on vehicle parameters. The model has been evaluated using metrics like **Mean Absolute Error (MAE)** and **R² Score**, ensuring reliable predictions.

The trained model is served as a **REST API using FastAPI**, deployed locally on a development server using Uvicorn. The project also includes a **frontend interface** that allows users to input vehicle parameters and receive fuel consumption predictions in real time.

![alt text](image.png)

## **Project Structure**

### **1. Dataset**

[FuelConsumption.csv](FuelConsumption.csv) : Contains vehicle attributes and fuel consumption data from the year 2000.

[Dataset on Kaggle](https://www.kaggle.com/datasets/krupadharamshi/fuelconsumption)

### **2. EDA and Machine Learning Model**

[AnalysisAndModelling.ipynb](AnalysisAndModelling.ipynb): Jupyter Notebook detailing data exploration, preprocessing,visualization and model training.

[LinearModel.pkl](LinearModel.pkl): Trained Linear Regression model for fuel consumption prediction.

### **3. Backend (FastAPI)**

[app.py](app.py): Implements the FastAPI backend to serve the model as a REST API.

### **4. Frontend**

[static/index.html](static/index.html): Web-based interface for user interaction.

[static/styles.css](static/styles.css): Styling for the frontend.

[static/script.js](static/script.js): Handles API calls and updates UI with predictions.


## **Installation & Setup**

### **1. Clone the Repository**

```bash  
git clone <repository_url>
cd <repository_directory>
```  

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Run the FastAPI Server**

```bash
uvicorn app:app --reload
```


## **Usage**

### **API Endpoints**

**GET** ```/```: Returns a welcome message.

**POST** ```/predict```: Takes vehicle parameters as input (engine size, cylinders, CO₂ emissions) and returns predicted fuel consumption.


## **Frontend Interaction**

1. Open ```static/index.html``` in a browser.

2. Input vehicle parameters and submit the form.

3. View the predicted fuel consumption displayed on the webpage.


## Author

- LinkedIn - [mariamkhan-0424](https://www.linkedin.com/in/mariam-khan0424)
- GitHub - [mariamkhan04](https://github.com/mariamkhan04)
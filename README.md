# Insurance-Claim-Prediction
Machine Learning, Flask, Docker, AWS EC2 Deployment

# 🏥 Insurance Claim Prediction

## 📌 Project Overview
The **Insurance Claim Prediction** system is a machine learning-based web application that predicts whether an insurance claim will be made based on user input. It uses a classification model trained on various factors such as age, BMI, number of children, smoking status, and region.

# Insurance Claim Prediction

## Project Overview
This project predicts whether an insurance claim will be made based on user input features like age, BMI, smoker status, and more. It is a full-stack ML application deployed using Flask, Docker, and AWS EC2.

## 📊 Dataset
The dataset consists of the following features:
- **age** (int) - Age of the insured
- **sex** (binary: 1 for Male, 0 for Female)
- **bmi** (float) - Body Mass Index
- **children** (int) - Number of children
- **smoker** (binary: 1 for Yes, 0 for No)
- **region** (categorical: 0=Northeast, 1=Northwest, 2=Southeast, 3=Southwest)
- **charges** (float) - Insurance charges
- **insurance_claim** (binary: 1 for Claimed, 0 for Not Claimed)

## Tech Stack
- **Machine Learning**: Scikit-learn
- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Deployment**: AWS EC2, Docker

## Project Structure
```
app/
│── templates/                  # Contains HTML files for UI
│── app.py                      # Flask application file
│── claim1.pem                  # AWS EC2 key file
│── Dockerfile                  # Docker setup file
│── insurance_model.pkl         # Trained ML model
│── model_training.ipynb        # Jupyter Notebook for training the model
│── my-app.tar                  # Compressed project file for deployment
│── requirements.txt            # Dependencies list
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone <repository_link>
cd app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Flask Application Locally
```bash
python app.py
```
Open your browser and go to:
```
http://127.0.0.1:5000
```

### 4️⃣ Train the Model 🚀 (if needed)
Run `model_training.ipynb` in Jupyter Notebook to retrain the model and save it as `insurance_model.pkl`.

## Docker Setup
### 1️⃣ Build the Docker Image
```bash
docker build -t insurance-claim-app .
```

### 2️⃣ Run the Container
```bash
docker run -p 5000:5000 insurance-claim-app
```
Visit `http://localhost:5000` in your browser.

## 📦 Dockerization
### 1️⃣ Build Docker Image
```bash
docker build -t insurance-claim-app .
```

### 2️⃣ Run Docker Container
```bash
docker run -p 5000:5000 insurance-claim-app

## 🖥️ Deployment on AWS EC2
### 1️⃣ Copy the Project to EC2
Transfer the `.tar` file from your local machine to EC2:
```bash
scp -i claim1.pem my-app.tar ubuntu@<EC2-IP-ADDRESS>:/home/ubuntu/
```

### 2️⃣ Connect to EC2
```bash
ssh -i claim1.pem ubuntu@<EC2-IP-ADDRESS>
```

### 3️⃣ Extract and Navigate
```bash
tar -xvf my-app.tar
cd app
```

### 4️⃣ Run the Application
```bash
python app.py
```
Access the application using:
```
http://<EC2-IP-ADDRESS>:5000
```

## Troubleshooting
- If permission is denied while connecting to EC2:
  ```bash
  chmod 400 claim1.pem
  ```
- If the URL is not working, ensure Flask is running and security group rules allow port 5000.


## 🎯 Features
✅ User-friendly Web Interface  
✅ Machine Learning-based Prediction  
✅ Flask API Backend  
✅ Deployed on AWS EC2  
✅ Dockerized for Scalability  

## 📜 License
This project is open-source and free to use.
Let me know if you need further modifications! 🚀
Made with ❤️ by Hetvi Bhora 🚀



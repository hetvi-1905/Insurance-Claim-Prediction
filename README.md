# Insurance-Claim-Prediction
Machine Learning, Flask, Docker, AWS EC2 Deployment

# 🏥 Insurance Claim Prediction

## 📌 Project Overview
The **Insurance Claim Prediction** system is a machine learning-based web application that predicts whether an insurance claim will be made based on user input. It uses a classification model trained on various factors such as age, BMI, number of children, smoking status, and region.

## 📂 Project Structure
```
Insurance-Claim-Prediction/
│── model/
│   ├── train_model.py          # Script to train the model
│   ├── insurance_model.pkl     # Saved trained model
│
│── app/
│   ├── main.py                 # Flask backend
│   ├── templates/
│   │   ├── index.html          # HTML form for user input
│   ├── static/
│   │   ├── styles.css          # Styles for UI
│
│── requirements.txt            # Python dependencies
│── Dockerfile                  # Docker containerization
│── README.md                   # Project documentation
│── run.sh                      # Script to start the application
```

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

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/insurance-claim-prediction.git
cd insurance-claim-prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application Locally
```bash
python app/main.py
```
Access the web app at: `http://127.0.0.1:5000`

## 🚀 Model Training
To train the model, run:
```bash
python model/train_model.py
```
This will generate `insurance_model.pkl`.

## 🖥️ Deployment on AWS EC2

### 1️⃣ Transfer Files to EC2
```bash
scp -i your-key.pem -r insurance-claim-prediction ubuntu@your-ec2-ip:/home/ubuntu/
```

### 2️⃣ Connect to EC2
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

### 3️⃣ Run the Application
```bash
cd insurance-claim-prediction
python app/main.py
```

### 4️⃣ Open the Web App
Access at: `http://<EC2-PUBLIC-IP>:5000`

## 📦 Dockerization

### 1️⃣ Build Docker Image
```bash
docker build -t insurance-claim-app .
```

### 2️⃣ Run Docker Container
```bash
docker run -p 5000:5000 insurance-claim-app
```

## 🎯 Features
✅ User-friendly Web Interface  
✅ Machine Learning-based Prediction  
✅ Flask API Backend  
✅ Deployed on AWS EC2  
✅ Dockerized for Scalability  

## 📜 License
This project is licensed under the MIT License.

---
Made with ❤️ by [Your Name] 🚀



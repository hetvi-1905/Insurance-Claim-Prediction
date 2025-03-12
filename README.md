# 🏥 Insurance Claim Prediction

## 📌 Project Overview
The **Insurance Claim Prediction** system is a machine learning-based web application that predicts whether an insurance claim will be made based on user input. It uses a classification model trained on various factors such as age, BMI, number of children, smoking status, and region.

## 📊 Dataset
The dataset consists of the following features:
- **age** (int) - Age of the insured
- **sex** (binary: 1 for Male, 0 for Female)
- **bmi** (float) - Body Mass Index!

- **children** (int) - Number of children
- **smoker** (binary: 1 for Yes, 0 for No)
- **region** (categorical: 0=Northeast, 1=Northwest, 2=Southeast, 3=Southwest)
- **charges** (float) - Insurance charges
- **insurance_claim** (binary: 1 for Claimed, 0 for Not Claimed)

## 🛠 Tech Stack
- **Machine Learning**: Scikit-learn
- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Deployment**: AWS EC2, Docker

## 📂 Project Structure

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

## 🚀 Model Training
To train the model, run:
```bash
python model/train_model.py
```
This will generate `insurance_model.pkl`.

## 🐳 Dockerization
### 1️⃣ Build Docker Image
```bash
docker build -t insurance-claim-app .
```

### 2️⃣ Run Docker Container
```bash
docker run -p 5000:5000 insurance-claim-app
```


## 🖥️-> ☁️ Deployment on AWS EC2
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


## 🛠 Troubleshooting ⚠️

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

## UI APP 
![UI1](https://github.com/user-attachments/assets/3c1d7ba9-6f02-455b-8146-8be7411964bd)
![UI2](https://github.com/user-attachments/assets/4dbf5e59-6213-4121-812a-15a0f820b54a)

## 📜 License
This project is open-source and free to use.
Let me know if you need further modifications! 🚀
Made with ❤️ by Hetvi Bhora 🚀



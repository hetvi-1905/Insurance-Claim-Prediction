# # Use official Python image
FROM python:3.9

# # Set working directory
# WORKDIR /app

# # Copy all files, including the model
# COPY . .

# # Install dependencies
# RUN pip install -r requirements.txt

# # Expose API port
# EXPOSE 5000

# # COPY insurance_model.pkl /app/insurance_model.pkl

# # Run Flask app
# CMD ["python", "app.py"]
# Set working directory
WORKDIR /app

# Copy all necessary files into the container
COPY requirements.txt /app/
COPY insurance_model.pkl /app/
COPY app.py /app/
COPY templates /app/templates/


RUN python --version
RUN pip --version
RUN cat requirements.txt
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "app.py"]

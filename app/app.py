import flask
import pickle
import numpy as np
import os

model_path = os.path.join(os.getcwd(), "insurance_model.pkl")

if not os.path.exists(model_path):
    print(f"ERROR: Model file not found at {model_path}")
else:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    print("Model loaded successfully!")


# Initialize Flask app
app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if flask.request.method == "GET":
        return flask.render_template("main.html", original_input={}, result=None) 

    if flask.request.method == "POST":
        try:
            # Debug: Print raw form data
            print("Received input:", flask.request.form)

            # Get input values from form
            age = flask.request.form.get("age")
            sex = flask.request.form.get("sex")
            bmi = flask.request.form.get("bmi")
            children = flask.request.form.get("children")
            smoker = flask.request.form.get("smoker")
            region = flask.request.form.get("region")
            charges = flask.request.form.get("charges")

            # Debug: Print extracted values
            print(f"Extracted values - Age: {age}, Sex: {sex}, BMI: {bmi}, Children: {children}, Smoker: {smoker}, Region: {region}, Charges: {charges}")

            # Check for missing inputs
            if None in [age, sex, bmi, children, smoker, region, charges]:
                print("ERROR: Missing input data!")
                return flask.render_template("main.html", original_input={}, result="Missing input data. Please fill all fields.")

            # Convert inputs to correct types
            age = int(age)
            sex = int(sex)
            bmi = float(bmi)
            children = int(children)
            smoker = int(smoker)
            region = int(region)
            charges = float(charges)

            # Debug: Print transformed inputs
            print("Transformed inputs:", [age, sex, bmi, children, smoker, region, charges])

            # Ensure the model is loaded
            if model is None:
                print("ERROR: Model not loaded!")
                return flask.render_template("main.html", original_input={}, result="Model not loaded. Please check the server.")

            # Make prediction
            input_data = np.array([[age, sex, bmi, children, smoker, region, charges]])
            print("Final input array for model:", input_data)
            prediction = model.predict(input_data)[0]
            print("Prediction result:", prediction)

            return flask.render_template("main.html", original_input=flask.request.form, result=str(prediction))

        except Exception as e:
            print(f"ERROR during processing: {e}")
            return flask.render_template("main.html", original_input={}, result="Error during prediction. Check inputs.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

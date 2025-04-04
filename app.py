import mysql.connector
import os
from flask import Flask, request, render_template
from dotenv import load_dotenv

# Load environment variables (Optional: for security)
load_dotenv()

app = Flask(__name__)

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",         # Change if needed
    password="your_root_password",  # Change this
    database="personal_web"
)
cursor = db.cursor()

# Serve the homepage
@app.route("/")
def home():
    return render_template("index.html")  # Loads index.html

@app.route("/contact")
def contact_form():
    return render_template("contact.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


# Handle Contact Form Submission
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Save data in MySQL
    cursor.execute("INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    db.commit()

    return "Message saved successfully!"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

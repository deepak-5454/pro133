# Importing flask module in the project
from flask import Flask, render_template

# Create an object of the Flask class
app = Flask(__name__)

# Sample family members data
family_members_data = [
    {"name": "Alex", "age": 30, "picture": "/static/alex.jpg"},
    {"name": "John", "age": 35, "picture": "/static/john.jpg"},
    # Add more family members as needed
]

# The route() function of the Flask class
@app.route("/")
def first_flask():
    return render_template("index.html")

@app.route("/family_members")
def family_members():
    return render_template("family_members.html", family_members=family_members_data)

# Run the application on the local server
if __name__ == "__main__":
    app.run(debug=True)

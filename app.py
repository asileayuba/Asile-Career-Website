from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact", methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    new_message = Message(name=name, email=email, message=message)
    db.session.add(new_message)
    db.session.commit()

    return redirect(url_for('thank_you'))

@app.route("/thank_you")
def thank_you():
    return "Thank you for your message!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the database and tables
    app.run(host='0.0.0.0', debug=True)

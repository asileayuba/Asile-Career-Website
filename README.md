# Hackathon Project: Flask Contact Form Application

## Overview
This project is a Flask-based web application designed as a contact form. It allows users to submit their name, email, and message, which are then stored in a SQLite database using SQLAlchemy. The application includes routes for the home page, contact form submission, and a thank-you page.

## Features
- **Contact Form**: Collects user inputs (name, email, message).
- **Database Storage**: Saves submissions to an SQLite database using SQLAlchemy.
- **Responsive Design**: Built with Bootstrap for a user-friendly interface.
- **Thank You Page**: Confirmation page shown after form submission.

## Table of Contents
1. Installation
2. Usage
3. Routes
4. Technologies Used
5. Contributing
6. License

## Installation

### Prerequisites
- Python 3.7 or higher
- Flask
- SQLAlchemy
- SQLite

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hackathon-contact-form.git
   cd hackathon-contact-form
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   Run the following commands in a Python shell to create the database:
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. **Run the application**:
   ```bash
   flask run
   ```
   Access the application at `http://127.0.0.1:5000`.

## Usage
- Navigate to the homepage to access the contact form.
- Fill out the form with your name, email, and message.
- Submit the form to store the data and be redirected to the thank-you page.

## Routes
- **`/`**: Displays the contact form.
- **`/submit`**: Handles form submissions and stores data in the database.
- **`/thankyou`**: Shows a confirmation message after successful form submission.

## Technologies Used
- **Flask**: Web framework for Python.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **SQLite**: Lightweight database for storing contact form data.
- **Bootstrap**: Framework for responsive design.
- **HTML/CSS**: For structuring and styling the web pages.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or fixes.

## License
This project is licensed under the MIT License.



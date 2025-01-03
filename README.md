Library Management System

This project is a web-based Library Management System built using Flask. It allows users to manage books, members, and borrowing activities efficiently.



Features

Manage books and their details.

Add, edit, and delete member records.

Borrowing and returning functionality.

User-friendly interface.

Prerequisites

Ensure you have the following installed on your system:

Python 3.7 or higher

pip (Python package installer)

Setup Instructions

Clone the Repository

git clone <repository-url>
cd library_management

Create a Virtual Environment
Create a virtual environment to isolate the project dependencies:

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

Install Dependencies
Install the required Python libraries:

pip install -r requirements.txt

Set Up the Database
Ensure the database.db file exists in the project directory. If not, create it by initializing the database:

python
>>> from models import db
>>> db.create_all()
>>> exit()

Run the Application
Start the Flask application:

python app.py

The application will be accessible at http://127.0.0.1:5000/.

Directory Structure

app.py: The main entry point of the application.

models.py: Contains database models for the application.

static/: Holds static assets such as CSS, JavaScript, and images.

templates/: Stores HTML templates for rendering views.

database.db: SQLite database file for storing application data.

Testing the Application

Access the Application
Open a browser and navigate to http://127.0.0.1:5000/.

Functionality to Test

Book Management: Add, edit, and delete books.

Member Management: Register new members and manage existing ones.

Borrowing Records: Issue books to members and manage returns.

Database Operations
Ensure CRUD operations work as expected.

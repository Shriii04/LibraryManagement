# Library Management System

This project is a web-based Library Management System built using Flask. It allows users to manage books and members efficiently.

## Features

- Manage books and their details.
- Add, edit, and delete member records.
- Borrowing and returning functionality.
- User-friendly interface.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd library_management
2. **Create a Virtual Environment Create a virtual environment to isolate the project dependencies:**
   ```bash
   Copy code
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\\Scripts\\activate
3. **Install Dependencies Install the required Python libraries:**
   ```bash
   Copy code
   pip install -r requirements.txt
4. **Set Up the Database Ensure the database.db file exists in the project directory. If not, create it by initializing the database:**
   ```bash
   Copy code
   python
   >>> from models import db
   >>> db.create_all()
   >>> exit()

5. **Run the Application Start the Flask application:**
   ```bash
   Copy code
   python app.py
The application will be accessible at http://127.0.0.1:5000/.




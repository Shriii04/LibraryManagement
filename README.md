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

## Directory Structure
   -app.py: The main entry point of the application.
   -models.py: Contains database models for the application.
   -static/: Holds static assets such as CSS, JavaScript, and images.
   -templates/: Stores HTML templates for rendering views.
   -database.db: SQLite database file for storing application data.
   -Testing the Application
   -Access the Application Open a browser and navigate to http://127.0.0.1:5000/.

## Functionality to Test
   -Book Management: Add, edit, and delete books.
   -Member Management: Register new members and manage existing ones.
   -Borrowing Records: Issue books to members and manage returns.
   -Database Operations Ensure CRUD operations work as expected.
      
   **Backend (app.py):**
   **Books:**
   -GET /books: List all books.
   -POST /books: Add a new book.
   -GET /books/<id>: View book information by ID.
   -PUT /books/<id>: Update a book by ID.
   -DELETE /books/<id>: Delete a book by ID.
   
   **Members:**
   -GET /members: List all members.
   -POST /members: Add a new member.
   -GET /members/<id>: View member information by ID.
   -PUT /members/<id>: Update a member by ID.
   -DELETE /members/<id>: Delete a member by ID.
   





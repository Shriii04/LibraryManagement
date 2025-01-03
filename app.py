from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def get_db_connection():
    """Establish a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE, timeout=10)
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row  # Enable dictionary-like access
    return connection


def init_db():
    """Initialize the database with required tables."""
    connection = get_db_connection()
    cursor = connection.cursor()

    # Create Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_date TEXT,
            isbn TEXT UNIQUE
        )
    ''')

    # Create Members table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT
        )
    ''')

    connection.commit()
    connection.close()


@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        connection = get_db_connection()
        books = connection.execute('SELECT * FROM books').fetchall()
        connection.close()
        return jsonify([dict(book) for book in books])

    elif request.method == 'POST':
        data = request.get_json()
        title = data['title']
        author = data['author']
        published_date = data.get('published_date', None)
        isbn = data.get('isbn', None)

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books (title, author, published_date, isbn) VALUES (?, ?, ?, ?)',
                       (title, author, published_date, isbn))
        connection.commit()
        connection.close()
        return {"message": "Book added successfully"}, 201


@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    connection = get_db_connection()

    if request.method == 'GET':
        book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
        connection.close()
        if not book:
            return {"message": "Book not found"}, 404
        return jsonify(dict(book))

    elif request.method == 'PUT':
        data = request.get_json()
        title = data['title']
        author = data['author']
        published_date = data.get('published_date', None)
        isbn = data.get('isbn', None)

        cursor = connection.cursor()
        cursor.execute('''
            UPDATE books
            SET title = ?, author = ?, published_date = ?, isbn = ?
            WHERE id = ?
        ''', (title, author, published_date, isbn, book_id))
        connection.commit()
        connection.close()
        return {"message": "Book updated successfully"}

    elif request.method == 'DELETE':
        connection.execute('DELETE FROM books WHERE id = ?', (book_id,))
        connection.commit()
        connection.close()
        return {"message": "Book deleted successfully"}


@app.route('/members', methods=['GET', 'POST'])
def handle_members():
    if request.method == 'GET':
        connection = get_db_connection()
        members = connection.execute('SELECT * FROM members').fetchall()
        connection.close()
        return jsonify([dict(member) for member in members])

    elif request.method == 'POST':
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone = data.get('phone', None)

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO members (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
        connection.commit()
        connection.close()
        return {"message": "Member added successfully"}, 201


@app.route('/members/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_member(member_id):
    connection = get_db_connection()

    if request.method == 'GET':
        member = connection.execute('SELECT * FROM members WHERE id = ?', (member_id,)).fetchone()
        connection.close()
        if not member:
            return {"message": "Member not found"}, 404
        return jsonify(dict(member))

    elif request.method == 'PUT':
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone = data.get('phone', None)

        cursor = connection.cursor()
        cursor.execute('''
            UPDATE members
            SET name = ?, email = ?, phone = ?
            WHERE id = ?
        ''', (name, email, phone, member_id))
        connection.commit()
        connection.close()
        return {"message": "Member updated successfully"}

    elif request.method == 'DELETE':
        connection.execute('DELETE FROM members WHERE id = ?', (member_id,))
        connection.commit()
        connection.close()
        return {"message": "Member deleted successfully"}


@app.route('/search/books', methods=['GET'])
def search_books():
    query = request.args.get('q', '')
    connection = get_db_connection()
    books = connection.execute('''
        SELECT * FROM books WHERE title LIKE ? OR author LIKE ?
    ''', (f'%{query}%', f'%{query}%')).fetchall()
    connection.close()
    return jsonify([dict(book) for book in books])

@app.route('/view_book/<int:book_id>', methods=['GET'])
def view_book(book_id):
    connection = get_db_connection()
    book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    connection.close()

    if book:
        return jsonify(dict(book))  # Return the book information as a JSON object
    else:
        return {"message": "Book not found"}, 404


if __name__ == '__main__':
    init_db()  # Initialize the database tables
    app.run(debug=True)

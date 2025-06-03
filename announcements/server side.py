from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import sqlite3

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DB_PATH = 'database.sqlite3'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------------------- Database Setup --------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS announcements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            filename TEXT NOT NULL,
            filepath TEXT NOT NULL,
            uploaded_at TIMESTAMP NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# -------------------- Routes --------------------

@app.route('/')
def index():
    return " Announcement server with DB is running."

# Upload with title
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files or 'title' not in request.form:
        return jsonify({'status': 'error', 'message': 'Missing file or title'}), 400

    file = request.files['file']
    title = request.form['title']

    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file selected'}), 400

    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'status': 'error', 'message': 'Only PDFs allowed'}), 400

    # Prepare paths
    safe_name = secure_filename(file.filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{safe_name}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file.save(filepath)

    # Save to DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO announcements (title, filename, filepath, uploaded_at) VALUES (?, ?, ?, ?)", 
              (title, filename, filepath, datetime.now()))
    conn.commit()
    conn.close()

    return jsonify({
        'status': 'success',
        'filename': filename,
        'url': f"/files/{filename}",
        'message': 'File uploaded successfully.'
    })

# List records from DB
@app.route('/records', methods=['GET'])
def records():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT title, filename, uploaded_at FROM announcements ORDER BY uploaded_at DESC")
    rows = c.fetchall()
    conn.close()

    data = [
        {
            'title': title,
            'filename': filename,
            'url': f"/files/{filename}",
            'uploaded_at': uploaded_at
        } for title, filename, uploaded_at in rows
    ]

    return jsonify(data)

# Serve files
@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

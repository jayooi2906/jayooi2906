from flask import Flask, request, jsonify, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Health check route
@app.route('/')
def index():
    return "📡 Announcement server is running."

# Upload endpoint
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file selected'}), 400

    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'status': 'error', 'message': 'Only PDFs allowed'}), 400

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{file.filename}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    return jsonify({
        'status': 'success',
        'filename': filename,
        'url': f"/files/{filename}",
        'message': 'File uploaded successfully.'
    })

# List all uploaded files
@app.route('/list', methods=['GET'])
def list_files():
    files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)
    return jsonify(files)

# Serve uploaded files
@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

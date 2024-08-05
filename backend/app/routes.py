from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from .utils import process_pdf, chat_with_document

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['pdf_file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        upload_folder = os.getenv('UPLOAD_FOLDER', 'data')
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully!"})
    else:
        return jsonify({"error": "Invalid file format. Please upload a PDF."}), 400

@main.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    try:
        response = chat_with_document(prompt)
        return jsonify({"prompt": prompt, "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@main.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get('filename')
    
    if not filename:
        return jsonify({"error": "No filename provided"}), 400
    
    upload_folder = os.getenv('UPLOAD_FOLDER', 'data')
    file_path = os.path.join(upload_folder, secure_filename(filename))
    
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": "File deleted successfully!"})
    else:
        return jsonify({"error": "File not found"}), 404

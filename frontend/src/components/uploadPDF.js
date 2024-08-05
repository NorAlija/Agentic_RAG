import React, { useState } from 'react';
import axios from 'axios';

const UploadPDF = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('pdf_file', file);

    try {
      const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setMessage(response.data.message || 'File uploaded successfully!');
    } catch (error) {
      setMessage('Error uploading file.');
    }
  };

  const handleDelete = async (filename) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/delete', { filename });
      setMessage(response.data.message || 'File deleted successfully!');
    } catch (error) {
      setMessage('Error deleting file.');
    }
  };

  return (
    <div>
      <h1>Upload PDF</h1>
      <form onSubmit={handleUpload}>
        <input type="file" accept=".pdf" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {file && <button onClick={() => handleDelete(file.name)}>Delete</button>}
      {message && <p>{message}</p>}
    </div>
  );
};

export default UploadPDF;

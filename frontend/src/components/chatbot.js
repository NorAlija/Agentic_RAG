import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    setPrompt(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:5000/chat', { prompt });
      setResponse(res.data.response);
    } catch (err) {
      setError('Error fetching response from the server');
    }
  };

  return (
    <div>
      <h1>Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={prompt}
          onChange={handleInputChange}
          placeholder="Ask a question..."
        />
        <button type="submit">Send</button>
      </form>
      {error && <p>{error}</p>}
      {response && (
        <div>
          <h2>NoriGPT:</h2>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
};

export default Chatbot;

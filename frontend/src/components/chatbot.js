
import React, { useState } from 'react';
import axios from 'axios';


const Chatbot = () => {
  const [prompt, setPrompt] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    setPrompt(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt) return;

    const userMessage = { text: prompt, sender: 'user' };
    setMessages([...messages, userMessage]);
    setPrompt('');
    setLoading(true);

    try {
      const res = await axios.post('http://127.0.0.1:5000/chat', { prompt });
      const botResponse = { text: res.data.response, sender: 'bot' };
      setMessages([...messages, userMessage, botResponse]);
    } catch (err) {
      setError('Error fetching response from the server');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="chatbot">
        <div className="chat-window">
          <div className="messages">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={msg.sender === 'user' ? 'user-message' : 'bot-response'}
              >
                {msg.text}
              </div>
            ))}
            {loading && <div className="bot-response">...</div>}
          </div>
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
        </div>
      </div>
    </div>
  );
};

export default Chatbot;


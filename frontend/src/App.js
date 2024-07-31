import React from 'react';
import UploadPDF from './components/chatbot.js';
import Chatbot from './components/uploadPDF.js';
import "./App.css";

function App() {
  return (
    <div className="App">
      <UploadPDF />
      <Chatbot />
    </div>
  );
}

export default App;

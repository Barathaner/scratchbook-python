import React from 'react';
import './App.css';
import Joystick from './Joystick';
import ReactPlayer from 'react-player'
import WebSocketImage from './WebSocketImage';

// Render a YouTube video player

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <WebSocketImage></WebSocketImage>
        <Joystick />
      </header>
    </div>
  );
}

export default App;

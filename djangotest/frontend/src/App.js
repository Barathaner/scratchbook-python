import React from 'react';
import './App.css';
import Joystick from './Joystick';
import ReactPlayer from 'react-player'

// Render a YouTube video player

function App() {
  return (
    <div className="App">
      <header className="App-header">
        
<ReactPlayer url='http://localhost:8000/media/stream.m3u8' />
        <Joystick />
      </header>
    </div>
  );
}

export default App;

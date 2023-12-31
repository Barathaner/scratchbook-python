import React, { useState, useEffect } from 'react';

function WebSocketImage() {
  const [imageSrc, setImageSrc] = useState(null);

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/ws/screen_capture/');

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setImageSrc(`data:image/jpeg;base64,${data.image}`);
    };

    // Close the socket when the component is unmounted
    return () => {
      socket.close();
    };
  }, []);  // The empty array means this useEffect runs once when the component mounts and cleans up when it unmounts

  return (
    <div>
      {imageSrc ? <img src={imageSrc} alt="Received from WebSocket" width="959" /> : <p>Waiting for image...</p>}
    </div>
  );
}

export default WebSocketImage;

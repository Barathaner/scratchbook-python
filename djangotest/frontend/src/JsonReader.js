import React, { useState, useEffect } from 'react';

function JsonReader() {
  const [data, setData] = useState({});
  const [ws, setWs] = useState(null);

  useEffect(() => {
    const websocket = new WebSocket('ws://localhost:8000/ws/xmlparser/');

    websocket.onopen = () => {
      console.log('WebSocket Client Connected');
    };

    websocket.onmessage = (message) => {
      const parsedData = JSON.parse(message.data);
      setData(parsedData);
    };

    setWs(websocket);

    return () => {
      if (websocket) {
        websocket.close();
      }
    };
  }, []);

  const renderJson = (obj) => {
    return Object.keys(obj).map((key, index) => {
      if (typeof obj[key] === 'object' && obj[key] !== null) {
        return (
          <div key={index} style={{ marginLeft: '20px' }}>
            <strong>{key}:</strong>
            {renderJson(obj[key])}
          </div>
        );
      }
      return (
        <div key={index}>
          <label>{key}:</label>
          <input type="text" value={obj[key]} readOnly />
        </div>
      );
    });
  };

  return <div>{renderJson(data)}</div>;
}

export default JsonReader;

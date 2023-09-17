import React, { Component } from 'react';
import './Joystick.css'; 
class Joystick extends Component {
  constructor(props) {
    super(props);
    this.state = {
      direction: null,
      isPressed: false,
      message: ''
    };
  }

  componentDidMount() {
    this.socket = new WebSocket('ws://localhost:8000/ws/joystick/'); // Adresse Ihres Django-Servers

    this.socket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      this.setState({ message: data.message });
    };

    document.addEventListener('keydown', this.handleKeyDown);
    document.addEventListener('keyup', this.handleKeyUp);
  }

  componentWillUnmount() {
    document.removeEventListener('keydown', this.handleKeyDown);
    document.removeEventListener('keyup', this.handleKeyUp);
  }

  handleKeyDown = (event) => {
    this.sendDirection(event, true);
  }

  handleKeyUp = (event) => {
    this.sendDirection(event, false);
  }

onTouchEnd = (direction,event) => {
    if (event) {
        event.preventDefault();
        if (event.changedTouches) {
          const touch = event.changedTouches[0];
          if (touch) {
            // Hier könnten Sie das Touch-Objekt verwenden, wenn Sie es benötigen
          }
        }
      }
      this.setState({ isPressed: false });
      this.socket.send(JSON.stringify({ direction, isPressed: false }));
    }

onTouchStart = (direction,event) => {
    if (event) {
        event.preventDefault();
        // Für Touch-Events verwenden Sie changedTouches anstelle von touches
        if (event.changedTouches) {
          // Behandle das erste Touch-Event
          const touch = event.changedTouches[0];
          if (touch) {
            // Hier könnten Sie das Touch-Objekt verwenden, wenn Sie es benötigen
            // Aktuell tun wir nichts mit dem Touch-Objekt, aber es ist wichtig zu wissen, dass es existiert
          }
        }
      }
      this.setState({ direction, isPressed: true });
      this.socket.send(JSON.stringify({ direction, isPressed: true }));
    }
    

  handleMouseDown = (direction, event) => {
    if (event) {
      event.preventDefault();
      // Für Touch-Events verwenden Sie changedTouches anstelle von touches
      if (event.changedTouches) {
        // Behandle das erste Touch-Event
        const touch = event.changedTouches[0];
        if (touch) {
          // Hier könnten Sie das Touch-Objekt verwenden, wenn Sie es benötigen
          // Aktuell tun wir nichts mit dem Touch-Objekt, aber es ist wichtig zu wissen, dass es existiert
        }
      }
    }
    this.setState({ direction, isPressed: true });
    this.socket.send(JSON.stringify({ direction, isPressed: true }));
  }
  
  handleMouseUp = (direction, event) => {
    if (event) {
      event.preventDefault();
      if (event.changedTouches) {
        const touch = event.changedTouches[0];
        if (touch) {
          // Hier könnten Sie das Touch-Objekt verwenden, wenn Sie es benötigen
        }
      }
    }
    this.setState({ isPressed: false });
    this.socket.send(JSON.stringify({ direction, isPressed: false }));
  }
  
  
sendDirection = (event, isPressed) => {
    let direction;
    switch (event.keyCode) {
        case 37: direction = 'left'; break;
        case 38: direction = 'up'; break;
        case 39: direction = 'right'; break;
        case 40: direction = 'down'; break;
        default: return;
    }
    this.setState({ direction, isPressed });
    this.socket.send(JSON.stringify({ direction, isPressed }));
}


renderButton(direction, label) {
    const isActive = this.state.isPressed && this.state.direction === direction;
    return (
<div
  className={`joystick-button ${isActive ? 'active' : ''}`}
  data-direction={direction}
  onMouseDown={(e) => this.handleMouseDown(direction, e)}
  onMouseUp={(e) => this.handleMouseUp(direction, e)}
  onTouchStart={(e) => this.handleMouseDown(direction, e)}
  onTouchEnd={(e) => this.handleMouseUp(direction, e)}
>
  {label}
</div>
    );
}



  render() {
    return (
      <div className="joystick-container">
        <h1>Joystick Control</h1>
        {this.renderButton('up', '↑')}
        <div className="joystick-horizontal">
          {this.renderButton('left', '←')}
          {this.renderButton('right', '→')}
        </div>
        {this.renderButton('down', '↓')}
        <p>Message from server: {this.state.message}</p>
      </div>
    );
  }
}

export default Joystick;

import React from 'react';
import axios from "axios";

var FLASK_SERVICE_URL = process.env.REACT_APP_FLASK_URL
var PYTHON_SERVICE_URL = process.env.REACT_APP_PYTHON_URL

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
          response: "",
    }

    this.sendRequest = this.sendRequest.bind(this)
  }

  sendRequest = (URL) => {
    console.log("get request sended on url: " + URL)
    
    axios.get(URL, {headers: {
      'Content-Type': 'application/json',
      'X-Custom-Header': 'value' // Если требуется
    }}).then((response) => {
      this.setState({ response: response.data.message });
    }).catch(() => {
      this.setState({ response: "request failed.." });
    })
  };
  
  render() {
    return (
      <div className="App">
        <div style={{ textAlign: "center", marginTop: "50px" }}>
          <h1>Frontend with Api Getaway</h1>
          <button onClick={() => {this.sendRequest(PYTHON_SERVICE_URL)}}>Send python request</button>
          <br/>
          <br/>
          <button onClick={() => {this.sendRequest(FLASK_SERVICE_URL)}}>Send flask request</button>
          <h2>Status: {this.state.response}</h2>
        </div>
      </div>
    )
  };
}

export default App;
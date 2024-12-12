import './App.css';
import axios from "axios";
import React from "react";

var FLASK_URL = process.env.REACT_APP_FLASK_URL

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
      this.setState({ response: response.data.status });
    }).catch(() => {
      this.setState({ response: "Bad response.." });
    })
  };
  
  render() {
    return (
      <div className="App">
        <div style={{ textAlign: "center", marginTop: "50px" }}>
          <h1>Frontend with Circuit Breaker</h1>
          <button onClick={() => {this.sendRequest(FLASK_URL)}}>Send good request</button>
          <br/>
          <br/>
          <button onClick={() => {this.sendRequest(FLASK_URL + "?param=error")}}>Send bad request</button>
          <h2>Status: {this.state.response}</h2>
        </div>
      </div>
    )
  };
}

export default App;
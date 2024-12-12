import React from 'react';
import axios from "axios";

var ADAPTER_SERVICE_URL = process.env.REACT_APP_ADAPTER_URL

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
          response: "",
          name: "",
    }

    this.sendRequest = this.sendRequest.bind(this)
  }

  sendRequest = () => {
    console.log("post request sended on url: " + ADAPTER_SERVICE_URL)

    axios.post(ADAPTER_SERVICE_URL, {name: this.state.name}, {headers: {
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
          <h1>Frontend with Adapter</h1>
          <input onChange={(e) => this.setState({name: e.target.value})}></input>
          <br/>
          <br/>
          <button onClick={() => {this.sendRequest()}}>Send rest request</button>
          <br/>
          <br/>
          <h2>Status: {this.state.response}</h2>
        </div>
      </div>
    )
  };
}

export default App;
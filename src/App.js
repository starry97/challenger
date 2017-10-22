import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Uploader} from "./components/upload.jsx";
import Introduction from "./components/introduction.jsx";

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <Introduction/>
        <Uploader />
      </div>
    );
  }
}

export default App;

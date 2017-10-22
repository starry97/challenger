import React, { Component } from 'react';
import {Uploader} from "./components/upload.jsx";
import Introduction from "./components/introduction.jsx";
import Footer from "./components/footer.jsx";
import './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          {/* <img src={'./logo.svg'} className="App-logo" alt="logo" /> */}
          <h1>Focus</h1>
        </header>
        <Introduction/>
        <Uploader />
        <Footer/>
      </div>
    );
  }
}

export default App;

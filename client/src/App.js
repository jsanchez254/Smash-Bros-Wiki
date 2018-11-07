import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom';

//IMPORT SEMANTIC UI
import { Container, Header } from 'semantic-ui-react'

//IMPORT COMPONENTS
import Navbar from "./components/navbar";
import Timeline from "./components/timeline";
import Home from "./components/home";

//IMPORT IMAGES
import smashLogo from "./assets/img/smashBros.jpg";

//IMPORT CSS
import "./assets/css/home.css";

class App extends Component {
  render() {
    return (
      <Router>
          <div className="App">
            <Navbar/>
                <Container>
                  <Route path = "/home" component = {Home}/>
                  <Route path = "/timeline" component = {Timeline}/>
                </Container>
          </div>
      </Router>
    );
  }
}

export default App;

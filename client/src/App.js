import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom';

//IMPORT SEMANTIC UI
import { Container, Header } from 'semantic-ui-react'

//IMPORT COMPONENTS
import LogIn from "./components/logIn";
import Navbar from "./components/navbar";
import Timeline from "./components/timeline";
import Home from "./components/home";

//IMPORT CHARACTERS
import Lucina from "./characters/Lucina";
import Bayonetta from "./characters/Bayonetta";
import Snake from "./characters/Snake";
import Samus from "./characters/Samus";
import Falco from "./characters/Falco";
import Fox from "./characters/Fox";
import Ike from "./characters/Ike";
import Link from "./characters/Link";
import Toon from "./characters/Toon_Link";
import Young from "./characters/Young_Link";
import Plant from "./characters/Piranha_Plant";

//IMPORT IMAGES
import smashLogo from "./assets/img/smashBros.jpg";

//IMPORT CSS
import "./assets/css/home.css";
import "./assets/css/characters.css";

class App extends Component {
  render() {
    return (
      <Router>
          <div className="App">
                <Route exact path = "/" component = {LogIn}/>
                <Navbar/>
                <Container>
                  <Route path = "/home" component = {Home}/>
                  <Route path = "/timeline" component = {Timeline}/>
                  {/*CHARACTER ROUTES*/}
                  <Route path = "/Lucina" component = {Lucina}/>
                  <Route path = "/Bayonetta" component = {Bayonetta}/>
                  <Route path = "/Snake" component = {Snake}/>
                  <Route path = "/Samus" component = {Samus}/>
                  <Route path = "/Falco" component = {Falco}/>
                  <Route path = "/Fox" component = {Fox}/>
                  <Route path = "/Ike" component = {Ike}/>
                  <Route path = "/Link" component = {Link}/>
                  <Route path = "/Toon Link" component = {Toon}/>
                  <Route path = "/Young Link" component = {Young}/>
                  <Route path = "/Piranha Plant" component = {Plant}/>
                </Container>
          </div>
      </Router>
    );
  }
}

export default App;

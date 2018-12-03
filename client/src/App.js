import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route, Redirect
} from 'react-router-dom';

//IMPORT SEMANTIC UI
import { Container, Header } from 'semantic-ui-react'

//IMPORT COMPONENTS
import LogIn from "./components/logIn";
import Navbar from "./components/navbar";
import Timeline from "./components/timeline";
import Home from "./components/home";
import CreateAccount from "./components/createAccount";
import CreateCharacter from "./components/createCharacter";
import DeleteUser from "./components/deleteUser";
import UpdateChar from  "./components/updateCharacter";

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
import Corrin from "./characters/corrin";
import Cloud from "./characters/cloud";
import Megaman from "./characters/Megaman";
import Greninja from "./characters/Greninja";

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
                <Route path={["/home", "/timeline", "/Lucina",
                 "/Bayonetta", "/Snake", "/Samus", "/Falco", "/Fox", "/Ike",
                 "/Link","/Toon Link", "/Young Link", "/Piranha Plant", "/Mega man",
                 "/Corrin", "/Cloud", "/Greninja", "/createCharacter" , "/DeleteUser",  "/updateChar"]} 
                component = {Navbar}/>
                <Container>
                  <Route path = "/home" component = {Home}/>
                  <Route path = "/timeline" component = {Timeline}/>
                  <Route path = "/createAccount" component = {CreateAccount}/>
                  <Route path = "/createCharacter" component = {CreateCharacter}/> 
                  <Route path = "/DeleteUser" component = {DeleteUser}/> 
                  <Route path = "/updateChar" component = {UpdateChar}/>                   
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
                  <Route path = "/Mega man" component = {Megaman}/>
                  <Route path = "/Corrin" component = {Corrin}/>
                  <Route path = "/Cloud" component = {Cloud}/>
                  <Route path = "/Greninja" component = {Greninja}/>
                </Container>
          </div>
      </Router>
    );
  }
}

export default App;

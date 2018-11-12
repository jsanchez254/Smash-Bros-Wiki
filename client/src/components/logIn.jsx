import React, { Component } from 'react';
import { Link } from 'react-router-dom';
//import logo
import logo from "../assets/img/smashLogo.png";

class logIn extends Component {
    state = {  }
    render() { 
        return (
            <React.Fragment>
                <section class = "hero is-dark is-fullheight">
                    <div class  ="hero-body"> 
                        <div class = "container">
                            <div class = "columns is-centered">
                                <div class = "column is-5-tablet is-3-desktop is-3-widescreen">
                                    <form class="box">
                                        <div class="field has-text-centered">
                                            <img src= {logo} width="167"/>
                                        </div>
                                        
                                        <div class = "field ">
                                            <label class = "label"> Email </label>
                                                <div class = "control has-icons-left">
                                                    <input class = "input" type = "email" placeholder = "EMAIL PORFAVOR!"/>
                                                        <span class = "icon is-small is-left">
                                                            <i class="fas fa-envelope"></i>
                                                        </span>
                                                </div>
                                        </div>
                                        
                                        <div class = "field ">
                                            <label class = "label"> Password </label>
                                                <div class = "control has-icons-left">
                                                    <input class = "input" type = "email" placeholder = "PASSWORD PORFAVOR!"/>
                                                        <span class = "icon is-small is-left">
                                                            <i class="fas fa-lock"></i>
                                                        </span>
                                                </div>
                                        </div>
                                        
                                        <div class = "field">
                                            <label class = "checkbox">
                                                <input type = "checkbox"/>
                                                    REMEMBA ME!
                                            </label>
                                        </div>
                                        
                                        <div class = "field">
                                        <Link to = "/home">
                                            <button class = "button is-success">
                                                Login
                                            </button>
                                        </Link>
                                        </div>
                                    </form>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </section>
            </React.Fragment>
          );
    }
}
 
export default logIn;
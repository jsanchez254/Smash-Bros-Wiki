import React, { Component } from 'react';
import { Link } from 'react-router-dom';
//import logo
import logo from "../assets/img/smashLogo.png";

class logIn extends Component {
    state = {  }
    render() { 
        return (
            <React.Fragment>
                <section className = "hero is-dark is-fullheight">
                    <div className  ="hero-body"> 
                        <div className = "container">
                            <div className = "columns is-centered">
                                <div className = "column is-5-tablet is-3-desktop is-3-widescreen">
                                    <form className="box">
                                        <div className="field has-text-centered">
                                            <img src= {logo} width="167"/>
                                        </div>
                                        
                                        <div className = "field ">
                                            <label className = "label"> Email </label>
                                                <div className = "control has-icons-left">
                                                    <input className = "input" type = "email" placeholder = "EMAIL PORFAVOR!"/>
                                                        <span className = "icon is-small is-left">
                                                            <i className="fas fa-envelope"></i>
                                                        </span>
                                                </div>
                                        </div>
                                        
                                        <div className = "field ">
                                            <label className = "label"> Password </label>
                                                <div className = "control has-icons-left">
                                                    <input className = "input" type = "email" placeholder = "PASSWORD PORFAVOR!"/>
                                                        <span className = "icon is-small is-left">
                                                            <i className="fas fa-lock"></i>
                                                        </span>
                                                </div>
                                        </div>
                                        
                                        <div className = "field">
                                            <label className = "checkbox">
                                                <input type = "checkbox"/>
                                                    REMEMBA ME!
                                            </label>
                                        </div>
                                        
                                        <div className = "field">
                                        <Link to = "/home">
                                            <button className = "button is-success">
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
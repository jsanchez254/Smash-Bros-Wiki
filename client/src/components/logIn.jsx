import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from "axios"
//import logo
import logo from "../assets/img/smashLogo.png";
//IMPORT ICONS 
import { Icon } from 'semantic-ui-react'

//IMPORT NAVBAR
import Navbar from "./navbar"; 


class logIn extends Component {
    state = {
        userName: "",
        password: "",
        stado: ""
      };

    handleChange = (event) => {
        this.setState({[event.target.name]: event.target.value});

    }

    handleSubmit = (event) => {
        event.preventDefault();

        const user ={
            userName: this.state.userName,
            password: this.state.password
        };

        axios.post("http://localhost:5000/logIn", {user})
        .then(res => {
            const stado= res.data;
            this.setState({stado});
        })
    }

    render() { 
        return (
            <React.Fragment>
                    <section className = "hero is-dark is-fullheight">
                        <div className  ="hero-body"> 
                        {this.state.stado}
                            <div className = "container">
                                <div className = "columns is-centered">
                                    <div className = "column is-5-tablet is-3-desktop is-3-widescreen">
                                        <form onSubmit = {this.handleSubmit} className = "box">
                                            <div className="field has-text-centered">
                                                <img src= {logo} width="167"/>
                                            </div>
                                            
                                            <div className = "field ">
                                                <label className = "label"> Email </label>
                                                    <div className = "control has-icons-left">
                                                        <input name = "userName" className = "input" type = "email"
                                                        onChange = {this.handleChange
                                                        } placeholder = "EMAIL PORFAVOR!"/>
                                                            <span className = "icon is-small is-left">
                                                            <Icon name ="mail"/>
                                                            </span>
                                                    </div>
                                            </div>
                                            
                                            <div className = "field ">
                                                <label className = "label"> Password </label>
                                                    <div className = "control has-icons-left">
                                                        <input name = "password" className = "input" type = "password"
                                                        onChange = {this.handleChange} placeholder = "PASSWORD PORFAVOR!"/>
                                                            <span className = "icon is-small is-left">
                                                                <Icon name ="lock"/>
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
                                            {/* <Link to = "/home"> */}
                                                <button type = "submit" value = "Submit" className = "button is-success">
                                                    Login
                                                </button>
                                            {/* </Link> */}
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
import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import axios from "axios"
//import logo
import logo from "../assets/img/smashLogo.png";



class logIn extends Component {
    state = {
        userName: "",
        password: "",
        usuario: "1",
        linkone: "/"
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
            const usuario = res.data;
            this.setState({usuario});
        })
    }

    handlePass = () =>{
        console.log(this.state.usuario);
        if(this.state.usuario == "null1" || this.state.usuario == "1" ){
            if(this.state.usuario == "null1"){
                return (<h1 className = "incorrect">Password or Email is incorrect, try again.</h1>)
            }
            return;
        }
        else{
            this.setState({linkone: "/home"})
            return (<Redirect to = "/home"/>)
        }
    }
    render() { 
        return (
            <React.Fragment>
                    <section className = "hero is-dark is-fullheight">
                        <div className  ="hero-body"> 
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
                                                        } placeholder = "Enter Email"/>
                                                            <span className = "icon is-small is-left">
                                                                <i className="fas fa-envelope"></i>
                                                            </span>
                                                    </div>
                                            </div>
                                            
                                            <div className = "field ">
                                                <label className = "label"> Password </label>
                                                    <div className = "control has-icons-left">
                                                        <input name = "password" className = "input" type = "password"
                                                        onChange = {this.handleChange} placeholder = "Enter Password"/>
                                                            <span className = "icon is-small is-left">
                                                                <i className="fas fa-lock"></i>
                                                            </span>
                                                    </div>
                                            </div>
                                            
                                        
                                            <div className = "field">
                                                <div className = "columns">
                                                        <div className = "column is-5">
                                                            {/* <ink to = {this.state.linkone}> */}
                                                                <button onClick={this.handleSubmit}   type = "submit" value = "Submit" className = "button is-success">
                                                                    Login
                                                                </button>
                                                                
                                                            {/* </Link>  */}
                                                        </div>
                                                        <div className = "column is-3">
                                                            <Link to = "/createAccount">
                                                                <button className = "button is-info">Create Account...</button>
                                                            </Link>
                                                        </div>
                                                </div>
                                                {this.handlePass()}
                                            </div>

                                             <div>
                                                
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
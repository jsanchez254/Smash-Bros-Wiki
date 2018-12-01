import React, { Component } from 'react';

//IMPORT AXIOS
import axios from "axios";

//import logo
import logo from "../assets/img/smashLogo.png";

class createAccount extends Component {
    state = { 
        userName: "",
        password: "",
        main: "",
        email:"",
        name:"",
        lname: ""
     }

     handleChange(event){
        this.setState({[event.target.name]: event.target.value});
     }

     handleSubmit(){
        const newUser= {
            userName : this.state.userName,
            password : this.state.password,
            main: this.state.main,
            email: this.state.email

        }
        axios.post("http://localhost:5000/", {newUser})
            .then(res => {
                
            })

     }
    render() { 
        return (
            <React.Fragment>
               <section className = "hero is-dark is-fullheight">
                        <div className  ="hero-body"> 
                            <div className = "container">
                                <div className = "columns is-centered">
                                    <div className = "column is-8">
                                        <form onSubmit = {this.handleSubmit} className = "box">
                                            <div className="field has-text-centered">
                                                <img src= {logo} width="167"/>
                                            </div>
                                            
                                            <div className = "field ">
                                                <div className = "columns">
                                                    <div className = "column is-6">
                                                        <label className = "label"> Name: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "name" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Name"/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                    </div>

                                                
                                                    <div className = "column is-6">
                                                        <label className = "label">Last Name: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "lname" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Last Name"/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                    </div>
                                                    
                                                    
                                                    

                                                </div>
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
 
export default createAccount;
import React, { Component } from 'react';

import { Link} from 'react-router-dom';

//IMPORT SEMANTIC UI
import { Icon } from 'semantic-ui-react'

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
        lname: "",
        characters: [],
        realCharacter: "realCharacter"
     }

     componentDidMount(){
        axios.get("http://localhost:5000/")
            .then(res => {
                const characters = res.data;
                console.log("hello");
                this.setState({characters});
                console.log(this.state.characters[0]);
            })
    }

     handleChange = (event) =>{
        this.setState({[event.target.name]: event.target.value});
        //takes care of updating main character option!
        if(event.target.name == ""){
            event.target.name = "realCharacter";
            this.setState({[event.target.name]: event.target.value});
        }
     }

     handleSubmit = (event) =>{
        event.preventDefault();
        const newUser= {
            userName : this.state.userName,
            password : this.state.password,
            main: this.state.realCharacter,
            email: this.state.email,
            name: this.state.name,
            lname: this.state.lname

        }
        axios.post("http://localhost:5000/createUser", {newUser})
            .then(res => {
                console.log(res.data)
            })

     }
    render() { 
        return (
            <React.Fragment>
               <section className = "hero is-dark is-fullheight">
                    <Link to = "/">
                        <button className = "button is-warning"><Icon name = "arrow alternate circle left"/>&nbsp;&nbsp;Back To Log In</button>
                    </Link>
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
                                                        
                                            <div className = "field ">
                                                <label className = "label"> User Name: </label>
                                                    <div className = "control has-icons-left">
                                                        <input name = "userName" className = "input"
                                                        onChange = {this.handleChange
                                                        } placeholder = "Enter User Name"/>
                                                            <span className = "icon is-small is-left">
                                                                <i className="fas fa-envelope"></i>
                                                            </span>
                                                    </div>
                                            </div>

                                            <div className = "field ">
                                                <label className = "label"> Email: </label>
                                                    <div className = "control has-icons-left">
                                                        <input name = "email" className = "input" type = "email"
                                                        onChange = {this.handleChange
                                                        } placeholder = "Enter Email"/>
                                                            <span className = "icon is-small is-left">
                                                                <i className="fas fa-envelope"></i>
                                                            </span>
                                                    </div>
                                            </div>

                                            <div className = "field ">
                                                <label className = "label"> Password: </label>
                                                    <div className = "control has-icons-left">
                                                        <input name = "password" className = "input" type = "email"
                                                        onChange = {this.handleChange
                                                        } placeholder = "Enter Email"/>
                                                            <span className = "icon is-small is-left">
                                                                <i className="fas fa-envelope"></i>
                                                            </span>
                                                    </div>
                                            </div>
                                            {/* {this.state.realCharacter}                     */}
                                            <div className  ="field">
                                                
                                                <div className = "select">
                                                        <select onChange = {this.handleChange}>
                                                            <option>Who Is Your Main?</option>
                                                            { this.state.characters.map((msg, index) => 
                                                                <option name = "realCharacter" value = {msg[0]} key = {index}>
                                                                    {msg}
                                                                </option>
                                                            )}
                                                        </select>
                                                </div>
                                            </div>
                                            
                                            <div className = "field">
                                                <button onClick={this.handleSubmit}   type = "submit" value = "Submit" 
                                                className = "button is-success">
                                                    SUBMIT
                                                </button>
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
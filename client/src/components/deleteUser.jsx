import React, { Component } from 'react';

import axios from "axios"

//import logo
import logo from "../assets/img/smashLogo.png";

class DeleteUser extends Component {
    state = {
        users: [],
        user: ""
      }

    componentDidMount(){
        axios.get("http://localhost:5000/getUsers")
            .then(res =>{
                const users = res.data;
                this.setState({users});
            })
    }

    handleChange = (event) =>{
        this.setState({[event.target.name]: event.target.value});
        console.log(event.target.value);
        console.log(event.target.name);
      }


      handleSubmit = (event) =>{
        event.preventDefault();
        const user1= {
            user : this.state.user
        }
        axios.post("http://localhost:5000/DeleteUser", {user1})
            .then(res => {
                console.log(res.data)
            })

     }

    render() { 
        return (
            <React.Fragment>
                <React.Fragment>
               <section className = "hero is-danger is-fullheight">
                        <div className  ="hero-body"> 
                            <div className = "container">
                                <div className = "columns is-centered">
                                    <div className = "column is-5">
                                        <form onSubmit = {this.handleSubmit} className = "box">
                                            <div className="field has-text-centered">
                                                <img src= {logo} width="167"/>
                                            </div>
                                            <div className  ="field">
                                                <div className = "columns">
                                                    <div className = "column is-5">
                                                        <div className = "select">
                                                                <select name = "user" onChange = {this.handleChange}>
                                                                    <option>Delete User</option>
                                                                    { this.state.users.map((msg, index) => 
                                                                        <option  value = {msg[0]} key = {index}>
                                                                            {msg[0]}
                                                                        </option>
                                                                    )}
                                                                </select>
                                                        </div>
                                                    </div>

                                                    <div className = "column is-6">
                                                        <button onClick={this.handleSubmit}   type = "submit" value = "Submit" className = "button is-danger">
                                                            DELETE
                                                        </button>
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
            </React.Fragment>
          );
    }
}
 
export default DeleteUser;
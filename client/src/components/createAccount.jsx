import React, { Component } from 'react';

//IMPORT AXIOS
import axios from "axios";

class createAccount extends Component {
    state = { 
        userName: "",
        password: "",
        main: "",
        email:""
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
                <h1>HELLO I AM CREATE ACCOUNT</h1>
            </React.Fragment>
          );
    }
}
 
export default createAccount;
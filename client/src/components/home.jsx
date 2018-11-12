import React, { Component } from 'react';
import axios from "axios";

import smashLogo from "../assets/img/smashBros.jpg";
import Characters from "./characters";

class home extends Component {
    state = {
        msg: []
      }
    
    componentDidMount(){
        axios.get("http://localhost:5000/")
            .then(res => {
                const msg = res.data;
                this.setState({msg});
            })
    }
    render() { 
        return ( 
            <React.Fragment>
                <div>
                    {/*<img className = "image" src = {smashLogo}/>*/}
                    <div className = "columns is-multiline">
                        { this.state.msg.map(msg => <Characters character = {msg}/>)}
                    </div>
                </div>
                
            </React.Fragment>
         );
    }
}
 
export default home;
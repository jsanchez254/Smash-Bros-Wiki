import React, { Component } from 'react';

import smashLogo from "../assets/img/smashBros.jpg";

class home extends Component {
    state = {  }
    render() { 
        return ( 
            <React.Fragment>
                <div>
                    <img className = "image" src = {smashLogo}/>
                </div>
            </React.Fragment>
         );
    }
}
 
export default home;
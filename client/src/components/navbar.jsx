import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from "axios"

import { Icon } from 'semantic-ui-react';

class navBar extends Component {
    state = { 
        userName: ""
     }
    componentDidMount(){
        axios.get("http://localhost:5000/logIn")
            .then(res => {
                const userName = res.data;
                this.setState({userName});
                console.log(res.data);
            })
     }

    render() { 
        return (
            <React.Fragment>
                <nav className = "navbar is-primary">
                    <div className = "navbar-end">
                
                        <Link className = "navbar-item" to = "/home">
                            <Icon name='home' size = "large" /><span className = "navFont" >Home</span>
                        </Link>
                        
                        <Link className = "navbar-item" to = "/timeline">
                        <Icon name='time' size = "large" /><span className = "navFont" >Timeline</span>
                        </Link>
                        
                        <div className = "navbar-item has-dropdown is-hoverable"  >
                            <div className = "navbar-link">
                            <Icon name='user circle' size = "large" /><span className = "navFont">{this.state.userName}</span>
                            </div>

                            <div className = "navbar-dropdown">
                                <Link to = "/">
                                    <a className = "navbar-item">
                                    <Icon name='sign out'  size = "large"/><h1 className = "is-size-6">Sign Out</h1>
                                    </a>
                                </Link>
                            </div>
                        </div>
                 </div>  
            </nav>
            <br/>
            </React.Fragment>
          );
    }
}
 
export default navBar;
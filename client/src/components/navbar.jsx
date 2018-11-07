import React, { Component } from 'react';
import { Link } from 'react-router-dom';

//IMPORT SEMANTIC UI
import {Menu} from "semantic-ui-react";

class navBar extends Component {
    state = {  }
    render() { 
        return (
            <React.Fragment>
                <Menu inverted> 
                <Menu.Menu position = "right"> 
                
                    <Link to = "/home">
                        <Menu.Item name = "home">
                            <span className = "navFont">Home</span>
                        </Menu.Item>
                    </Link>
                         
                    <Menu.Item>
                        <span className = "navFont">Character</span>
                    </Menu.Item>
                    
                    <Link to = "/timeline">
                        <Menu.Item>
                            <span className = "navFont">Timeline</span>
                        </Menu.Item>
                    </Link>
                    
                    <Menu.Item>
                        <span className = "navFont">Log In</span>
                    </Menu.Item>
                    
                    </Menu.Menu>
                </Menu>
            </React.Fragment>
          );
    }
}
 
export default navBar;
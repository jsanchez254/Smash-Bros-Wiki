import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import axios from "axios"

import { Icon } from 'semantic-ui-react';

class navBar extends Component {
    state = { 
        userName: " ",
        isAdmin: 0,
        navbar: "navbar is-primary"
     }
    componentDidMount = () =>{
        axios.get("http://localhost:5000/logIn")
            .then(res => {
                const userName = res.data;
                this.setState({userName});
                console.log(res.data);
            })

        setTimeout(this.handleUser(), 500)
     }
     
     handleUser = () =>{
         if(this.state.userName == "HELLO"){
            return (<Redirect to = "/"/>)
         }

        setTimeout(() => {
            console.log("I was called ", this.state.userName);
                const user = {
                    userName: this.state.userName
                }
                axios.post("http://localhost:5000/admin", {user})
                .then(res => {
                    const isAdmin = res.data;
                    this.setState({isAdmin});
                    console.log("IT IS ",this.state.isAdmin);
                })
            }, 500)
     }

     handleAdmin = () =>{
           
            if(this.state.isAdmin){
                return (<span>(ADMIN)</span>)
            }
            else{
                return (<span></span>)
            }
        }
     
    navBarAdmin = ()=>{
        if(this.state.isAdmin){
            return "navbar is-danger";
        }
        
        else{
            return "navbar is-primary";
        }
    }

    handleAdminOptions = ()=>{
        if(this.state.isAdmin){
            return(
            <Link to = "/createCharacter">
                <a className = "navbar-item">
                <Icon name='plus square'  size = "large"/><h1 className = "is-size-6">Add New Character</h1>
                </a>
            </Link>)
        }
    }

    render() { 
        return (
            <React.Fragment>
                {/* {() => this.handleUser} */}
                <nav className = {this.navBarAdmin()}>
                    <div className = "navbar-end">
                
                        <Link className = "navbar-item" to = "/home">
                            <Icon name='home' size = "large" /><span className = "navFont" >Home</span>
                        </Link>
                        
                        <Link className = "navbar-item" to = "/timeline">
                        <Icon name='time' size = "large" /><span className = "navFont" >Timeline</span>
                        </Link>
                        
                        <div className = "navbar-item has-dropdown is-hoverable"  >
                            <div className = "navbar-link">
                            <Icon name='user circle' size = "large" /><span className = "navFont">{this.state.userName} {this.handleAdmin()}</span>
                            </div>

                            <div className = "navbar-dropdown">
                                {this.handleAdminOptions()}
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
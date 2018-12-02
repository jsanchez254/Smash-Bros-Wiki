import React, { Component } from 'react';

//IMPORT SEMANTIC UI
import { Icon } from 'semantic-ui-react'

//IMPORT AXIOS
import axios from "axios";

//import logo
import logo from "../assets/img/smashLogo.png";

class CreateCharacter extends Component {
    state = {
        name:"",
        tier: ["S", "A", "B", "C", "D", "E" ,"F"],
        class: ["Heavy", "Projectile", "Melee", "Swordsman"],
        description: "",
        realTier: "",
        realClass: ""
      }

      handleChange = (event) =>{
        this.setState({[event.target.name]: event.target.value});
        console.log(event.target.value);
        console.log(event.target.name);
      }


      handleSubmit = (event) =>{
        event.preventDefault();
        const newChar= {
            name : this.state.name,
            tier : this.state.realTier,
            class: this.state.realClass,
            description: this.state.description
        }
        axios.post("http://localhost:5000/createCharacter", {newChar})
            .then(res => {
                console.log(res.data)
            })

     }
    render() { 
        return (
            <React.Fragment>
               <section className = "hero is-light is-fullheight">
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
                                                        <label className = "label"> Character Name: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "name" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Name"/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                    </div>

                                                
                                                    <div className = "column is-3">
                                                       
                                                        <label className = "label">Select Tier:</label>
                                                        <div className = "select">
                                                            <select name = "realTier" onChange = {this.handleChange}>
                                                                <option>Select Tier</option>
                                                                { this.state.tier.map((msg, index) => 
                                                                    <option value = {msg[0]} key = {index}>
                                                                        {msg}
                                                                    </option>
                                                                )}
                                                            </select>
                                                        </div>
                                           
                                                    </div>

                                                    <div className = "column is-3">
                                                       
                                                       <label className = "label">Select Class:</label>
                                                       <div className = "select">
                                                           <select name = "realClass" onChange = {this.handleChange}>
                                                               <option>Select Class</option>
                                                               { this.state.class.map((msg, index) => 
                                                                   <option value = {msg} key = {index}>
                                                                       {msg}
                                                                   </option>
                                                               )}
                                                           </select>
                                                       </div>
                                          
                                                   </div>
                                                    
                                                </div>
                                            </div>
                                            <div className="field">
                                            <label className = "label">Add Description:</label>
                                            <article className="media">
                                                <div className="media-content">
                                                <div className="field">
                                                    <p className="control">
                                                        <textarea type ="text" name = "description" className="textarea"
                                                        onChange = {this.handleChange} placeholder="Add Description..."/>
                                                    </p>
                                                </div>
                                                    <nav className="level">
                                                    <div className="level-left">
                                                        <div className="level-item">
                                                        <button type = "submit" value = "Submit" className="button is-warning">Submit</button>
                                                        </div>
                                                    </div>
                                                    </nav>
                                                </div>
                                        </article>
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
 
export default CreateCharacter;
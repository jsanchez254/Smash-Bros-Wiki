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
        realClass: "",
        move1: "",
        move2: "",
        move3: "",
        move4: "",
        franchise: [],
        realFranchise: "",
        game1: "",
        console1: "",
        date1: "",
        game2: "",
        console2: "",
        date2: ""
      }

      componentDidMount(){
          axios.get("http://localhost:5000/getFranchise")
            .then(res =>{       
                    const franchise = res.data;
                    this.setState({franchise});
                    console.log(this.state.franchise[0]);
            })
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
            description: this.state.description,
            move1: this.state.move1,
            move2: this.state.move2,
            move3: this.state.move3,
            move4: this.state.move4,
            franchise: this.state.realFranchise,
            game1: this.state.game1,
            console1:this.state.console1,
            date1: this.state.date1,
            game2: this.state.game2,
            console2:this.state.console2,
            date2: this.state.date2
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


                                                <div className = "field ">
                                                <div className = "columns">
                                                    <div className = "column is-6">
                                                        <label className = "label"> Ultimate: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "move1" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Name"/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                        <label className = "label"> Side Smash: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "move3" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Name"/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                    </div>

                                                
                                                    <div className = "column is-6">
                                                        <label className = "label">B-Attack: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "move2" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Last Name"/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                        <label className = "label"> Recovery: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "move4" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Name"/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                    </div>
                                                    
                                                </div>
                                            </div>
                                            </div>
                                            <div className="field">
                                                <label className = "label">Select Franchise:</label>
                                                        <div className = "select">
                                                            <select name = "realFranchise" onChange = {this.handleChange}>
                                                                <option>Select Franchise</option>
                                                                { this.state.franchise.map((msg, index) => 
                                                                    <option value = {msg[0]} key = {index}>
                                                                        {msg[0]}
                                                                    </option>
                                                                )}
                                                            </select>
                                                    </div>
                                            </div>
                                            <div className = "field ">
                                                <div className = "columns">
                                                    <div className = "column is-6">
                                                        <label className = "label"> Game 1: </label>
                                                        
                                                            <input name = "game1" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Game"/>
                                                                
                                                        
                                                    </div>

                                                
                                                    <div className = "column is-3">
                                                        <label className = "label">Console: </label>
                                                        
                                                            <input name = "console1" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Console"/>
                                                              
                                                        
                                                    </div>

                                                    <div className = "column is-3">
                                                        <label className = "label">Date: </label>
                                                       
                                                            <input name = "date1" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "YYYY-MM-DD"/>
                                                                
                                                        
                                                    </div>
                                                    
                                                </div>
                                            </div>
                                            <div className = "field ">
                                                <div className = "columns">
                                                    <div className = "column is-6">
                                                        <label className = "label"> Game 2: </label>
                                                        
                                                            <input name = "game2" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Game"/>
                                                                
                                                        
                                                    </div>

                                                
                                                    <div className = "column is-3">
                                                        <label className = "label">Console: </label>
                                                        
                                                            <input name = "console2" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Console"/>
                                                              
                                                        
                                                    </div>

                                                    <div className = "column is-3">
                                                        <label className = "label">Date: </label>
                                                       
                                                            <input name = "date2" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "YYYY-MM-DD"/>
                                                                
                                                        
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
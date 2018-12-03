import React, { Component } from 'react';

import axios from "axios";

//import logo
import logo from "../assets/img/smashLogo.png";

class updateCharacter extends Component {
    state = {
        characters: [],
        tier: ["S", "A", "B", "C", "D", "E" ,"F"],
        class: ["Heavy", "Projectile", "Melee", "Swordsman"],
        moves: [],
        description: "",
        realTier: "*",
        realClass: "*",
        character: "",
        char : "",
        move1: "",
        move2: "",
        move3: "",
        move4: ""
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
        console.log(event.target.value);
        if(event.target.name == "character"){
            this.handleChar(event.target.value);
        }
      }

      //HANDLE UPDATES
      handleChar(char1){
        var length = char1.length;
        var tempChar = "";
        for(var i = 0; i < length; i++){
            if(char1[i] == " "){
                tempChar += "_";
                continue;
            }
            tempChar += char1[i];
        }

        axios.get("http://localhost:5000/" + tempChar)
            .then(res => {
                var temp = res.data[0];
                const description = temp[0]
                this.setState({description})
            })
        axios.get("http://localhost:5000/" + tempChar + "/moves")
            .then(res => {
                const moves = res.data;
                const newMoves = moves[0];
                const move1 = newMoves[0];
                const move2 = newMoves[1];
                const move3 = newMoves[2];
                const move4 = newMoves[3];

                this.setState({move1});
                this.setState({move2});
                this.setState({move3});
                this.setState({move4});
                this.setState({moves});
                this.setState({newMoves});
            })
        
        axios.get("http://localhost:5000/" + tempChar + "/tier")
            .then(res => {
                var temp = res.data[0];
                const realTier = temp[0]
                this.setState({realTier});
                console.log(this.state.realTier);
            })
        
        axios.get("http://localhost:5000/" + tempChar + "/class")
            .then(res => {
                var temp = res.data[0];
                const realClass = temp[0]
                this.setState({realClass});
            })
      }


      handleSubmit = (event) =>{
        event.preventDefault();
        const char= {
            character : this.state.character,
            tier : this.state.realTier,
            class: this.state.realClass,
            description: this.state.description,
            move1: this.state.move1,
            move2: this.state.move2,
            move3: this.state.move3,
            move4: this.state.move4
        }
        axios.post("http://localhost:5000/updateChar", {char})
            .then(res => {
                console.log(res.data)
            })

     }

    render() { 
        return (
            <React.Fragment>
             
               <section className = "hero is-primary is-fullheight">
                        <div className  ="hero-body"> 
                            <div className = "container">
                                <div className = "columns is-centered">
                                    <div className = "column is-8">
                                        <form onSubmit = {this.handleSubmit} className = "box">
                                            <div className="field has-text-centered">
                                                <img src= {logo} width="167"/>
                                            </div>
                                            <div className  ="field">  
                                                <div className = "columns">
                                                    <div className = "column is-5">
                                                    <label className = "label">Select Character to Edit:</label>
                                                        <div className = "select">
                                                                <select name = "character" onChange = {this.handleChange}>
                                                                    <option>Edit Character</option>
                                                                    { this.state.characters.map((msg, index) => 
                                                                        <option  value = {msg[0]} key = {index}>
                                                                            {msg[0]}
                                                                        </option>
                                                                    )}
                                                                </select>
                                                        </div>
                                                    </div>

                                                
                                                    <div className = "column is-3">
                                                        
                                                        <label className = "label">Select Tier:</label>
                                                        <div className = "select">
                                                            <select name = "realTier" onChange = {this.handleChange}>
                                                                <option>{this.state.realTier}</option>
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
                                                              <option>{this.state.realClass}</option>
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
                                                            } placeholder = "Enter Name" value = {this.state.move1}/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                        <label className = "label"> Side Smash: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "move3" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Name" value = {this.state.move3}/>
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
                                                            } placeholder = "Enter Last Name" value = {this.state.move2}/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
                                                        <label className = "label"> Recovery: </label>
                                                        <div className = "control has-icons-left">
                                                            <input name = "move4" className = "input"
                                                            onChange = {this.handleChange
                                                            } placeholder = "Enter Name" value = {this.state.move4}/>
                                                                <span className = "icon is-small is-left">
                                                                    <i className="fas fa-envelope"></i>
                                                                </span>
                                                        </div>
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
                                                        onChange = {this.handleChange} placeholder="Add Description..."
                                                        value = {this.state.description}/>
                                                    </p>
                                                </div>
                                                    <nav className="level">
                                                    <div className="level-left">
                                                        <div className="level-item">
                                                        <button type = "submit" value = "Submit" className="button is-warning">UPDATE</button>
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
 
export default updateCharacter;
import React, { Component } from 'react';

import axios from "axios";

//import semantic ui
import {Button} from "semantic-ui-react";

//IMPORT IMAGE
import Fox1 from "../assets/img/Character_Pics/Fox_SSBU.png";

//IMPORT COMMENTBOX
import WriteComment from "../components/writeComment";

class Fox extends Component {
    state = {
        content: "",
        moves: [],
        newMoves: [],
        tier: "",
        class1: "",
        dislike: "",
        like: ""
      }
      componentDidMount(){
        axios.get("http://localhost:5000/Fox")
            .then(res => {
                const content = res.data;
                this.setState({content})
            })

        axios.get("http://localhost:5000/Fox/moves")
            .then(res => {
                const moves = res.data;
                const newMoves = moves[0];
                this.setState({moves});
                this.setState({newMoves});
            })
        
        axios.get("http://localhost:5000/Fox/tier")
            .then(res => {
                const tier = res.data;
                this.setState({tier});
            })
        
        axios.get("http://localhost:5000/Fox/class")
            .then(res => {
                const class1 = res.data;
                this.setState({class1});
            })
        
        axios.get("http://localhost:5000/Fox/like")
            .then(res => {
                const like = res.data;
                this.setState({like});
            })

        axios.get("http://localhost:5000/Fox/dislike")
        .then(res => {
            const dislike = res.data;
            this.setState({dislike});
        })

  }
    render() { 
        return (
            <React.Fragment>
            <div className = "columns">
                <div className = "column is-5">
                    <div className = "charImg">
                        <img src = {Fox1}/>
                    </div>
                    <div className = "columns">
                        <div className = "column is-4">
                            <Button
                            color = "blue"
                            content = ""
                            icon = "thumbs up"
                            label = {{basic: true, color: "blue", pointing: "left", content: this.state.like}}
                            />
                        </div>
                        <div className = "column is-4 is-offset-1">
                            <Button
                            color = "red"
                            content = ""
                            icon = "thumbs down"
                            label = {{basic: true, color: "red", pointing: "left", content: this.state.dislike}}
                            />
                        </div>
                    </div>
                </div>
                <div className = "column is-5 is-offset-1">
                    <h1 className = "title">Fox</h1>
                    <div>
                        {this.state.content}
                    </div>
                    
                    <br/>
                    <center> <h1 className = "title">Tier:</h1> </center>
                        <div className = "tier">{this.state.tier}</div>
                    <br/>
                    <center><h1 className = "title">Class:</h1></center>
                        <div className = "class1">{this.state.class1}</div>
                    <br/>
                    <h1 className = "title">Moves:</h1>
                    <table className = "table">
                        <thead>
                            <tr>
                                <th>Ultimate</th>
                                <th>Side Smash</th>
                                <th>B-Attack</th>
                                <th>Recovery</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                {this.state.newMoves.map((move, index) => <td key = {index}> {move} </td>)}
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <WriteComment character = "Fox"/>
        </React.Fragment>
          );
    }
}
 
export default Fox;
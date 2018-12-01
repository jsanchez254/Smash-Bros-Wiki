import React, { Component } from 'react';
import axios from "axios";

//import semantic ui
import {Button} from "semantic-ui-react";

//IMPORT IMAGE
import ike from "../assets/img/Character_Pics/Ike_SSBU.png";

//IMPORT COMMENTBOX
import WriteComment from "../components/writeComment";

class Ike extends Component {
    state = {
        content: "",
        moves: [],
        newMoves: [],
        tier: "",
        class1: "",
        dislike: "",
        like: "",
        letLike: false,
        userName: "",
        whatLike: true
      }
      
      componentDidMount(){
            axios.get("http://localhost:5000/logIn")
            .then(res => {
                const userName = res.data;
                this.setState({userName});
            })


            axios.get("http://localhost:5000/Ike")
                .then(res => {
                    const content = res.data;
                    this.setState({content})
                })
            
            axios.get("http://localhost:5000/Ike/moves")
                .then(res => {
                    const moves = res.data;
                    const newMoves = moves[0];
                    this.setState({moves});
                    this.setState({newMoves});
                })
            
            axios.get("http://localhost:5000/Ike/tier")
                .then(res => {
                    const tier = res.data;
                    this.setState({tier});
                })
            
            axios.get("http://localhost:5000/Ike/class")
                .then(res => {
                    const class1 = res.data;
                    this.setState({class1});
                })
            
            axios.get("http://localhost:5000/Ike/like")
                .then(res => {
                    const like = res.data;
                    this.setState({like});
                })

            axios.get("http://localhost:5000/Ike/dislike")
            .then(res => {
                const dislike = res.data;
                this.setState({dislike});
            })
      }

      HandleLike = () =>{
        setTimeout(() => {
            if(!this.state.letLike){
                const like = +this.state.like + 1;
                const whatLike = true;
                this.setState({whatLike});
                this.setState({like}); 
                this.HandleUpdateOfLikes();
            }
        }, 350);
    }
      

      HandleDislike = () =>{
        setTimeout(() => {
            if(!this.state.letLike){
                const dislike = +this.state.dislike + 1;
                const whatLike = false;
                this.setState({whatLike});
                this.setState({dislike}); 
                this.HandleUpdateOfLikes();
            }
        }, 350);
    }
     

    HandleUpdateOfLikes = () =>{
        var check;
        if(this.state.whatLike){
            check= {
                userName: this.state.userName,
                character: "Ike",
                like: 1,
                dislike: 0
            };
        }
        else{
            check= {
                userName: this.state.userName,
                character: "Ike",
                like: 0,
                dislike: 1
            };
        }
        axios.post("http://localhost:5000/updateLikes", {check})
            .then(res => {
                console.log(res.data);
            })
    }

     //makes sure that user cannot like or dislike something twice
     HandleCheckLikeStatus = (funcion) =>{
        const check= {
            userName: this.state.userName,
            character: "Ike"
        };

        axios.post("http://localhost:5000/checkLikeStatus", {check})
        .then(res =>{
            const letLike = res.data;
            this.setState({letLike})
        })

        if(funcion == "dislike"){
            this.HandleDislike();
        }

        else{
            this.HandleLike();
           
        }

     }


    render() { 
        return (
            <React.Fragment>
                <div className = "columns">
                    <div className = "column is-5">
                        <div className = "charImg">
                            <img src = {ike}/>
                        </div>
                        <div className = "columns">
                            <div className = "column is-4">
                                <Button onClick = {() => this.HandleCheckLikeStatus("like")}
                                color = "blue"
                                content = ""
                                icon = "thumbs up"
                                label = {{basic: true, color: "blue", pointing: "left", content: +this.state.like}}
                                />
                            </div>
                            <div className = "column is-4 is-offset-1">
                                <Button onClick = {() => this.HandleCheckLikeStatus("dislike")}
                                color = "red"
                                content = ""
                                icon = "thumbs down"
                                label = {{basic: true, color: "red", pointing: "left", content: this.state.dislike}}
                                />
                            </div>
                        </div>
                    </div>
                    <div className = "column is-5 is-offset-1">
                        <h1 className = "title">Ike</h1>
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
                <WriteComment character = "Ike"/>
            </React.Fragment>
          );
    }
}
 
export default Ike;
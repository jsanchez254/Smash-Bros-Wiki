import React, { Component } from 'react';
import axios from "axios";

//import semantic ui
import {Button} from "semantic-ui-react";

//IMPORT IMAGE
import bayonetta from "../assets/img/Character_Pics/Bayonetta_SSBU.png";

//IMPORT COMMENTBOX
import WriteComment from "../components/writeComment";

class Bayonetta extends Component {
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
        whatLike: true,
        games: [],
        franchise: ""
      }
      
      componentDidMount(){
            axios.get("http://localhost:5000/Bayonetta/getFranchise")
            .then(res => {
                const franchise = res.data;
                this.setState({franchise});
            })

            axios.get("http://localhost:5000/Bayonetta/getGames")
            .then(res => {
                const games = res.data;
                this.setState({games});
            })


            axios.get("http://localhost:5000/logIn")
            .then(res => {
                const userName = res.data;
                this.setState({userName});
            })


            axios.get("http://localhost:5000/Bayonetta")
                .then(res => {
                    const content = res.data;
                    this.setState({content})
                })
            
            axios.get("http://localhost:5000/Bayonetta/moves")
                .then(res => {
                    const moves = res.data;
                    const newMoves = moves[0];
                    this.setState({moves});
                    this.setState({newMoves});
                })
            
            axios.get("http://localhost:5000/Bayonetta/tier")
                .then(res => {
                    const tier = res.data;
                    this.setState({tier});
                })
            
            axios.get("http://localhost:5000/Bayonetta/class")
                .then(res => {
                    const class1 = res.data;
                    this.setState({class1});
                })
            
            axios.get("http://localhost:5000/Bayonetta/like")
                .then(res => {
                    const like = res.data;
                    this.setState({like});
                })

            axios.get("http://localhost:5000/Bayonetta/dislike")
            .then(res => {
                const dislike = res.data;
                this.setState({dislike});
            })
      }

      //NEW
      HandleLike = () =>{
        setTimeout(() => {
            if(!this.state.letLike){
                const like = +this.state.like + 1;
                const whatLike = true;
                this.setState({whatLike});
                this.setState({like}); 
                this.HandleUpdateOfLikes();
                console.log("hello like ", this.state.letLike );
            }
        }, 1000);
    }
      

      HandleDislike = () =>{
        setTimeout(() => {
            if(!this.state.letLike){
                const dislike = +this.state.dislike + 1;
                const whatLike = false;
                this.setState({whatLike});
                this.setState({dislike}); 
                this.HandleUpdateOfLikes();
                console.log("hello dislike ", this.state.letLike );
            }
        }, 1000);
    }
     

    HandleUpdateOfLikes = () =>{
        var check;
        if(this.state.whatLike){
            check= {
                userName: this.state.userName,
                character: "Bayonetta",
                like: 1,
                dislike: 0
            };
        }
        else{
            check= {
                userName: this.state.userName,
                character: "Bayonetta",
                like: 0,
                dislike: 1
            };
        }
        axios.post("http://localhost:5000/updateLikes", {check})
            .then(res => {
                console.log(res.data);
            })
    }
    //UNTIL HERE

     //makes sure that user cannot like or dislike something twice
     HandleCheckLikeStatus = (funcion) =>{
        const check= {
            userName: this.state.userName,
            character: "Bayonetta"
        };

        axios.post("http://localhost:5000/checkLikeStatus", {check})
        .then(res =>{
            const letLike = res.data;
            this.setState({letLike})
            console.log("Hello", this.state.letLike);
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
                            <img src = {bayonetta}/>
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
                        <br/>
                        <br/>
                        <br/>
                        <br/>
                        <h1 className = "title">Franchise:</h1>
                        <span className = "franchise">{this.state.franchise}</span>
                    </div>
                    <div className = "column is-5 is-offset-1">
                        <h1 className = "charTitle">Bayonetta</h1>
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
                        <h1 className = "title">Game Apparitions:</h1>
                        <table className = "table">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Console</th>
                                    <th>Release Date</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        { this.state.games.map((msg, index) => <h1 key = {index}>{msg[0]}</h1> )}  
                                    </td>                                        
                                    <td>
                                        { this.state.games.map((msg, index) => <h1 key = {index}>{msg[1]}</h1> )}   
                                    </td> 
                                    <td>
                                        { this.state.games.map((msg, index) => <h1 key = {index}>{msg[2]}</h1> )}   
                                    </td>                                      
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <h1 className = "title">Comments</h1>
                <WriteComment character = "Bayonetta"/>
            </React.Fragment>
          );
    }
}
 
export default Bayonetta;
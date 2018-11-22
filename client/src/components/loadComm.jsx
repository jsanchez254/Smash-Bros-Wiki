import React, { Component } from 'react';
import axios from "axios";

import LoadCommDef from './loadCommentDefinitive';

class loadComm extends Component {
    state = {
        usersComments: []
      }

      componentDidMount(){
        if(this.props.character == "Toon Link")
            axios.get("http://localhost:5000/Toon_Link/comments")
                .then(res => {
                    const usersComments = res.data;
                    console.log(usersComments);
                    this.setState({usersComments});
                })
        else if(this.props.character == "Ike")
        axios.get("http://localhost:5000/Ike/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })
        else if(this.props.character == "Bayonetta")
        axios.get("http://localhost:5000/Bayonetta/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })

      }

    render() { 
        return (  
            <React.Fragment>
                {this.state.usersComments.map((user, index) => <LoadCommDef key = {index} userName = {user[0]} 
                    comment = {user[1]}/> )}
            </React.Fragment>
        );
    }
}
 
export default loadComm;
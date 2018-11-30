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
        else if(this.props.character == "Snake")
        axios.get("http://localhost:5000/Snake/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })
        else if(this.props.character == "Samus")
        axios.get("http://localhost:5000/Samus/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })

        else if(this.props.character == "Falco")
        axios.get("http://localhost:5000/Falco/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })

        else if(this.props.character == "Fox")
        axios.get("http://localhost:5000/Fox/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })

        else if(this.props.character == "Link")
        axios.get("http://localhost:5000/Link/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })

        else if(this.props.character == "Lucina")
        axios.get("http://localhost:5000/Lucina/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })

        else if(this.props.character == "Piranha Plant")
        axios.get("http://localhost:5000/Piranha_Plant/comments")
            .then(res => {
                const usersComments = res.data;
                console.log(usersComments);
                this.setState({usersComments});
            })

        else if(this.props.character == "Young Link")
        axios.get("http://localhost:5000/Young_Link/comments")
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
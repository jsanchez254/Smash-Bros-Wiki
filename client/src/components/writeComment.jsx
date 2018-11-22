import React, { Component } from 'react';
import axios from "axios";

import LoadComm from "./loadComm"
import { Divider } from 'semantic-ui-react'

class writeComment extends Component {
    state = { 
        comment: "",
        userName: ""
     }

     componentDidMount(){
        axios.get("http://localhost:5000/logIn")
        .then(res => {
            const userName = res.data;
            this.setState({userName});
        })
     }

     handleChange = (event) => {
         this.setState({comment: event.target.value});
     }

     handleSubmit = (event) => {
         event.preventDefault();

         const blog ={
             comment: this.state.comment,
             character: this.props.character,
             userName: this.state.userName
         };

     axios.post("http://localhost:5000/blog", {blog})
        .then(res => {
          
        })
        console.log(blog.comment);
    }

    loadComments(){
        return (<LoadComm character = {this.props.character}/>);
    }

    render() { 
        return (
        <React.Fragment>
            <form onSubmit ={this.handleSubmit}>
            <article className="media">
                <div className="media-content">
                    <div className="field">
                    <p className="control">
                        <textarea type ="text" name = "comment" className="textarea"
                         onChange = {this.handleChange} placeholder="Add a comment..."/>
                    </p>
                    </div>
                    <nav className="level">
                    <div className="level-left">
                        <div className="level-item">
                        <button type = "submit" value = "Submit" className="button is-success">Submit</button>
                        </div>
                    </div>
                    </nav>
                </div>
            </article>
            </form>
            <Divider/>
            {this.loadComments()}
        </React.Fragment>
        );
    }
}
 
export default writeComment;
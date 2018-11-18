import React, { Component } from 'react';
import axios from "axios";

import LoadComm from "./loadComm"
import { Divider } from 'semantic-ui-react'

class writeComment extends Component {
    state = { 
        comment: ""
     }

     handleChange = (event) => {
         this.setState({comment: event.target.value});
     }

     handleSubmit = (event) => {
         event.preventDefault();

         const blog ={
             comment: this.state.comment
         };

     axios.post("http://localhost:5000/register", {blog})
        .then(res => {
            console.log(res);
            console.log(res.data);
        })
        console.log(blog.comment);
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
            <LoadComm character = {this.props.character}/>
        </React.Fragment>
        );
    }
}
 
export default writeComment;
import React, { Component } from 'react';

class writeComment extends Component {
    state = {  }
    render() { 
        return (
        <React.Fragment>
            <article className="media">
                <div className="media-content">
                    <div className="field">
                    <p className="control">
                        <textarea className="textarea" placeholder="Add a comment..."></textarea>
                    </p>
                    </div>
                    <nav className="level">
                    <div className="level-left">
                        <div className="level-item">
                        <a className="button is-success">Submit</a>
                        </div>
                    </div>
                    </nav>
                </div>
            </article>
        </React.Fragment>
        );
    }
}
 
export default writeComment;
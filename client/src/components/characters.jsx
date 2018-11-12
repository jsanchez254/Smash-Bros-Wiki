import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Characters extends Component {
    state = {  }
    render() { 
        return (
            <React.Fragment>
                <Link to = {"/" + this.props.character}>
                    <div className = "column is-3">
                        <div className = "character"> 
                            {this.props.character}
                        </div>
                    </div>
                </Link>
            </React.Fragment>
          );
    }
}
 
export default Characters;
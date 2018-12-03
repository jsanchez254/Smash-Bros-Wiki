import React, { Component } from 'react';

class LoadCommDef extends Component {
    state = {  }
    render() { 
        return (
            <React.Fragment>
                <div className = "comment1">
                    <div className="media-content">
                        <div className="content">
                            <p>
                                <div className = "commBox">
                                    <strong>{this.props.userName}</strong>
                                    <br/>
                                        {this.props.comment}
                                    <br/>
                                </div>
            
                            </p>
                        </div>
                    </div>
                </div>
            </React.Fragment>
          );
    }
}
 
export default LoadCommDef;
import React, { Component } from 'react';

class LoadCommDef extends Component {
    state = {  }
    render() { 
        return (
            <React.Fragment>
                <div className="media-content">
                    <div className="content">
                        <p>
                            <strong>{this.props.userName}</strong>
                            <br/>
                                {this.props.comment}
                            <br/>
        
                        </p>
                    </div>
                </div>
            </React.Fragment>
          );
    }
}
 
export default LoadCommDef;
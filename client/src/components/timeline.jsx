import React, { Component } from 'react';

import axios from "axios";


class timeline extends Component {
    state = {
        timeChar: []
      }
    
    componentDidMount(){
        axios.get("http://localhost:5000/getTimeline")
            .then(res => {
                const timeChar = res.data;
                this.setState({timeChar});
                console.log(this.state.timeChar);
            })
    }

    render() { 
        return (
            <React.Fragment>
                {/* <center><div className = "divider1"></div></center> */}
                <table className = "table">
                    <thead>
                        <tr>
                            <th>Character</th>
                            <th>First Appearence</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                            { this.state.timeChar.map((msg, index) => <h1 key = {index}>{msg[0]}</h1> )}  
                            </td>                                        
                            <td>
                            { this.state.timeChar.map((msg, index) => <h1 key = {index}>{msg[1]}</h1> )}   
                            </td>                                       
                        </tr>
                    </tbody>
                </table>
            </React.Fragment>
          );
    }
}
 
export default timeline;
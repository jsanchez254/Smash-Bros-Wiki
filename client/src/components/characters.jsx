import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import FireEmblemSymbol from "../assets/img/Franchise_Icons/FireEmblemSymbol.svg"
import FinalFantasySymbol from "../assets/img/Franchise_Icons/FinalFantasySymbol.svg"
import BayonettaSymbol from "../assets/img/Franchise_Icons/BayonettaSymbol.svg"
import MegaManSymbol from "../assets/img/Franchise_Icons/MegaManSymbol.svg"
import MetalGearSymbol from "../assets/img/Franchise_Icons/MetalGearSymbol.svg"
import PokemonSymbol from "../assets/img/Franchise_Icons/PokemonSymbol.svg"
import ZeldaSymbol from "../assets/img/Franchise_Icons/ZeldaSymbol.svg"
import StarFoxSymbol from "../assets/img/Franchise_Icons/StarFoxSymbol.svg"
import MarioSymbol from "../assets/img/Franchise_Icons/MarioSymbol.svg"
import MetroidSymbol from "../assets/img/Franchise_Icons/MetroidSymbol.svg"


class Characters extends Component {
    state = {
     }

     handleImage(char){
        if(this.props.character == "Ike" || this.props.character == "Lucina" ||
        this.props.character == "Corrin"){
            return FireEmblemSymbol;
        }
        else if(this.props.character == "Link" || this.props.character == "Toon Link" ||
         this.props.character == "Young Link" ){
            return ZeldaSymbol;
        }

        else if (this.props.character == "Falco" || this.props.character == "Fox"){
            return StarFoxSymbol;
        }

        else if (this.props.character == "Pikachu" || this.props.character == "Greninja"){
            return PokemonSymbol;
        }

        else if (this.props.character == "Bayonetta"){
            return BayonettaSymbol;
        }

        else if (this.props.character == "Snake"){
            return MetalGearSymbol;
        }

        else if (this.props.character == "Cloud"){
            return FinalFantasySymbol;
        }

        else if (this.props.character == "Mega Man"){
            return MegaManSymbol;
        }

        else if (this.props.character == "Piranha Plant"){
            return MarioSymbol;
        }

        else if (this.props.character == "Samus"){
            return MetroidSymbol;
        }

        else{
            return MegaManSymbol;
        }

     }

    render() { 
        return (
            <React.Fragment>
                <Link to = {"/" + this.props.character}>
                    <div className = "column is-3">
                        <div className = "character"> 
                            {this.props.character}
                            <img src = {this.handleImage(this.props.character)}/>
                        </div>
                    </div>
                </Link>
            </React.Fragment>
          );
    }
}
 
export default Characters;
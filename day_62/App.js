import React from "react";

import { useState,useEffect } from "react";
import  MovieCard  from "./MovieCard";
import './App.css';
import SearchIcon from './search.svg'


// 46d856f8 

const API_URL='http://www.omdbapi.com?apikey=46d856f8'

const App =()=>{
    const [searchTerm,setsearchTerm]=useState("");
    const [movies,setmovies] =useState([]);  
    useEffect(
        ()=> {
            searchMovies('Batman')
        },[]
    );
    const searchMovies=async(title)=>{
        const response = await fetch(`${API_URL}&s=${title}`)
        const data = await response.json();
        setmovies(data.Search)
    };
    
    return(
        <div className="app">
            <h1>MovieFlix</h1>
            <div className="search">
                <input value={searchTerm}
                    onChange={(e)=>setsearchTerm(e.target.value)}
                    placeholder="Search for movies"
                />
                <img src= {SearchIcon} alt="Search icon" 
                onClick={()=>searchMovies(searchTerm)} />

            </div>
            {
                movies.length > 0 ? (
                <div className="container">
                    {movies.map((movie)=>(<MovieCard movie={movie}/>
                    ))}
                </div>):(
                <div>
                    <h2>Movies Not Found !</h2>
                </div>
            )
            }
        
        </div>
    );
}

export default App;
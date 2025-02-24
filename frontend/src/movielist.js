import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MovieList = () => {
    const [movies, setMovies] = useState([]);  // State to store movies

    // Fetch movies from the Django backend
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/movies/')  // Django API endpoint
            .then(response => {
                setMovies(response.data);  // Update state with fetched movies
            })
            .catch(error => {
                console.error("Error fetching movies:", error);
            });
    }, []);  // Empty dependency array ensures this runs only once

    return (
        <div>
            <h1>Movie List</h1>
            <ul>
                {movies.map(movie => (
                    <li key={movie._id}>
                        <h2>{movie.title}</h2>
                        <p><strong>Genre:</strong> {movie.genre}</p>
                        <p><strong>Rating:</strong> {movie.rating}</p>
                        <p><strong>Release Date:</strong> {movie.release_date}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MovieList;
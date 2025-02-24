import React from 'react';
import MovieList from './movielist';  // Import the MovieList component

function App() {
    return (
        <div>
            <h1>Movie Recommendation System</h1>
            <MovieList />  {/* Render the MovieList component */}
        </div>
    );
}

export default App;
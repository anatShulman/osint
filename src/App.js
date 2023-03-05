import FullPage from './Components/FullPage';
import './App.module.css'
import images from "./images.jpg";
import React from 'react';
import Register from './Components/Register';
import Login from './Components/Login';

const App = () => {
  return (
    <div>
        <img className="AppBackground" src={images} alt={""} />
        <FullPage />
      </div>
  );
}

export default App;



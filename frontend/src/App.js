import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from "./components/ui/provider";

import Login from './routes/login';

import './App.css';


function App() {
  return (
    <Provider>
      <Router>
        <div className="App">
          <Routes>
            <Route path="/login" element={<Login />} />

            <Route path="/" element={<h1>Welcome to jakNajtaniej</h1>} />
          </Routes>
        </div>
      </Router>
    </Provider>
  );
}

export default App;

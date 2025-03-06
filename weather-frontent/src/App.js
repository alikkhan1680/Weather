import './App.css';
import {AuthProvider} from "./components/AuthContext"
import React, {lazy } from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";


const Home = lazy(()=> import("./components/Home"))
const Login = lazy(()=> import("./components/login"))
const Registration = lazy(()=> import("./components/registration"))
const Logoute = lazy(()=> import("./components/logoute"))

function App() {
  return (
      <AuthProvider>
          <BrowserRouter>
              <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="login" element={<Login />} />
                <Route path="registration" element={<Registration />} />
                <Route path='logout' element={<Logoute/>}/>
              </Routes>
            </BrowserRouter>
      </AuthProvider>      
   
  );
}


export default App;



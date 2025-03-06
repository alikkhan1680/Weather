import '../App.css';
import './style.css'
import { useNavigate, useLocation } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useContext } from 'react';
import { AuthContext } from './AuthContext';




import latitude from "../img/latitude.jpeg";
import weather from "../img/weather.webp";
import { LuCloudy } from "react-icons/lu";
import { PiWindDuotone } from "react-icons/pi";
import { LiaTemperatureHighSolid } from "react-icons/lia";




function Home () {
    const [countryName, setCountryName] = useState('');
    const [countryData, setCountryData] = useState({});
    const {userData} = useContext(AuthContext);
    const navigate = useNavigate()


  const handleCountry = async (e) => {
    e.preventDefault();

    if (!countryName) {
      console.error("Country name kiritilmadi!");
      return;
    }

    const requestData = { country_Name: countryName }; 

    try {
      const response = await fetch("http://127.0.0.1:8000/country-data/", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(requestData),
      });

      if (response.ok) {
        const data = await response.json();
        setCountryData(data); // Set countryData to the response
        setCountryName("")
      } else {
        console.log("Xatolik yuzaga keldi, status:", response.status);
      }
    } catch (err) {
      console.error("Catch xatoligi:", err);
    }
  };

    return (
        <div className="App">
<div class="auth">
  <div>
        {userData ? 
        (
        <div>
          <h3>@{userData.user_data.username}</h3>
          <b>{userData.user_data.first_name}</b>
          <b>{userData.user_data.last_name}</b>
        </div>
          )
         : 
        (<b>Siz hali ro'yhatdan o'tmagansiz</b>)
        }
  </div>
  <div>
    <b className="link_auth"  onClick={()=> navigate('/registration')} >Registration</b>
    <b className='link_auth' onClick={()=> navigate('/login')} >Login</b>
    <b className='link_auth' onClick={()=> navigate('/logout')}>logoute</b>
  </div>
</div>

<div className='container'>
  <h1>WOrld Weather</h1>

  <div className='img_G'>
    <img src={latitude} alt="Weather" />
  </div>

  <div className='weather-info'>

    <p>Poytaxt: <img className='latitude_img' src={latitude} alt="Lat" /> 
      <b>{countryData?.name || 'N/A'}</b> 
    </p>

    <p>Country: <img className='latitude_img' src={latitude} alt="Lat" /> 
      <b>{countryData?.country || 'N/A'}</b> 
    </p>

    <p>Latitude: <img className='latitude_img' src={latitude} alt="Lat" /> 
      <b>{countryData?.lat || 'N/A'}</b> 
    </p>

    <p>Longitude: <img className='latitude_img' src={latitude} alt="Lat" /> 
      <b>{countryData?.lon || 'N/A'}</b> 
    </p>

    <p>Wind kph: <PiWindDuotone />
      <b style={{color: countryData?.wind_color || "black"}}>{countryData?.wind_kph || 'N/A'}</b> 
    </p>

    <p>Cloud: <LuCloudy />
      <b style={{color: countryData?.cloud_color || "black"}}>{countryData?.cloud || 'N/A'}</b> 
    </p>

    <p>Temp °C: <LiaTemperatureHighSolid /> 
      <b style={{color: countryData?.temp_color || "black"}}>{countryData?.temp_c || 'N/A'}</b>
    </p>

  </div>

  <div className='input'>
    <b>Country Name:</b>
    <form onSubmit={handleCountry}>
      <input
        placeholder='Country'
        value={countryName}
        onChange={(e) => setCountryName(e.target.value)}
      />
    </form>
  </div>
</div>
      </div>
    )
}

export default Home;
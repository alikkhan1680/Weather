import './style.css'
import { useNavigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';
import { useContext } from 'react';






function Logoute (){
    const navigate = useNavigate();
    const {userData, setUserData} = useContext(AuthContext);

    
    const handleLogout = async () => {
        const refreshToken = localStorage.getItem("refresh_token");
    
        await fetch("http://127.0.0.1:8000/logoute/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ refresh_token: refreshToken }),
        });
    
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        localStorage.clear()
        setUserData(null)
        navigate("/")
    };
    
    return (
        <div className="logoute">
            <h1>Rostan ham Tizimdan chiqishni Xoxlaysizmi </h1>
            <button onClick={handleLogout} className="logoute-button">Logoute qilish</button>
        </div>
    )
}

export default Logoute;
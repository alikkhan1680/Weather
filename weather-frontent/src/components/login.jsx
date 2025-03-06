import "./style.css";
import { useState, useContext} from "react";
import { TbXboxX } from "react-icons/tb";
import { useNavigate } from 'react-router-dom';
import {AuthContext} from "./AuthContext"





function Login() {
    const navigate = useNavigate()
    const {setUserData}  = useContext(AuthContext)
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch("http://127.0.0.1:8000/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                throw new Error("Login xato! Username yoki parol noto‘g‘ri.");
            }
            const data = await response.json();
            setUserData(data);
            localStorage.setItem("user", JSON.stringify(data)); // LocalStorage-ga saqlash
            setUsername("")
            setPassword("")
            setError("");
            navigate("/")
        } catch (err) {
            setError(err.message);
        }
    };


    return (
        <div className="login_box">
            <TbXboxX style={{fontSize:"40px"}} onClick={()=> navigate("/")}/>
            <h1>Login</h1>
            <form onSubmit={handleLogin}>
                <input
                    className="inpt"
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    className="inpt"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button className="submit" type="submit">
                    Login
                </button>
            </form>

            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
}

export default Login;

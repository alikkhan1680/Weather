import "./style.css"
import { useNavigate } from 'react-router-dom';
import { TbXboxX } from "react-icons/tb";
import { useState } from "react";
import { AuthContext } from './AuthContext';
import { useContext } from 'react';




function Registration(){
    const navigate = useNavigate()
    const [username, setuserName] = useState("")
    const [first_name, setfirstName] = useState("")
    const [last_name, setlastName] = useState("")
    const [password, setpassword] = useState("")
    const [error, seterr] = useState("")
    const [success, setSuccess] = useState(false); // Yangi holat qo'shildi
    const {userData, setUserData} = useContext(AuthContext);// AuthContext dan userdatalarni saqlaydi




    const handelRegister = async (e) => {
        e.preventDefault();        
        setSuccess(false); // Har bir urinishda successni false qilish



        
        try {
            const response = await fetch("http://127.0.0.1:8000/register/", {
                method : "POST",
                headers : {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({username, first_name, last_name, password}),
            });

            if (!response.ok) {
                throw new Error("Registration Xatolik bor! qaysidir qatorda xatolik mavjud ")
            }
                const data = await response.json();
                localStorage.setItem("user", JSON.stringify(data)); // LocalStorage-ga saqlash
                setUserData(data)
                setSuccess(true);
                setuserName("")
                setfirstName("")
                setlastName("")
                setpassword("")
                seterr("")
                return ("siz muofaqiyatli ro'hattan o'tingiz")
        } catch (err) {
            seterr(err.massage);
        }
    };
    return(
               <div className="login_box">
                    <TbXboxX style={{fontSize:"40px"}} onClick={()=> navigate("/")}/>
                    <h1>Registration</h1>
                    <form onSubmit={handelRegister}>
                        <input
                            className="inpt"
                            type="text"
                            placeholder="Username"
                            value={username}
                            onChange={(e) => setuserName(e.target.value)}
                            required
                          />

                        <input 
                            className="inpt" 
                            type="text"
                            placeholder="firstName"
                            value={first_name}
                            onChange={(e) => setfirstName(e.target.value)}
                            required
                         />
                
                        <input 
                            className="inpt" 
                            type="text"
                            placeholder="LastName"
                            value={last_name}
                            onChange={(e) => setlastName(e.target.value)}
                            required
                        />
                        <input 
                            className="inpt" 
                            type="text"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setpassword(e.target.value)}
                            required
                        />
                        <button className="submit" type="submit" >Registration</button>
                    </form>  
                    {error && <p style={{ color: "red" }}>{error}</p>}
                    {success && <p style={{ color: "green", fontWeight: "bold" }}>Muofaqiyatli Ro'yhatdan o'tdingiz</p>} {/* Success xabari */}
  
                </div>    
    )
}

export default Registration
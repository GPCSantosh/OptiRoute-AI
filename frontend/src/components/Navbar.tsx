import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {

    const { logout } = useAuth();

    const navigate = useNavigate();

    function handleLogout() {

        logout();

        navigate("/");

    }

    return (

        <div
            style={{
                height:70,
                background:"#f8fafc",
                display:"flex",
                justifyContent:"space-between",
                alignItems:"center",
                padding:"0 30px"
            }}
        >

            <h3>Dashboard</h3>

            <button
                onClick={handleLogout}
                style={{
                    background:"#ef4444",
                    color:"white",
                    border:"none",
                    padding:"10px 20px",
                    borderRadius:8,
                    cursor:"pointer"
                }}
            >
                Logout
            </button>

        </div>

    );

}
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../../api/auth";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();

    const handleLogin = async () => {
        console.log("Button clicked");

        try {
            console.log(email, password);

            const data = await login(email, password);

            console.log(data);

            localStorage.setItem(
                "token",
                data.access_token
            );

            navigate("/dashboard");
        } catch (err: any) {
            console.log(err);

            console.log(err.response);

            console.log(err.response?.data);

            alert(
                JSON.stringify(err.response?.data || err.message)
            );
        }
    };

    return (
        <div
            style={{
                width: 420,
                background: "#1e293b",
                padding: 40,
                borderRadius: 12,
                color: "white",
                boxShadow: "0 0 20px rgba(0,0,0,.4)",
            }}
        >
            <h1 style={{ marginBottom: 10 }}>
                OptiRoute AI
            </h1>

            <p
                style={{
                    color: "#94a3b8",
                    marginBottom: 30,
                }}
            >
                Smart Route Optimization Platform
            </p>

            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) =>
                    setEmail(e.target.value)
                }
                style={{
                    width: "100%",
                    padding: 14,
                    marginBottom: 20,
                    borderRadius: 8,
                    border: "none",
                }}
            />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) =>
                    setPassword(e.target.value)
                }
                style={{
                    width: "100%",
                    padding: 14,
                    marginBottom: 30,
                    borderRadius: 8,
                    border: "none",
                }}
            />

            <button
                onClick={handleLogin}
                style={{
                    width: "100%",
                    padding: 14,
                    background: "#2563eb",
                    color: "white",
                    border: "none",
                    borderRadius: 8,
                    cursor: "pointer",
                    fontWeight: 700,
                }}
            >
                Login
            </button>
            <div
    style={{
        textAlign: "center",
        marginTop: 20,
    }}
>
    {/* <span>Don't have an account? </span> */}

    <div
    style={{
        textAlign: "center",
        marginTop: 22,
        color: "#cbd5e1",
        fontSize: 15,
    }}
>
    Don't have an account?{" "}

    <button
        onClick={() => navigate("/register")}
        style={{
            background: "transparent",
            border: "none",
            color: "#60a5fa",
            cursor: "pointer",
            fontWeight: 700,
            fontSize: 15,
        }}
    >
        Register
    </button>
</div>
</div>
        </div>
    );
};

export default Login;
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { register } from "../../api/auth";

const Register = () => {

    const navigate = useNavigate();

    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    async function handleRegister() {

        if (
            !firstName ||
            !lastName ||
            !username ||
            !email ||
            !password ||
            !confirmPassword
        ) {
            alert("Please fill all fields.");
            return;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        try {

            await register({
                first_name: firstName,
                last_name: lastName,
                username: username,
                email: email,
                password: password,
            });

            alert("Registration successful.");

            navigate("/");

        } catch (err: any) {

    console.log(err);

    console.log(err.response);

    console.log(err.response?.data);

    alert(JSON.stringify(err.response?.data));

}

    }

    return (

        <div
            style={{
                width: 430,
                background: "#1e293b",
                padding: 40,
                borderRadius: 12,
                color: "white",
                boxShadow: "0 0 20px rgba(0,0,0,.4)",
            }}
        >

            <h1
                style={{
                    marginBottom: 10,
                }}
            >
                Create Account
            </h1>

            <p
                style={{
                    color: "#94a3b8",
                    marginBottom: 30,
                }}
            >
                Register to OptiRoute AI
            </p>

            <input
                type="text"
                placeholder="First Name"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                style={inputStyle}
            />
            <input
                type="text"
                placeholder="Last Name"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                style={inputStyle}
            />
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                style={inputStyle}
            />
            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                style={inputStyle}
            />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                style={inputStyle}
            />

            <input
                type="password"
                placeholder="Confirm Password"
                value={confirmPassword}
                onChange={(e) =>
                    setConfirmPassword(e.target.value)
                }
                style={inputStyle}
            />

            <button
                onClick={handleRegister}
                style={{
                    width: "100%",
                    padding: 14,
                    background: "#2563eb",
                    color: "white",
                    border: "none",
                    borderRadius: 8,
                    cursor: "pointer",
                    fontWeight: 700,
                    marginTop: 15,
                }}
            >
                Register
            </button>

            <div
                style={{
                    marginTop: 25,
                    textAlign: "center",
                    color: "#cbd5e1",
                }}
            >
                Already have an account?

                <button
                    onClick={() => navigate("/")}
                    style={{
                        background: "transparent",
                        border: "none",
                        color: "#60a5fa",
                        marginLeft: 5,
                        cursor: "pointer",
                        fontWeight: 700,
                    }}
                >
                    Login
                </button>

            </div>

        </div>

    );

};

const inputStyle = {

    width: "100%",
    padding: 14,
    marginBottom: 18,
    borderRadius: 8,
    border: "none",

} as const;

export default Register;
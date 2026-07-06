import { Outlet } from "react-router-dom";

export default function AuthLayout() {
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                background: "#0f172a",
            }}
        >
            <Outlet />
        </div>
    );
}
import { useEffect, useState, type ReactElement } from "react";
import { Navigate } from "react-router-dom";
import { me } from "../api/auth";

export default function ProtectedRoute({
    children,
}: {
    children: ReactElement;
}) {
    const [loading, setLoading] = useState(true);
    const [authenticated, setAuthenticated] = useState(false);

    useEffect(() => {
        async function verify() {
            try {
                await me();
                setAuthenticated(true);
            } catch {
                localStorage.clear();
                setAuthenticated(false);
            } finally {
                setLoading(false);
            }
        }

        verify();
    }, []);

    if (loading) return <h2>Loading...</h2>;

    return authenticated ? children : <Navigate to="/" replace />;
}
import { createContext, useContext, useEffect, useState } from "react";
import { me } from "../api/auth";

type AuthContextType = {
    loggedIn: boolean;
    loading: boolean;
    login: () => void;
    logout: () => void;
};

const AuthContext = createContext<AuthContextType>(null!);

export function AuthProvider({
    children,
}: {
    children: React.ReactNode;
}) {

    const [loggedIn, setLoggedIn] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function verify() {

            const token = localStorage.getItem("token");

            if (!token) {
                setLoading(false);
                return;
            }

            try {
                await me();
                setLoggedIn(true);
            } catch {

                localStorage.removeItem("token");
                setLoggedIn(false);

            } finally {

                setLoading(false);

            }

        }

        verify();

    }, []);

    function login() {

        setLoggedIn(true);

    }

    function logout() {

        localStorage.removeItem("token");
        setLoggedIn(false);

    }

    return (
        <AuthContext.Provider
            value={{
                loggedIn,
                loading,
                login,
                logout,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    return useContext(AuthContext);
}
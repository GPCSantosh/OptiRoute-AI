import { useEffect } from "react";
import AppRouter from "./router/AppRouter";

function App() {
    useEffect(() => {
        console.log(
            "Google Maps API Key:",
            import.meta.env.VITE_GOOGLE_MAPS_API_KEY
        );
    }, []);

    return <AppRouter />;
}

export default App;
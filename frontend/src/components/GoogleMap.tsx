import {
    GoogleMap,
    LoadScript,
    Marker,
} from "@react-google-maps/api";

const containerStyle = {
    width: "100%",
    height: "600px",
};

const center = {
    lat: 17.728,
    lng: 83.304,
};

export default function GoogleMapComponent() {
    return (
        <LoadScript
            googleMapsApiKey={
                import.meta.env.VITE_GOOGLE_MAPS_API_KEY
            }
        >
            <GoogleMap
                mapContainerStyle={containerStyle}
                center={center}
                zoom={13}
            >
                <Marker position={center} />
            </GoogleMap>
        </LoadScript>
    );
}
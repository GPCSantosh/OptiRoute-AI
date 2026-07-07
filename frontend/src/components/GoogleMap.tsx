import { useEffect, useState } from "react";
import {
    GoogleMap,
    LoadScript,
    Marker,
} from "@react-google-maps/api";

import { getWarehouses } from "../api/warehouses";

const containerStyle = {
    width: "100%",
    height: "650px",
};

const center = {
    lat: 17.728,
    lng: 83.304,
};

export default function GoogleMapComponent() {

    const [warehouses, setWarehouses] = useState<any[]>([]);

    useEffect(() => {

        async function load() {

            try {

                const data = await getWarehouses();

                setWarehouses(data);

            } catch (err) {

                console.error(err);

            }

        }

        load();

    }, []);

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

                {warehouses.map((warehouse) => (

                    <Marker

                        key={warehouse.id}

                        position={{
                            lat: warehouse.latitude,
                            lng: warehouse.longitude,
                        }}

                        title={warehouse.warehouse_name}

                    />

                ))}

            </GoogleMap>

        </LoadScript>

    );

}
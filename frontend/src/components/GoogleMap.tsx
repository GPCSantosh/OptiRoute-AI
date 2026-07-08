import { GoogleMap, Marker, useJsApiLoader } from "@react-google-maps/api";
import { useEffect, useState } from "react";
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

  const { isLoaded } = useJsApiLoader({
    id: "google-map-script",
    googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
  });

  useEffect(() => {
    async function load() {
      try {
        const data = await getWarehouses();
        console.log("Warehouses:", data);
        setWarehouses(data);
      } catch (err) {
        console.error(err);
      }
    }

    load();
  }, []);

  if (!isLoaded) return <h2>Loading Google Maps...</h2>;

  return (
    <GoogleMap
      mapContainerStyle={containerStyle}
      center={center}
      zoom={12}
    >
      {warehouses.map((warehouse) => (
        <Marker
          key={warehouse.id}
          position={{
            lat: Number(warehouse.latitude),
            lng: Number(warehouse.longitude),
          }}
          title={warehouse.warehouse_name}
        />
      ))}
    </GoogleMap>
  );
}
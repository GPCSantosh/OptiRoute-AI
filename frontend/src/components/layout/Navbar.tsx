import "../../styles/navbar.css";

export default function Navbar() {

    return (

        <header className="navbar">

            <input
                placeholder="Search..."
            />

            <div className="profile">

                <span>🔔</span>

                <span>Admin</span>

            </div>

        </header>

    );

}
import { Link, useLocation } from "react-router-dom"
import {BiMenu} from "react-icons/bi";

function Header() {
    const location = useLocation();
    return (
        <div className='header'>
            <Link to="/" className='return-link'>
                <BiMenu />
                {location.pathname === '/'? <h2>Home</h2> : <h2>Go Back</h2> }
            </Link>
        </div>
    );
}

export default Header;
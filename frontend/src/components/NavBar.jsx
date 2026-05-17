import { Link, NavLink } from "react-router-dom";

export default function Navbar() {
  return (
    <header className="navbar">
      <Link to="/" className="logo">
        <div className="logo-icon">✉️</div>
        <div>
          <h2>SpamGuard</h2>
          <span>AI SMS Protection</span>
        </div>
      </Link>

      <nav className="nav-links">
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/feature">Feature</NavLink>
        <NavLink to="/contact">Contact</NavLink>
      </nav>
    </header>
  );
}
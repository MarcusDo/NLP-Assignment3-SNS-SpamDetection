import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import About from "./pages/About";
import Feature from "./pages/Feature";
import Contact from "./pages/Contact";

export default function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/feature" element={<Feature />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </>
  );
}
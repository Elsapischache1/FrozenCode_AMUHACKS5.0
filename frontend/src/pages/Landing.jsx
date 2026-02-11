import "../styles/landing.css";
import catImage from "../assets/cat_landing.png"; // replace with your image
import { useNavigate } from "react-router-dom";

const Landing = () => {
  const navigate = useNavigate();

  return (
    <div className="landing-container">

      {/* Big Background Title */}
      <h1 className="hero-title">SYNAPSE</h1>

      {/* Cat Image */}
      <img
        src={catImage}
        alt="Synapse Cat"
        className="hero-cat"
      />

      {/* Text Content */}
      <div className="text-content fade-in">
        <p className="tagline">Bridge the Gap.</p>

        <button
          className="begin-btn"
          onClick={() => navigate("/skills")}
        >
          Let’s Begin
        </button>
      </div>

    </div>
  );
};

export default Landing;

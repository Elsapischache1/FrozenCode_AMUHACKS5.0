import "../styles/landing.css";
import introVideo from "../assets/intro.mp4";
import { useNavigate } from "react-router-dom";

const Landing = () => {
  const navigate = useNavigate();

  return (
    <div className="landing-container">
      {/* Video */}
      <video
        className="intro-video"
        src={introVideo}
        autoPlay
        loop
        muted
      />

      {/* Text */}
      <div className="text-content fade-in">
        <h1 className="title">Synapse</h1>
        <p className="tagline">Bridge the ap.</p>

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

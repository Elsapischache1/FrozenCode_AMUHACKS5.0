import "../styles/pathSelection.css";
import { useNavigate, useLocation } from "react-router-dom";

const PathSelection = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const skill = location.state?.skill || "Python";

  const sendChoice = async (choice) => {
    if (choice === "quiz") {
      try {
        console.log("Connecting to backend...");
        
        const response = await fetch("http://127.0.0.1:8000/quiz/start", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ skill: skill }),
        });

        if (response.ok) {
          console.log("Success! Navigating to quiz...");
          navigate("/quiz", { state: { skill } });
        } else {
          const errorText = await response.text();
          alert(`Backend Error: ${errorText}`);
        }
      } catch (error) {
        console.error("Connection failed:", error);
        alert("Cannot connect to server at http://127.0.0.1:8000. \n\nMake sure your Python backend is running!");
      }
    } else {
      // Manual Path (Beginner)
      navigate("/result", { 
        state: { 
          level: "Beginner", 
          score: 0,
          manual: true,
          skill: skill
        } 
      });
    }
  };

  return (
    <div className="path-container">
      <h1 className="path-title">Choose Your Path</h1>
      <p className="path-subtitle">Selected Skill: <strong>{skill}</strong></p>

      <div className="path-buttons">
        <button onClick={() => sendChoice("beginner")}>
         <img src={require("../assets/luna-reading.png")} alt="Beginner" />
         <span>I'm a Beginner</span>
        </button>

        <button onClick={() => sendChoice("quiz")}>
         <img src={require("../assets/luna-thinking.png")} alt="Quiz" />
         <span>Take Self‑Assessment Quiz</span>
        </button>
      </div>
    </div>
  );
};

export default PathSelection;
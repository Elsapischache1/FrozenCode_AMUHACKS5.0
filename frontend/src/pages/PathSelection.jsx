import "../styles/pathSelection.css";
import { useNavigate } from "react-router-dom";

const PathSelection = () => {
  const navigate = useNavigate();

  const sendChoice = async (choice) => {
    console.log("User choice:", choice);

    // later → POST to backend
    // await fetch("/path/select", {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify({ choice }),
    // });

    if (choice === "beginner") {
      navigate("/result", {
        state: {
          level: "Beginner",
          score: 0, // optional, but useful
        },
      });
    }

    if (choice === "quiz") {
      navigate("/quiz");
    }
  };

  return (
    <div className="path-container">
      <h1 className="path-title">Choose Your Path</h1>
      <p className="path-subtitle">
        Let us tailor the learning experience for you
      </p>

      <div className="path-buttons">
        <button onClick={() => sendChoice("beginner")}>
          I’m a Beginner
        </button>

        <button onClick={() => sendChoice("quiz")}>
          Take Self‑Assessment Quiz
        </button>
      </div>
    </div>
  );
};

export default PathSelection;

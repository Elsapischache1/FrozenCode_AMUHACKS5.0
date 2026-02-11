import "../styles/result.css";
import { useLocation } from "react-router-dom";

const Result = () => {
  const location = useLocation();
  const { level = "Beginner", score = 0 } = location.state || {};

  const recommendations = {
    Beginner: {
      courses: [
        "Python Basics on Coursera",
        "CS50 Introduction to Programming",
      ],
      projects: [
        "Calculator App",
        "Number Guessing Game",
      ],
      motivation:
        "Every expert was once a beginner. Stay consistent and keep building!",
    },
    Intermediate: {
      courses: [
        "Data Structures & Algorithms",
        "Object-Oriented Programming",
      ],
      projects: [
        "Quiz Application",
        "Task Manager App",
      ],
      motivation:
        "You’re making strong progress. Push a little harder — greatness is close!",
    },
    Advanced: {
      courses: [
        "System Design",
        "Advanced Algorithms",
      ],
      projects: [
        "Full‑Stack Web App",
        "AI‑Powered Assistant",
      ],
      motivation:
        "You’re operating at an advanced level. Now aim for mastery 🚀",
    },
  };

  const data = recommendations[level];

  return (
    <div className="result-container">
      <h1>Your Assessment Result</h1>

      <div className="result-card">
        <p><strong>Level:</strong> {level}</p>
        <p><strong>Score:</strong> {score}/15</p>
      </div>

      <h2>📚 Recommended Courses</h2>
      <ul>
        {data.courses.map((c, i) => (
          <li key={i}>{c}</li>
        ))}
      </ul>

      <h2>🛠 Recommended Projects</h2>
      <ul>
        {data.projects.map((p, i) => (
          <li key={i}>{p}</li>
        ))}
      </ul>

      <p className="motivation">✨ {data.motivation}</p>
    </div>
  );
};

export default Result;

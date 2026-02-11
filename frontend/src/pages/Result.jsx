import "../styles/result.css";
import { useEffect, useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
// 1. Import the Chatbot component
import Chatbot from "../components/Chatbot";

const Result = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const [resultData, setResultData] = useState(null);
  const [loading, setLoading] = useState(true);

  // Get the skill from navigation state (defaults to Python if not found)
  const skill = location.state?.skill || "Python";

  // Recommendations Data
  const recommendations = {
    Beginner: {
      courses: [
        { title: "CS50's Introduction to Programming", link: "https://cs50.harvard.edu/python/" },
        { title: "100 Days of Code: Python Bootcamp", link: "https://www.udemy.com/course/100-days-of-code/" }
      ],
      projects: [
        { title: "Number Guessing Game", desc: "Basic loops and conditionals practice." },
        { title: "Basic Calculator", desc: "CLI tool for math operations." },
        { title: "Mad Libs Generator", desc: "String manipulation mastery." }
      ],
      motivation: "Every expert was once a beginner. Keep going!",
    },
    Intermediate: {
      courses: [
        { title: "Python for Data Science (Coursera)", link: "https://www.coursera.org/learn/python-for-applied-data-science-ai" },
        { title: "Intermediate Python Nanodegree", link: "https://www.udacity.com/course/intermediate-python-nanodegree--nd303" }
      ],
      projects: [
        { title: "Weather App (API)", desc: "Fetch data from web APIs." },
        { title: "URL Shortener", desc: "Database interactions." },
        { title: "Automated Price Tracker", desc: "Web scraping and automation." }
      ],
      motivation: "You have a solid foundation. Now let's build real systems.",
    },
    Advanced: {
      courses: [
        { title: "Cosmic Python (Architecture)", link: "https://www.cosmicpython.com/" },
        { title: "Deep Learning Specialization", link: "https://www.deeplearning.ai/" }
      ],
      projects: [
        { title: "Real-time Chat App", desc: "Websockets and AsyncIO." },
        { title: "Custom Blockchain", desc: "Cryptography and data structures." },
        { title: "AI Content Generator", desc: "LLM integration." }
      ],
      motivation: "You are operating at a professional level. Aim for mastery.",
    },
  };

  useEffect(() => {
    // 1. Manual Mode (User clicked "I'm a Beginner")
    if (location.state?.manual) {
      setResultData({
        final_level: "beginner",
        scores: { beginner: 0, intermediate: 0, advanced: 0 }
      });
      setLoading(false);
      return;
    }

    // 2. Fetch from Backend (Calculated Result)
    const fetchResults = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/quiz/result");
        if (response.ok) {
          const data = await response.json();
          setResultData(data);
        } else {
          console.error("Failed to fetch results");
          alert("Could not load results. Please try again.");
        }
      } catch (err) {
        console.error("Error fetching results:", err);
        alert("Could not connect to backend.");
      } finally {
        setLoading(false);
      }
    };

    fetchResults();
  }, [location.state]);

  if (loading) return <div className="result-container"><h2>Analyzing Performance...</h2></div>;
  if (!resultData) return <div className="result-container"><h2>No results found.</h2></div>;

  // --- LOGIC ---
  const backendLevel = resultData.final_level || "beginner";
  const formattedLevel = backendLevel.charAt(0).toUpperCase() + backendLevel.slice(1);
  const data = recommendations[formattedLevel] || recommendations["Beginner"];

  // Display scores for all levels
  const scores = resultData.scores || {};

  return (
    <div className="result-container">
      <h1>Assessment Complete</h1>

      <div className="result-card">
        <p className="final-level">Assessed Level: <strong>{formattedLevel}</strong></p>
        <div className="score-breakdown">
          <p>Beginner: {scores.beginner || 0}/5</p>
          <p>Intermediate: {scores.intermediate || 0}/5</p>
          <p>Advanced: {scores.advanced || 0}/5</p>
        </div>
      </div>

      <h2>📚 Recommended Path</h2>
      <ul className="course-list">
        {data.courses.map((course, i) => (
          <li key={i}><a href={course.link} target="_blank" rel="noreferrer">{course.title}</a></li>
        ))}
      </ul>

      <h2>🛠 Project Ideas</h2>
      <ul className="project-list">
        {data.projects.map((p, i) => (
          <li key={i}><strong>{p.title}</strong>: {p.desc}</li>
        ))}
      </ul>

      <div className="motivation-box">
        <p>"{data.motivation}"</p>
      </div>

      <button className="restart-btn" onClick={() => navigate("/")}>Back to Home</button>

      {/* 2. Add the Chatbot component and pass required props */}
      <Chatbot skill={skill} level={formattedLevel} />
    </div>
  );
};

export default Result;
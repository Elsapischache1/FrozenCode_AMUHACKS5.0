import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "../styles/quiz.css";

const Quiz = () => {
  const { state } = useLocation();
  const navigate = useNavigate();
  const skill = state?.skill || "Python";

  // We will loop through these levels
  const LEVEL_ORDER = ["beginner", "intermediate", "advanced"];

  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [loading, setLoading] = useState(true);
  
  // Track which stage of the quiz we are in
  const [levelIndex, setLevelIndex] = useState(0); 
  const currentLevel = LEVEL_ORDER[levelIndex];

  // Fetch Question Function
  const fetchQuestion = async () => {
    setLoading(true);
    try {
      // 1. Ask backend for question for current level
      const res = await fetch(`http://127.0.0.1:8000/quiz/question/${currentLevel}`);
      const data = await res.json();

      if (data.error) {
        alert("Session expired. Restarting.");
        navigate("/path");
        return;
      }

      // 2. If this level is DONE
      if (data.done) {
        // Check if there is a next level
        if (levelIndex < LEVEL_ORDER.length - 1) {
          console.log(`Level ${currentLevel} finished. Moving to ${LEVEL_ORDER[levelIndex + 1]}`);
          setLevelIndex(prev => prev + 1); // Move to next level
          // The useEffect will trigger the fetch for the new level
        } else {
          // No more levels? Go to Result
          navigate("/result");
        }
      } else {
        // 3. If valid question, show it
        setCurrentQuestion(data);
      }
    } catch (err) {
      console.error("Failed to load question", err);
      alert("Error connecting to backend. Please check if the server is running.");
    }
    setLoading(false);
  };

  // Trigger fetch whenever levelIndex changes (or on mount)
  useEffect(() => {
    fetchQuestion();
    // eslint-disable-next-line
  }, [levelIndex]);

  const handleOptionSelect = async (index) => {
    const answerPayload = {
      level: currentLevel,
      selected_option: index + 1 
    };

    try {
      await fetch("http://127.0.0.1:8000/quiz/answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(answerPayload),
      });

      // Fetch next question immediately
      fetchQuestion();
    } catch (err) {
      console.error("Error submitting answer", err);
    }
  };

  if (loading) {
    return (
      <div className="quiz-container loading-screen">
        <div className="spinner"></div>
        <h2>Generating {currentLevel} question...</h2>
      </div>
    );
  }

  if (!currentQuestion) return null;

  return (
    <div className="quiz-container">
      <h1 className="quiz-title">{skill} Assessment</h1>
      <div className="level-badge">Level: {currentLevel.charAt(0).toUpperCase() + currentLevel.slice(1)}</div>
      
      <div className="question-card">
        <h3 className="question-text">{currentQuestion.question}</h3>

        <div className="options-grid">
          {currentQuestion.options.map((opt, idx) => (
            <button
              key={idx}
              className="option-btn"
              onClick={() => handleOptionSelect(idx)}
            >
              {opt}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Quiz;
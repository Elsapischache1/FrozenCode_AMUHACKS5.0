import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "../styles/quiz.css";

const quizData = [
  // BEGINNER (5)
  { q: "What is Python?", options: ["Snake", "Programming Language", "Car", "OS"], answer: 1 },
  { q: "Which keyword is used to define a function?", options: ["func", "define", "def", "function"], answer: 2 },
  { q: "What is a variable?", options: ["Value", "Container", "Loop", "Class"], answer: 1 },
  { q: "Which symbol is used for comments?", options: ["//", "#", "/*", "<!--"], answer: 1 },
  { q: "Which data type stores text?", options: ["int", "float", "string", "bool"], answer: 2 },

  // INTERMEDIATE (5)
  { q: "Which loop runs at least once?", options: ["for", "while", "do-while", "foreach"], answer: 2 },
  { q: "What does OOP stand for?", options: ["Object Oriented Programming", "Open Object Process", "Order Of Program", "None"], answer: 0 },
  { q: "Which keyword creates an object in Java?", options: ["make", "new", "create", "object"], answer: 1 },
  { q: "Time complexity of binary search?", options: ["O(n)", "O(log n)", "O(n²)", "O(1)"], answer: 1 },
  { q: "Stack follows which principle?", options: ["FIFO", "LIFO", "Random", "Priority"], answer: 1 },

  // ADVANCED (5)
  { q: "Which data structure uses recursion heavily?", options: ["Array", "Tree", "Queue", "Stack"], answer: 1 },
  { q: "What is polymorphism?", options: ["One form", "Many forms", "Inheritance", "Encapsulation"], answer: 1 },
  { q: "Which algorithm uses divide and conquer?", options: ["Bubble Sort", "Merge Sort", "Linear Search", "Insertion Sort"], answer: 1 },
  { q: "Which is immutable in Python?", options: ["List", "Set", "Dictionary", "Tuple"], answer: 3 },
  { q: "What does API stand for?", options: ["Application Programming Interface", "Advanced Program Input", "Applied Process Interface", "None"], answer: 0 },
];

const Quiz = () => {
  const { state } = useLocation();
  const navigate = useNavigate();
  const skill = state?.skill || "Skill";

  const [answers, setAnswers] = useState({});

  const selectOption = (qIndex, optIndex) => {
    setAnswers({ ...answers, [qIndex]: optIndex });
  };

  const allAnswered = Object.keys(answers).length === quizData.length;

  const handleSubmit = () => {
    if (!allAnswered) return;

    let score = 0;
    quizData.forEach((q, i) => {
      if (answers[i] === q.answer) score++;
    });

    let level = "Beginner";
    if (score >= 11) level = "Advanced";
    else if (score >= 6) level = "Intermediate";

    navigate("/result", {
      state: {
        score,
        level,
      },
    });
  };

  return (
    <div className="quiz-container">
      <h1 className="quiz-title">{skill} Self‑Assessment</h1>

      {quizData.map((item, qIndex) => (
        <div key={qIndex} className="question-card">
          <h3 className="question-text">
            Q{qIndex + 1}. {item.q}
          </h3>

          <div className="options-grid">
            {item.options.map((opt, optIndex) => (
              <label key={optIndex} className="option">
                <input
                  type="radio"
                  name={`question-${qIndex}`}
                  checked={answers[qIndex] === optIndex}
                  onChange={() => selectOption(qIndex, optIndex)}
                />
                <span>{opt}</span>
              </label>
            ))}
          </div>
        </div>
      ))}

      <button
        className={`submit-btn ${!allAnswered ? "disabled" : ""}`}
        onClick={handleSubmit}
        disabled={!allAnswered}
      >
        Submit Quiz
      </button>

      {!allAnswered && (
        <p className="warning-text">
          Please answer all questions before submitting.
        </p>
      )}
    </div>
  );
};

export default Quiz;

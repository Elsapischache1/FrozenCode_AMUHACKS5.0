import { useNavigate } from "react-router-dom";
import "../styles/skillDevelopment.css";

const skills = [
  {
    name: "Python",
    description:
      "Learn syntax, variables, loops, functions, and basics of Python programming.",
    enabled: true,
  },
  {
    name: "Java",
    description:
      "Understand OOP concepts, classes, objects, and Java fundamentals.",
    enabled: false,
  },
  {
    name: "Problem Solving",
    description:
      "Improve your ability to break down problems and design solutions.",
    enabled: false,
  },
  {
    name: "Logical Reasoning",
    description:
      "Sharpen logical thinking, patterns, and analytical skills.",
    enabled: false,
  },
];

const SkillDevelopment = () => {
  const navigate = useNavigate();

  const handleClick = (skill) => {
    if (skill.enabled && skill.name === "Python") {
      // Pass skill name to PathSelection
      navigate("/path", { state: { skill: skill.name } });
    }
  };

  return (
    <div className="skill-container">
      <h1>Select a Skill</h1>

      <div className="skill-grid">
        {skills.map((skill) => (
          <div
            key={skill.name}
            className={`skill-card ${!skill.enabled ? "locked" : ""}`}
            onClick={() => handleClick(skill)}
          >
            <h2>{skill.name}</h2>
            <p>{skill.description}</p>

            {!skill.enabled && (
              <span className="lock-text">🔒 Locked</span>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default SkillDevelopment;
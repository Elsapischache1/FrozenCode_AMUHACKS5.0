import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Landing from "./pages/Landing";
import SkillDevelopment from "./pages/SkillDevelopment";
import PathSelection from "./pages/PathSelection";
import Quiz from "./pages/Quiz";
import Result from "./pages/Result";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/skills" element={<SkillDevelopment />} />
        <Route path="/path" element={<PathSelection />} />
        <Route path="/quiz" element={<Quiz />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </Router>
  );
}

export default App;

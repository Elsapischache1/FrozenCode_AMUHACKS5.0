import google.generativeai as genai
import json
import os

# CONFIGURATION - Use environment variable for API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
MODEL_NAME = "gemini-2.0-flash"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

# --- FALLBACK STATIC QUESTIONS (In case API fails) ---
STATIC_QUESTIONS = {
    "beginner": [
        {"question": "What is the correct file extension for Python files?", "options": [".pt", ".pyth", ".py", ".ptr"], "answer": 3},
        {"question": "How do you output text to the console in Python?", "options": ["echo()", "print()", "console.log()", "write()"], "answer": 2},
        {"question": "Which of these is a valid variable name?", "options": ["2myvar", "my-var", "my_var", "my var"], "answer": 3},
        {"question": "What keyword is used to define a function?", "options": ["func", "def", "function", "define"], "answer": 2},
        {"question": "How do you create a list in Python?", "options": ["{}", "[]", "()", "<>"], "answer": 2}
    ],
    "intermediate": [
        {"question": "Which method adds an element to the end of a list?", "options": ["add()", "push()", "insert()", "append()"], "answer": 4},
        {"question": "What is the output of len([1, 2, 3])?", "options": ["2", "3", "4", "Error"], "answer": 2},
        {"question": "How do you handle exceptions in Python?", "options": ["try/except", "do/catch", "try/catch", "attempt/fail"], "answer": 1},
        {"question": "Which of these is a mutable data type?", "options": ["Tuple", "String", "List", "Integer"], "answer": 3},
        {"question": "What does the 'break' statement do?", "options": ["Stops the program", "Exits the current loop", "Skips to the next iteration", "Restarts the loop"], "answer": 2}
    ],
    "advanced": [
        {"question": "What is a lambda function?", "options": ["A named function", "A loop structure", "An anonymous function", "A class method"], "answer": 3},
        {"question": "What is the purpose of __init__?", "options": ["To terminate a class", "To initialize an object", "To import a library", "To clear memory"], "answer": 2},
        {"question": "What does the GIL stand for?", "options": ["Global Interpreter Lock", "General Interface Library", "Global Interface Lock", "General Interpreter List"], "answer": 1},
        {"question": "Which decorator is used to define a static method?", "options": ["@classmethod", "@staticmethod", "@public", "@void"], "answer": 2},
        {"question": "What is the time complexity of looking up an item in a set?", "options": ["O(n)", "O(log n)", "O(1)", "O(n^2)"], "answer": 3}
    ]
}

def generate_questions_for_level(skill: str, level: str, count: int = 5):
    """
    Tries to generate questions using AI. Returns STATIC if API fails.
    """
    print(f"   -> Fetching {level} questions for {skill}...")
    
    # Check if API key is set
    if GEMINI_API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️ API Key not set. Using static questions.")
        return STATIC_QUESTIONS.get(level, STATIC_QUESTIONS["beginner"])
    
    try:
        prompt = f"""
        Generate {count} {level} level multiple choice questions on "{skill}".
        Rules:
        - Return ONLY valid JSON array.
        - Exactly 4 options per question.
        - "answer" must be a NUMBER (1-4).
        - No markdown formatting.
        
        Example: [{{"question": "...", "options": ["A", "B", "C", "D"], "answer": 1}}]
        """
        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        
        # Clean markdown if present
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
        
        raw_text = raw_text.strip()
            
        questions = json.loads(raw_text)
        if isinstance(questions, list) and len(questions) > 0:
            print(f"   ✓ Generated {len(questions)} AI questions")
            return questions
    except Exception as e:
        print(f"⚠️ AI Generation Failed ({e}). Using Backup.")
    
    return STATIC_QUESTIONS.get(level, STATIC_QUESTIONS["beginner"])

class QuizEngine:
    def __init__(self, skill="Python"):
        self.skill = skill
        self.current_level = "beginner"
        self.scores = {"beginner": 0, "intermediate": 0, "advanced": 0}
        self.current_index = 0
        
        # Initialize with Beginner questions. 
        # Intermediate/Advanced are None until we actually reach them (Lazy Load).
        self.questions_cache = {
            "beginner": generate_questions_for_level(skill, "beginner"),
            "intermediate": None, 
            "advanced": None
        }

    def switch_level(self, level: str):
        """Switches level and generates questions if not already present."""
        print(f"🔄 Switching to {level}...")
        self.current_level = level
        self.current_index = 0
        
        # LAZY LOAD: If we haven't fetched questions for this level yet, do it now.
        if self.questions_cache[level] is None:
            self.questions_cache[level] = generate_questions_for_level(self.skill, level)

    def get_next_question(self):
        qs = self.questions_cache[self.current_level]
        if self.current_index >= len(qs):
            return None # Indicates this level is done
        return qs[self.current_index]

    def submit_answer(self, selected_option: int):
        qs = self.questions_cache[self.current_level]
        if self.current_index < len(qs):
            q = qs[self.current_index]
            if selected_option == q["answer"]:
                self.scores[self.current_level] += 1
                print(f"   ✓ Correct! Score: {self.scores[self.current_level]}")
            else:
                print(f"   ✗ Incorrect. Correct answer was: {q['answer']}")
            self.current_index += 1

    def final_level(self):
        """
        Determine level based on performance with smart logic:
        - If you ace beginner AND intermediate, you're ready for advanced
        - If you score well on intermediate (4+), you're intermediate+
        - Progressive assessment based on cumulative performance
        """
        beginner_score = self.scores.get("beginner", 0)
        intermediate_score = self.scores.get("intermediate", 0)
        advanced_score = self.scores.get("advanced", 0)
        
        # If you aced or nearly aced both beginner AND intermediate (4-5 on each),
        # you should get advanced recommendations regardless of advanced score
        if beginner_score >= 4 and intermediate_score >= 4:
            return "advanced"
        
        # If you did well on intermediate (4+), you're at intermediate level
        if intermediate_score >= 4:
            return "intermediate"
        
        # If you passed intermediate with decent score (3), check advanced
        if intermediate_score >= 3 and advanced_score >= 2:
            return "advanced"
        
        # Standard check: did well on intermediate
        if intermediate_score >= 3:
            return "intermediate"
        
        # Default to beginner
        return "beginner"
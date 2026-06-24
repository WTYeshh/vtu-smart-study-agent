import os
import json
from typing import List, Dict, Any
import google.generativeai as genai
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger("quiz_generator")

class QuizGenerator:
    """Skill to generate quizzes using Gemini LLM from syllabus modules and notes."""

    def __init__(self):
        # Configure Gemini API if key is present
        if Config.GEMINI_API_KEY and Config.GEMINI_API_KEY != "your_api_key_here":
            genai.configure(api_key=Config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            self.api_available = True
        else:
            self.api_available = False
            logger.warning("Gemini API key not configured or set to default value. QuizGenerator will use mock generation.")

    def generate_quiz(self, topic: str, content_context: str, num_questions: int = 5) -> List[Dict[str, Any]]:
        """Generates multiple-choice quiz questions from the provided content context."""
        logger.info(f"Generating a quiz for topic: {topic} with {num_questions} questions.")

        if not self.api_available:
            return self._generate_mock_quiz(topic, num_questions)

        prompt = f"""
        You are an expert tutor helper for Visvesvaraya Technological University (VTU) courses.
        Generate a quiz with {num_questions} multiple-choice questions based on the following course content:
        
        {content_context}
        
        For each question, provide:
        1. The question text.
        2. Four options (A, B, C, D).
        3. The correct option letter (A, B, C, or D).
        4. A brief explanation of the correct answer.

        Format the output strictly as a JSON list of objects:
        [
          {{
            "question": "...",
            "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
            "correct_answer": "A",
            "explanation": "..."
          }}
        ]
        """

        try:
            response = self.model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            data = json.loads(response.text)
            return data
        except Exception as e:
            logger.error(f"Failed to generate quiz with Gemini API: {e}. Falling back to mock generator.")
            return self._generate_mock_quiz(topic, num_questions)

    def _generate_mock_quiz(self, topic: str, num_questions: int) -> List[Dict[str, Any]]:
        """Fallback mock quiz generator for development/offline mode."""
        logger.info("Using mock quiz generator.")
        mock_questions = []
        for i in range(1, num_questions + 1):
            mock_questions.append({
                "question": f"Sample Question {i} about {topic} under the VTU syllabus?",
                "options": {
                    "A": "Option A explanation and answer detail",
                    "B": "Option B explanation and answer detail",
                    "C": "Option C explanation and answer detail",
                    "D": "Option D explanation and answer detail"
                },
                "correct_answer": "A",
                "explanation": f"This is a placeholder explanation for sample question {i}."
            })
        return mock_questions

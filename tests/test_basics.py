import os
import unittest
from utils.config import Config
from memory.database import init_db, get_db_connection
from agents.manager_agent import ManagerAgent

class TestStudyAgentBasics(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Override config database path to a test database during testing
        Config.DATABASE_URL = "sqlite:///vtu_test_study.db"
        init_db()

    @classmethod
    def tearDownClass(cls):
        # Clean up testing database
        if os.path.exists("vtu_test_study.db"):
            try:
                os.remove("vtu_test_study.db")
            except Exception:
                pass

    def test_database_connection(self):
        conn = get_db_connection()
        self.assertIsNotNone(conn)
        cursor = conn.cursor()
        
        # Verify schema tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row["name"] for row in cursor.fetchall()]
        self.assertIn("study_plans", tables)
        self.assertIn("quiz_results", tables)
        self.assertIn("chat_memory", tables)
        conn.close()

    def test_manager_routing_fallback(self):
        manager = ManagerAgent()
        # General query should trigger the manager fallback introduction
        result = manager.route_and_execute("hello there, who are you?")
        self.assertEqual(result["agent"], "manager")
        self.assertIn("VTU Smart Study Agent", result["response"])

    def test_manager_routing_quiz(self):
        manager = ManagerAgent()
        result = manager.route_and_execute("please generate a quiz for me")
        self.assertEqual(result["agent"], "quiz")
        self.assertIn("Generated a new quiz", result["response"])

if __name__ == "__main__":
    unittest.main()

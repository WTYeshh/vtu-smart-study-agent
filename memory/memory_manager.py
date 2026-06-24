from typing import List, Dict, Any
from .database import get_db_connection
from utils.logger import setup_logger

logger = setup_logger("memory_manager")

class MemoryManager:
    """Manages reading and writing execution states, progress, and chat memory."""
    
    @staticmethod
    def save_chat_message(session_id: str, role: str, message: str) -> None:
        """Stores a chat exchange in the memory database."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO chat_memory (session_id, role, message) VALUES (?, ?, ?)",
                (session_id, role, message)
            )
            conn.commit()
        except Exception as e:
            logger.error(f"Failed to save chat message: {e}")
        finally:
            conn.close()

    @staticmethod
    def get_chat_history(session_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Retrieves recent chat history for context window loading."""
        conn = get_db_connection()
        history = []
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT role, message, timestamp FROM chat_memory WHERE session_id = ? ORDER BY timestamp DESC LIMIT ?",
                (session_id, limit)
            )
            rows = cursor.fetchall()
            # Rows are returned latest first, so reverse to maintain conversation order
            for row in reversed(rows):
                history.append({
                    "role": row["role"],
                    "message": row["message"],
                    "timestamp": row["timestamp"]
                })
        except Exception as e:
            logger.error(f"Failed to fetch chat history: {e}")
        finally:
            conn.close()
        return history

    @staticmethod
    def save_study_plan(plan_items: List[Dict[str, Any]]) -> None:
        """Saves a batch of study plan items."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            for item in plan_items:
                cursor.execute(
                    """INSERT INTO study_plans (subject_code, subject_name, topic, module, planned_date, status)
                       VALUES (?, ?, ?, ?, ?, ?)""",
                    (
                        item.get("subject_code"),
                        item.get("subject_name"),
                        item.get("topic"),
                        item.get("module"),
                        item.get("planned_date"),
                        item.get("status", "PENDING")
                    )
                )
            conn.commit()
        except Exception as e:
            logger.error(f"Failed to save study plan: {e}")
        finally:
            conn.close()

    @staticmethod
    def get_study_plan(subject_code: str = None) -> List[Dict[str, Any]]:
        """Retrieves active study plans."""
        conn = get_db_connection()
        plans = []
        try:
            cursor = conn.cursor()
            if subject_code:
                cursor.execute("SELECT * FROM study_plans WHERE subject_code = ? ORDER BY module, planned_date", (subject_code,))
            else:
                cursor.execute("SELECT * FROM study_plans ORDER BY subject_code, module, planned_date")
            
            for row in cursor.fetchall():
                plans.append(dict(row))
        except Exception as e:
            logger.error(f"Failed to fetch study plans: {e}")
        finally:
            conn.close()
        return plans

    @staticmethod
    def record_quiz_score(subject_code: str, module: int, score: int, total: int) -> None:
        """Saves quiz evaluation results."""
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO quiz_results (subject_code, module, score, total_questions) VALUES (?, ?, ?, ?)",
                (subject_code, module, score, total)
            )
            conn.commit()
        except Exception as e:
            logger.error(f"Failed to record quiz score: {e}")
        finally:
            conn.close()

from datetime import datetime, timedelta
from typing import List, Dict, Any
from utils.logger import setup_logger

logger = setup_logger("planner_skill")

class StudyPlanner:
    """Skill to organize syllabus modules into chronological schedules."""

    @staticmethod
    def create_schedule(
        subject_code: str,
        subject_name: str,
        modules: List[Dict[str, Any]],
        start_date_str: str = None,
        days_per_module: int = 7
    ) -> List[Dict[str, Any]]:
        """Maps structured modules/topics onto specific calendar dates.
        
        Args:
            subject_code: e.g. "21CS51"
            subject_name: e.g. "Database Management Systems"
            modules: List of dicts representing syllabus modules/topics, e.g.
                     [{"module": 1, "topics": ["Introduction", "Entity Relationship Model"]}]
            start_date_str: ISO format date string, defaults to today
            days_per_module: Duration assigned to study each module
        """
        logger.info(f"Generating study plan schedule for {subject_name} starting {start_date_str or 'today'}")
        
        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            except ValueError:
                logger.warning(f"Invalid date format '{start_date_str}', expected YYYY-MM-DD. Defaulting to today.")
                start_date = datetime.today()
        else:
            start_date = datetime.today()

        schedule = []
        current_date = start_date

        for mod in modules:
            module_num = mod.get("module", 1)
            topics = mod.get("topics", ["Overview"])
            
            # Distribute topics across the days allocated for the module
            days_allocated = max(len(topics), days_per_module)
            days_increment = days_allocated / len(topics) if topics else days_per_module
            
            for idx, topic in enumerate(topics):
                planned_date = current_date + timedelta(days=int(idx * days_increment))
                schedule.append({
                    "subject_code": subject_code,
                    "subject_name": subject_name,
                    "module": module_num,
                    "topic": topic,
                    "planned_date": planned_date.strftime("%Y-%m-%d"),
                    "status": "PENDING"
                })
            
            # Advance start date for the next module
            current_date += timedelta(days=days_allocated)

        logger.info(f"Generated plan with {len(schedule)} topics.")
        return schedule

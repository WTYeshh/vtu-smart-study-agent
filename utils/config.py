import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    """Configuration class containing environment variable values."""
    
    # API configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    
    # DB configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///vtu_study.db")
    
    # Logging configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls) -> bool:
        """Validates critical config configurations."""
        if not cls.GEMINI_API_KEY or cls.GEMINI_API_KEY == "your_api_key_here":
            return False
        return True

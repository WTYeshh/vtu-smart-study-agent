from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from memory.database import init_db
from agents.manager_agent import ManagerAgent
from utils.logger import setup_logger

logger = setup_logger("app_api")

# Initialize database schema
try:
    init_db()
except Exception as e:
    logger.error(f"Failed to auto-initialize DB: {e}")

app = FastAPI(
    title="VTU Smart Study Agent API",
    description="Backend services for VTU Multi-Agent Study Assistant",
    version="1.0.0"
)

# Shared ManagerAgent instance
manager = ManagerAgent()

class ChatRequest(BaseModel):
    query: str
    session_id: str = "default_api_session"

class ChatResponse(BaseModel):
    query: str
    agent: str
    response: str

@app.get("/")
def get_root():
    return {
        "status": "online",
        "service": "VTU Smart Study Agent API",
        "message": "Welcome! Use POST /chat to interact with the study agents."
    }

@app.post("/chat", response_model=ChatResponse)
def post_chat(req: ChatRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    
    try:
        result = manager.route_and_execute(req.query, req.session_id)
        return ChatResponse(
            query=result["query"],
            agent=result["agent"],
            response=result["response"]
        )
    except Exception as e:
        logger.error(f"API chat execution failure: {e}")
        raise HTTPException(status_code=500, detail=str(e))

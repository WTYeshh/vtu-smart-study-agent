import sys
from memory.database import init_db
from agents.manager_agent import ManagerAgent
from utils.logger import setup_logger

logger = setup_logger("main_cli")

def main():
    logger.info("Starting VTU Smart Study Agent (CLI)...")
    
    # Auto-initialize database tables on run
    try:
        init_db()
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        sys.exit(1)

    manager = ManagerAgent()
    print("=" * 60)
    print("Welcome to the VTU Smart Study Agent CLI!")
    print("Ask me anything about syllabus, notes, quizzes, or planning.")
    print("Type 'exit' or 'quit' to terminate the session.")
    print("=" * 60)

    session_id = "cli_session"

    while True:
        try:
            user_input = input("\nStudent > ").strip()
            if not user_input:
                continue
            
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye! Happy studying!")
                break
                
            result = manager.route_and_execute(user_input, session_id)
            
            print(f"\n[Agent: {result['agent'].upper()}]")
            print(result["response"])
            
        except KeyboardInterrupt:
            print("\nGoodbye! Happy studying!")
            break
        except Exception as e:
            logger.error(f"Execution error: {e}")
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# app.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from decouple import config

from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks

from langchain.tools import DuckDuckGoSearchRun

# Initialize the DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

# Load environment variables
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# Define request and response schemas
class CrewRequest(BaseModel):
    var1: str
    var2: str

class CrewResponse(BaseModel):
    result: str

# Initialize FastAPI app
app = FastAPI(
    title="Crew AI API",
    description="API for running custom Crew AI tasks",
    version="1.0.0",
)

# Define the CustomCrew class
class CustomCrew:
    def __init__(self, var1: str, var2: str):
        self.var1 = var1
        self.var2 = var2

    def run(self) -> dict:
        agents = CustomAgents()
        tasks = CustomTasks()

        # Initialize custom agents
        agent1 = agents.agent_1_name()
        agent2 = agents.agent_2_name()
        agent3 = agents.agent_3_name()
        agent4 = agents.agent_4_name()
   

        # Initialize custom tasks
        task1 = tasks.task_1_name(agent1, self.var1, self.var2)
        task2 = tasks.task_2_name(agent2)
        task3 = tasks.task_3_name(agent3)
        task4 = tasks.task_4_name(agent4)

        # Create and run the crew
        crew = Crew(
        agents=[agent1, agent2, agent3, agent4],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        )
        crew_output = crew.kickoff()

        return {"output": getattr(crew_output, 'raw', str(crew_output))}


# In CustomCrew.run()


# Update Crew


# Define the API endpoint
@app.post("/run_agents", response_model=CrewResponse)
async def run_crew(crew_request: CrewRequest):
    """
    Run the custom Crew AI with provided variables.

    - **var1**: Economic variable 1 (e.g., inflation rate)
    - **var2**: Economic variable 2 (e.g., government spending)
    """
    try:
        custom_crew = CustomCrew(crew_request.var1, crew_request.var2)
        result = custom_crew.run()
        return CrewResponse(result=result["output"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "Welcome to the Crew AI API. Use /docs for API documentation."}

# Entry point for running the app
if __name__ == "__main__":
    uvicorn.run("your_module_name:app", host="127.0.0.1", port=8000, reload=True)